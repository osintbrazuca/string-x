from core.basemodule import BaseModule
import re

class AuxRegexURL(BaseModule):
    """Módulo para extrair URLs de strings"""
    
    def __init__(self):
        super().__init__()
        self.meta = {
            "name": "Extractor de URLs",
            "description": "Extrai URLs de strings",
            "author": "MrCl0wn",
            "type":"extractor"
        }
        self.options = {
            "data": str(),
            "regex": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?:/[-\w%/.]*)*(?:\?[-\w%&=.]*)?',
        }
    
    def run(self):
        """
        Extrai URLs de uma string
        Utiliza uma expressão regular para identificar URLs no texto fornecido.
        Args:
            None
        Returns:
            None
        """

        # Verifica se há dados para processar
        if (target_value := self.options.get("data")) and (regex_data := self.options.get("regex")): 
            regex_data = re.compile(regex_data,re.IGNORECASE)
            if regex_result_list := set(re.findall(regex_data, target_value)):
                for value_regex in regex_result_list:
                    if value_regex.startswith(('http://', 'https://')):
                        # Armazenar resultados
                        self.set_result(value_regex)
