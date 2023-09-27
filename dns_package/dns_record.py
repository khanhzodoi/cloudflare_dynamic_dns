
class DNSRecord():
    def __init__(self, type, name, content, proxied=False, ttl=3600, comment=""):
        self._type = type
        self._name = name
        self._content = content
        self._proxied = proxied
        self._ttl = ttl
        self._comment = comment
    
    @property
    def name(self):
        return self._name
    
    @property
    def type(self):
        return self._type
    
    @property
    def content(self):
        return self._content
    
    @property
    def proxied(self):
        return self._proxied
    
    @property
    def ttl(self):
        return self._ttl
    
    @property
    def comment(self):
        return self._comment
    
    def __str__(self) -> str:
        return f"Name: {self._name} - Type: {self._type} - Content: {self._content}" 
    
