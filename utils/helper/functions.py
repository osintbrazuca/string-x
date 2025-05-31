"""
Módulo de funções auxiliares.

Este módulo contém a classe Funcs com métodos estáticos que implementam
diversas funções auxiliares para formatação, codificação, rede e manipulação
de dados. Essas funções são utilizadas pelo sistema de templates dinâmicos.
"""
import socket
import datetime
import json
from urllib.parse import urlparse
from core.request import Request
from core.format import Format
from core.randomvalue import RandomValue


class Funcs:
    """
    Classe com funções auxiliares estáticas.
    
    Esta classe fornece um conjunto de métodos estáticos para diversas
    operações como codificação/decodificação, hash, geração de valores
    aleatórios, resolução DNS e manipulação de URLs.
    """
    def __init__(self):
        ...

    @staticmethod
    def clear(value: str) -> str:
        """
        Limpa e formata uma string removendo caracteres especiais.
        
        Args:
            value (str): String a ser limpa
            
        Returns:
            str: String limpa ou string vazia
        """
        if value:
            return Format.clear_value(value)
        return str()

    @staticmethod
    def debase64(value: str) -> str:
        """
        Decodifica string de Base64.
        
        Args:
            value (str): String codificada em Base64
            
        Returns:
            str: String decodificada ou string vazia
        """
        if value:
            return Format.decode64(value)
        return str()

    @staticmethod
    def base64(value: str) -> str:
        """
        Codifica string em Base64.
        
        Args:
            value (str): String a ser codificada
            
        Returns:
            str: String codificada em Base64 ou string vazia
        """
        if value:
            return Format.encode64(value)
        return str()

    @staticmethod
    def sha1(value: str) -> str:
        """
        Gera hash SHA1 de uma string.
        
        Args:
            value (str): String para gerar hash
            
        Returns:
            str: Hash SHA1 ou string vazia
        """
        if value:
            return Format.sha1(value)
        return str()

    @staticmethod
    def sha256(value: str) -> str:
        """
        Gera hash SHA256 de uma string.
        
        Args:
            value (str): String para gerar hash
            
        Returns:
            str: Hash SHA256 ou string vazia
        """
        if value:
            return Format.sha256(value)
        return str()

    @staticmethod
    def hex(value: str) -> str:
        """
        Codifica string em hexadecimal.
        
        Args:
            value (str): String a ser codificada
            
        Returns:
            str: String codificada em hex ou string vazia
        """
        if value:
            return Format.encodehex(value)
        return str()

    @staticmethod
    def dehex(value: str) -> str:
        """
        Decodifica string hexadecimal.
        
        Args:
            value (str): String em hexadecimal
            
        Returns:
            str: String decodificada ou string vazia
        """
        if value:
                        return Format.decodehex(value)
        return str()

    @staticmethod
    def md5(value: str) -> str:
        """
        Gera hash MD5 de uma string.
        
        Args:
            value (str): String para gerar hash
            
        Returns:
            str: Hash MD5 ou string vazia
        """
        if value:
            return Format.md5(value)
        return str()

    @staticmethod
    def str_rand(len_int: str) -> str:
        """
        Gera string aleatória de caracteres alfanuméricos.
        
        Args:
            len_int (str): Comprimento da string
            
        Returns:
            str: String aleatória ou string vazia
        """
        if len_int:
            return RandomValue.get_str_rand(len_int)
        return str()

    @staticmethod
    def int_rand(len_int: str) -> str:
        """
        Gera string de números aleatórios.
        
        Args:
            len_int (str): Quantidade de números
            
        Returns:
            str: String de números aleatórios ou string vazia
        """
        if len_int:
            return str(RandomValue.get_int_rand(len_int))
        return str()

    @staticmethod
    def ip(host: str) -> str:
        """
        Resolve hostname para endereço IP.
        
        Args:
            host (str): Hostname ou domínio
            
        Returns:
            str: Endereço IP ou string vazia se falhar
        """
        if host:
            try:
                return socket.gethostbyname(host)
            except socket.gaierror:
                pass
        return str()

    @staticmethod
    def replace(value: str) -> str:
        """
        Substitui substring em uma string.
        
        Args:
            value (str): String no formato "old,new,texto"
            
        Returns:
            str: String com substituição aplicada ou string vazia
        """
        if value:
            old, new, cmd = value.split(',')
            if old and new and cmd: 
                return cmd.replace(old, new)
        return str() 
        
    @staticmethod
    def get(url: str) -> str:
        """
        Faz requisição HTTP GET para uma URL.
        
        Args:
            url (str): URL para requisição
            
        Returns:
            str: Resposta da requisição ou string vazia
        """
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
        """
        Codifica URL.
        
        Args:
            url (str): URL a ser codificada
            
        Returns:
            str: URL codificada ou string vazia
        """
        if url:
           encode = Format.parse_urlencode(url)
           if encode:
               return encode
        return str()
    
    @staticmethod
    def rev(value: str) -> str:
        """
        Inverte uma string.
        
        Args:
            value (str): String a ser invertida
            
        Returns:
            str: String invertida ou string vazia
        """
        if value:
            value_rev = value[::-1]
            if value_rev:
                return value_rev
        return str()
    
    @staticmethod
    def timestamp(value: str) -> str:
        """
        Retorna timestamp atual formatado.
        
        Args:
            value (str): Formato da data/hora (não utilizado)
            
        Returns:
            str: Timestamp formatado ou string vazia
        """
        if not value:
            return str()

        try:
            return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        except ValueError:
            return str()
        
    @staticmethod
    def extract_domain(value: str) -> str:
        """
        Extrai domínio de uma URL.
        
        Args:
            value (str): URL completa
            
        Returns:
            str: Domínio extraído ou string vazia
        """
        if not value:
            return str()
        
        try:
            parsed = urlparse(value)
            return parsed.netloc or parsed.path.split('/')[0]
        except:
            return str()
           
    
