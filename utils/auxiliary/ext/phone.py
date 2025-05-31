from core.basemodule import BaseModule
import re

class Phone(BaseModule):
    """
    Módulo para extrair números de telefone de strings.
    """
    
    def __init__(self):
        super().__init__()
        
        # Definir metadados do módulo
        self.meta = {
            'name': 'Phone Extractor',
            "author": "MrCl0wn",
            'version': '1.0',
            'description': 'Extrai números de telefone brasileiros',
            'type': 'extractor'
        }
        
        # Definir opções configuráveis
        self.options = {
            'data': str(),    # dados de entrada
            'regex': r'(?:\+?\d{1,3}\s*)?(?:\(?\d{2,3}\)?\s*)?(?:9?\d{4,5}[-.\s]?\d{4})'
        }
    
    def run(self):
        """
        Método principal do módulo.
        
        Args:
            data (str): String contendo possíveis números de telefone
            **kwargs: Argumentos adicionais
            
        Returns:
            list: Lista de números encontrados
        """
        # Verifica se há dados para processar
        if (target_value := self.options.get('data')) and (regex_data := self.options.get('regex')):
            regex_data = re.compile(regex_data, re.IGNORECASE)
            if regex_result_list := set(re.findall(regex_data, target_value)):
                for value_regex in regex_result_list:
                    # Formata o número de telefone conforme as opções
                    self.set_result(value_regex)