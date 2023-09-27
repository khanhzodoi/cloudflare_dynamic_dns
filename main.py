from dns_package.dns_zone import DNSZone
from dns_package.dns_record import DNSRecord
from utils.ip import get_public_ip
from utils.file import load_credential
from utils.file import load_config
from utils.logger import get_logger


if __name__ == "__main__":
    config_file = "config.toml"

    # Load configuration from config.toml
    config = load_config(config_file)
    if not config:
        print("Failed to load config. Exit script(1)")
        exit(1)

    # Initialize logger
    logger = get_logger(config["paths"]["log_file_path"])
    if not logger:
        print("Failed to init logger. Exit script(1)")
        exit(1)

    logger.info("> Loading credential...")
    credential = load_credential(logger, config["paths"]["credential_file_path"])
    if not credential or credential is None:
        logger.error("Failed to load credential. Exit script(1)")
        exit(1)
        
    logger.info("> Initializing DNSZone...")
    dns_zone = DNSZone(logger, credential["zone_identifier"], credential["email_account"], credential["api_token"])
    dns_zone.list_dns_records()

    logger.info("> Getting current public IP...")
    current_public_ip = get_public_ip()

    if not current_public_ip:
        logger.error("Failed to retrieve public IP address.")
        exit(1)

    logger.info("> Initializing DNS Record...")
    www_khanhpham_uk_record = DNSRecord(name="www.khanhpham.uk", type="A", content=current_public_ip, proxied=False, ttl=3600, comment="www.khanhpham.us")

    logger.info("> Updating DNS Record...")
    dns_zone.update_dns_record(www_khanhpham_uk_record)
