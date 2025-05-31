"""
Módulo extrator de números de telefone.

Este módulo implementa funcionalidade para extrair números de telefone brasileiros
de textos usando expressões regulares. Faz parte do sistema de módulos auxiliares
do String-X.
"""
from core.basemodule import BaseModule
import re

class Phone(BaseModule):
    """
    Módulo para extração de números de telefone usando regex.

    Este módulo herda de BaseModule e fornece funcionalidade específica para
    identificar e extrair números de telefone brasileiros de strings de texto.

    Attributes:
        meta (dict): Metadados do módulo incluindo nome, descrição, autor e tipo
        options (dict): Opções requeridas incluindo dados de entrada e padrão regex
    """
    
    def __init__(self):
        """
        Inicializa o módulo extrator de telefones.
        
        Configura os metadados do módulo e define as opções necessárias,
        incluindo o padrão regex para detecção de números de telefone brasileiros.
        """
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
        Executa o processo de extração de números de telefone.
        
        Utiliza os dados fornecidos e o padrão regex configurado para identificar
        e extrair números de telefone válidos. Os telefones encontrados são
        armazenados nos resultados do módulo.
        
        O processo inclui:
        1. Verificação da disponibilidade de dados e padrão regex
        2. Compilação do padrão regex com flag IGNORECASE
        3. Busca por números de telefone no texto
        4. Armazenamento dos resultados únicos encontrados
        """
        # Verifica se há dados para processar
        if (target_value := self.options.get("data")) and (regex_data := self.options.get("regex")): 
            regex_data = re.compile(regex_data, re.IGNORECASE)
            if regex_result_list := set(re.findall(regex_data, target_value)):
                for value_regex in regex_result_list:
                    self.set_result(value_regex)

            
    