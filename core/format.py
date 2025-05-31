"""
Módulo de formatação e codificação de strings.

Este módulo contém a classe Format que fornece diversos métodos utilitários
para formatação, codificação, decodificação e geração de hashes de strings.
É utilizado para processar e transformar dados durante a execução de comandos.
"""
from random import Random
import urllib.parse
import re
import base64
import hashlib
import yaml


class Format:
    """
    Classe utilitária para diversas operações de formatação e codificação de strings.

    Esta classe fornece métodos estáticos para limpeza de strings, codificação/decodificação
    base64, geração de hashes e outras operações de transformação de dados.

    Methods:
        clear_value(value: str) -> str: Remove espaços e caracteres de quebra de linha
        decode64(value: str) -> str: Decodifica string base64
        encode64(value: str) -> str: Codifica string em base64
        sha1(value: str) -> str: Gera hash SHA-1 da string
        sha256(value: str) -> str: Gera hash SHA-256 da string
        encodehex(value: str) -> str: Codifica string em representação hexadecimal
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

