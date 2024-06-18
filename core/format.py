from random import Random
import re
import base64
import hashlib
import yaml


class Format:

    @staticmethod
    def clear_value(value_str: str) -> str:
        if value_str:
            value_str = value_str.rstrip()
            value_str = re.sub(r'[\t\n\r]', '', value_str)
            return value_str
        return None

    @staticmethod
    def decode64(value_str: str) -> str:
        if value_str:
            return base64.b64decode(value_str).decode('utf-8')
        return None

    @staticmethod
    def encode64(value_str: str):
        if value_str:
            return base64.b64encode(value_str).decode('utf-8')
        return None

    @staticmethod
    def sha1(value_str: str):
        if value_str:
            return hashlib.sha1(str(value_str).encode('utf-8')).hexdigest()
        return None

    @staticmethod
    def sha256(value_str: str):
        if value_str:
            return hashlib.sha256(str(value_str).encode('utf-8')).hexdigest()
        return None

    @staticmethod
    def encodehex(value_str: str):
        if value_str:
            str_hex = value_str.encode('utf-8')
            return str_hex.hex()
        return None

    @staticmethod
    def decodehex(value_str: str):
        if value_str:
            return bytes.fromhex(value_str).decode('utf-8')
        return None

    @staticmethod
    def md5(value_str: str):
        if value_str:
            return hashlib.md5(str(value_str).encode('utf-8')).hexdigest()
        return None

    @staticmethod
    def json(value_str: str):
        if value_str:
            return yaml.load(value_str, yaml.SafeLoader)
        return None
