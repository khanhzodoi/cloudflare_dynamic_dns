"""Module providing a DNSZone class to help add remove update list DNS Record in a specific zone."""
import requests
from requests.exceptions import RequestException
from dns_package.dns_record import DNSRecord


class DNSZone():
    """DNSZone Class"""
    def __init__(self, logger, zone_identifier, email_account, token):
        """
        Constructor for the DNSZone class.

        Args:
            logger (Logger): The logger object for logging.
            zone_identifier (str): Cloudflare zone identifier.
            email_account (str): Cloudflare account email.
            token (str): Cloudflare API token.
        """
        self.cloud_flare_links = {
            "update": "https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}",
            "list": "https://api.cloudflare.com/client/v4/zones/{}/dns_records"
        }
        self.logger = logger
        self.zone_identifier = zone_identifier
        self.email_account = email_account
        self.token = token
        self.dns_records = []
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
            "X-Auth-Email": email_account
        }

    def update_dns_record(self, record):
        """
        Update a DNS record on Cloudflare.

        Args:
            record (DNSRecord): The DNS record object to update.

        Returns:
            None
        """
        if not isinstance(record, DNSRecord):
            self.logger.error(
                "Record is not an instance of DNSRecord or its subclass.")
            return

        self.list_dns_records()
        existing_record = self.find_existing_record(record)

        if existing_record:
            self.update_existing_record(existing_record, record)
        else:
            self.logger.error("Record not found in DNS records.")

    def find_existing_record(self, record):
        """
        Find an existing DNS record on Cloudflare.

        Args:
            record (DNSRecord): The DNS record object to find.

        Returns:
            dict or None: The existing DNS record as a dictionary, or None if not found.
        """
        for each_record in self.dns_records:
            if record.name == each_record["name"] and record.record_type == each_record["type"]:
                return each_record
        return None

    def update_existing_record(self, existing_record, new_record):
        """
        Update an existing DNS record on Cloudflare.

        Args:
            existing_record (dict): The existing DNS record to update.
            new_record (DNSRecord): The new DNS record object with updated values.

        Returns:
            None
        """
        url = self.cloud_flare_links["update"].format(
            self.zone_identifier, existing_record["id"])
        payload = {
            "content": str(new_record.content),
            "name": str(new_record.name),
            "proxied": bool(new_record.proxied),
            "type": str(new_record.record_type),
            "comment": str(new_record.comment),
            "tags": [],
            "ttl": int(new_record.ttl)
        }

        try:
            with requests.request(
                "PUT", url, json=payload, headers=self.headers, timeout=5
            ) as response:
                if response.status_code == 200:
                    data = response.json()
                    self.logger.info(
                        "> Finished updating - Cloudflare response: " +
                        str(data["result"])
                    )
                else:
                    self.logger.error(
                        f"Failed to update record. HTTP status code: {response.status_code}"
                    )

        except RequestException as error:
            self.logger.error(
                f"An error occurred during the request: {str(error)}")

    def add_dns_record(self, record):
        """
        Add a DNS record to the list of DNS records.

        Args:
            record (DNSRecord): The DNS record object to add.

        Returns:
            None
        """
        self.dns_records.append(record)

    def remove_dns_record(self, record):
        """
        Remove a DNS record from the list of DNS records.

        Args:
            record (DNSRecord): The DNS record object to remove.

        Returns:
            None
        """
        if record in self.dns_records:
            self.dns_records.remove(record)

    def list_dns_records(self):
        """
        List DNS records from Cloudflare and update the internal records list.

        Returns:
            None
        """
        url = self.cloud_flare_links["list"].format(self.zone_identifier)

        try:
            with requests.request("GET", url, headers=self.headers, timeout=10) as response:
                if response.status_code == 200:
                    if data := response.json():
                        self.dns_records = data["result"]
                else:
                    self.logger.error(
                        f'There was some error. HTTP status code: {str(response.status_code)}'
                    )

        except RequestException as error:  # Catch network-related exceptions
            self.logger.error('An error occurred during the request:', str(error))
