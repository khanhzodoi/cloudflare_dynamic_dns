"""Module providing a DNSRecord to manage dns records of any kinds"""
from dataclasses import dataclass

@dataclass
class DNSRecord:
    """DNSRecord for managing dns records"""
    record_type: str
    name: str
    content: str
    proxied: bool = False
    ttl: int = 3600
    comment: str = ""

    def __str__(self) -> str:
        return f"Name: {self.name} - Type: {self.record_type} - Content: {self.content}"
