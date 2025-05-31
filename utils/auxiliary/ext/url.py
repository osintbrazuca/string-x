"""
Módulo extrator de URLs.

Este módulo implementa funcionalidade para extrair URLs de textos usando
expressões regulares. Faz parte do sistema de módulos auxiliares do String-X.
"""
from core.basemodule import BaseModule
import re

class AuxRegexURL(BaseModule):
    """
    Módulo para extração de URLs usando regex.

    Este módulo herda de BaseModule e fornece funcionalidade específica para
    identificar e extrair URLs válidas de strings de texto.

    Attributes:
        meta (dict): Metadados do módulo incluindo nome, descrição, autor e tipo
        options (dict): Opções requeridas incluindo dados de entrada e padrão regex
    """
    
    def __init__(self):
        """
        Inicializa o módulo extrator de URLs.
        
        Configura os metadados do módulo e define as opções necessárias,
        incluindo o padrão regex para detecção de URLs HTTP/HTTPS.
        """
        super().__init__()
        self.meta = {
            "name": "Extractor de URLs",
            "description": "Extrai URLs de strings",
            "author": "MrCl0wn",
            "type": "extractor"
        }
        self.options = {
            "data": str(),
            "regex": r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?:/[-\w%/.]*)*(?:\?[-\w%&=.]*)?',
        }
    
    def run(self):
        """
        Executa o processo de extração de URLs.
        
        Utiliza os dados fornecidos e o padrão regex configurado para identificar
        e extrair URLs válidas que começam com http:// ou https://. As URLs
        encontradas são armazenadas nos resultados do módulo.
        
        O processo inclui:
        1. Verificação da disponibilidade de dados e padrão regex
        2. Compilação do padrão regex com flag IGNORECASE
        3. Busca por URLs no texto
        4. Validação de que as URLs começam com http:// ou https://
        5. Armazenamento dos resultados únicos encontrados
        """
        # Verifica se há dados para processar
        if (target_value := self.options.get("data")) and (regex_data := self.options.get("regex")): 
            regex_data = re.compile(regex_data, re.IGNORECASE)
            if regex_result_list := set(re.findall(regex_data, target_value)):
                for value_regex in regex_result_list:
                    if value_regex.startswith(('http://', 'https://')):
                        # Armazenar resultados
                        self.set_result(value_regex)
