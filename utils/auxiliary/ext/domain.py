from core.basemodule import BaseModule
import re

class AuxRegexDomain(BaseModule):
    """Módulo para extrair domínios de strings"""
    
    def __init__(self):
        super().__init__()
        self.meta = {
            "name": "Extractor de Domínios",
            "description": "Extrai domínios de strings fornecidas",
            "author": "MrCl0wn",
            "version": "1.0",
            "type":"extractor"
        }
        
        # Lista de TLDs válidos mais comuns
        tlds = ['com', 'org', 'net', 'edu', 'gov', 'mil', 'int', 'co', 'io', 'ai', 'app', 'dev',
            'br', 'us', 'uk', 'ca', 'de', 'fr', 'it', 'es', 'au', 'jp', 'cn', 'in', 'ru',
            'com.br', 'gov.br', 'org.br', 'net.br', 'edu.br', 'mil.br',
            # Novos TLDs genéricos
            'info', 'biz', 'name', 'pro', 'aero', 'asia', 'cat', 'coop', 'jobs', 'mobi', 
            'museum', 'tel', 'travel', 'xxx', 'xyz', 'online', 'site', 'tech', 'store',
            'web', 'blog', 'shop', 'cloud', 'host', 'space', 'media', 'news', 'live',
            # Mais ccTLDs (country code)
            'eu', 'nl', 'be', 'ch', 'at', 'se', 'no', 'dk', 'fi', 'pl', 'cz', 'sk',
            'hu', 'ro', 'bg', 'gr', 'pt', 'ie', 'is', 'lt', 'lv', 'ee', 'si', 'hr',
            'mx', 'ar', 'cl', 'pe', 'co', 've', 'ec', 'uy', 'py', 'bo', 'cr', 'pa',
            'za', 'eg', 'ma', 'ng', 'ke', 'tn', 'ae', 'sa', 'il', 'tr', 'ua', 'kz',
            'sg', 'my', 'th', 'vn', 'id', 'ph', 'kr', 'tw', 'hk', 'mo', 'nz', 'au']
        
        # Regex com validação de TLD
        tld_pattern = '|'.join(re.escape(tld) for tld in tlds)
        
        self.options = {
            "data": str(),
            "regex": rf'(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{{0,61}}[a-zA-Z0-9])?\.)+(?:{tld_pattern})\b'
        }
        
    def run(self):
        """
        Implementação principal do módulo que extrai domínios
        
        Args:
            data (str): String de entrada para processamento
            **kwargs: Argumentos opcionais adicionais
        """
    
        # Verifica se há dados para processar
        if (target_value := self.options.get("data")) and (regex_data := self.options.get("regex")): 
            regex_data = re.compile(regex_data, re.IGNORECASE)
            if regex_result_list := set(re.findall(regex_data, target_value)):
                for value_regex in regex_result_list:
                    self.set_result(value_regex)
            