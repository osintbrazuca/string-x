"""
Módulo de requisições HTTP.

Este módulo contém a classe Request responsável por fazer requisições HTTP
e extrair informações básicas como código de status e título das páginas.
"""
import httpx
from core.format import Format


class Request:
    """
    Classe para realizar requisições HTTP.
    
    Esta classe fornece métodos para fazer requisições HTTP e extrair
    informações básicas das respostas, como códigos de status e títulos.
    """

    @staticmethod
    def _get_title(html: str) -> str:
        """
        Extrai o título de uma página HTML.
        
        Args:
            html (str): Conteúdo HTML da página
            
        Returns:
            str: Título extraído da página ou string vazia
        """
        if html:
            title = Format.clear_value(Format.regex(html, r'<title[^>]*>([^<]+)</title>')[0])
            title = title.replace("'", "")
            if title:
                return title
        return str()
        

    def get(self, url: str) -> str:
        """
        Realiza requisição GET para uma URL.
        
        Args:
            url (str): URL para fazer a requisição
            
        Returns:
            str: String formatada com código de status e título da página
        """
        if url.startswith('http'):
            try:
                rest = httpx.get(url=url, verify=False, timeout=3)
                if rest.is_success or rest.is_error or rest.is_redirect:
                    return f"{rest.status_code}; {self._get_title(rest.text)}"
            except Exception:
                pass
        return str() 