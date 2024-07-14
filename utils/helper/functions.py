import socket
from core.request import Request
from core.format import Format
from core.randomvalue import RandomValue

class Funcs:
    def __init__(self):
        ...

    @staticmethod
    def clear(value: str) -> str:
        if value:
            return Format.clear_value(value)
        return str()

    @staticmethod
    def debase64(value: str) -> str:
        if value:
            return Format.decode64(value)
        return str()

    @staticmethod
    def base64(value: str) -> str:
        if value:
            return Format.encode64(value)
        return str()

    @staticmethod
    def sha1(value: str) -> str:
        if value:
            return Format.sha1(value)
        return str()

    @staticmethod
    def sha256(value: str) -> str:
        if value:
            return Format.sha256(value)
        return str()

    @staticmethod
    def hex(value: str) -> str:
        if value:
            return Format.encodehex(value)
        return str()

    @staticmethod
    def dehex(value: str) -> str:
        if value:
            return Format.decodehex(value)
        return str()

    @staticmethod
    def md5(value: str) -> str:
        if value:
            return Format.md5(value)
        return str()

    @staticmethod
    def str_rand(len_int: str) -> str:
        if len_int:
            return RandomValue.get_str_rand(len_int)
        return str()

    @staticmethod
    def int_rand(len_int: str) -> str:
        if len_int:
            return str(RandomValue.get_int_rand(len_int))
        return str()

    @staticmethod
    def ip(host: str) -> str:
        if host:
            try:
                return socket.gethostbyname(host)
            except socket.gaierror:
                pass
        return str()

    @staticmethod
    def replace(value: str) -> str:
        if value:
            old, new, cmd = value.split(',')
            if old and new and cmd: 
                return cmd.replace(old, new)
        return str() 
        
    @staticmethod
    def get(url: str) -> str:
        if url.startswith('https://') or url.startswith('http://'):
            request = Request()
            try:
                result = request.get(url)
                if result:
                    return result
            except Exception:
                pass
        return str() 
    
    @staticmethod
    def urlencode(url: str) -> str:
        if url:
           encode = Format.parse_urlencode(url)
           if encode:
               return encode
        return str()
    
    @staticmethod
    def rev(value: str) -> str:
        if value:
            value_rev = value[::-1]
            if value_rev:
                return value_rev
        return str()
           
    
