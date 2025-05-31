from random import Random
import urllib.parse
import re
import base64
import hashlib
import yaml


class Format:
    """
    A utility class for various string formatting and encoding operations.

    Methods:
        clear_value(value: str) -> str:
            Removes leading and trailing whitespace and tabs, newlines, and carriage returns from the string.

        decode64(value: str) -> str:
            Decodes a base64 encoded string.

        encode64(value: str) -> str:
            Encodes a string into base64.

        sha1(value: str) -> str:
            Generates a SHA-1 hash of the string.

        sha256(value: str) -> str:
            Generates a SHA-256 hash of the string.

        encodehex(value: str) -> str:
            Encodes a string into its hexadecimal representation.

        decodehex(value: str) -> str:
            Decodes a hexadecimal string back to its original string.

        md5(value: str) -> str:
            Generates an MD5 hash of the string.

        json(value: str):
            Parses a YAML string into a Python object.

        regex(value: str, regex: str) -> str:
            Finds all occurrences of a regex pattern in the string.

        parse_urlencode(url: str) -> str:
            Encodes a URL string using URL encoding.
    """

    @staticmethod
    def clear_value(value: str) -> str:
        if value:
            value = value.strip()
            value = re.sub(r'[\t\n\r]', '', value)
            return value
        return str()

    @staticmethod
    def decode64(value: str) -> str:
        if value:
            try:
                return base64.b64decode(value.encode(), validate=False).decode("utf-8", "ignore")
            except Exception:
                pass
        return str()

    @staticmethod
    def encode64(value: str) -> str:
        if value:
            return base64.b64encode(value.encode()).decode("utf-8", "ignore")
        return str()

    @staticmethod
    def sha1(value: str) -> str:
        if value:
            return hashlib.sha1(str(value).encode('utf-8')).hexdigest()
        return str()

    @staticmethod
    def sha256(value: str) -> str:
        if value:
            return hashlib.sha256(str(value).encode('utf-8')).hexdigest()
        return str()

    @staticmethod
    def encodehex(value: str) -> str:
        if value:
            str_hex = value.encode('utf-8')
            return str_hex.hex()
        return str()

    @staticmethod
    def decodehex(value: str) -> str:
        if value:
            return bytes.fromhex(value).decode('utf-8')
        return str()

    @staticmethod
    def md5(value: str) -> str:
        if value:
            return hashlib.md5(str(value).encode('utf-8')).hexdigest()
        return str()

    @staticmethod
    def json(value: str):
        if value:
            return yaml.load(value, yaml.SafeLoader)
        return None

    @staticmethod
    def regex(value: str, regex: str) -> str:
        if value:
            re_result =  re.findall(regex, value, re.IGNORECASE)
            if re_result:
                return re_result
        return str()

    @staticmethod
    def parse_urlencode(url: str) -> str:
        if url:
            encode =  urllib.parse.urlencode(url)
            if encode:
                return encode
        return str()     

