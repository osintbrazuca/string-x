"""
Módulo extrator de endereços de email.

Este módulo implementa funcionalidade para extrair endereços de email de textos
usando expressões regulares. Faz parte do sistema de módulos auxiliares do String-X.
"""
import re
from core.basemodule import BaseModule

class AuxRegexEmail(BaseModule):
    """
    Módulo para extração de endereços de email usando regex.

    Este módulo herda de BaseModule e fornece funcionalidade específica para
    identificar e extrair endereços de email válidos de strings de texto.

    Attributes:
        meta (dict): Metadados do módulo incluindo nome, descrição, autor e tipo
        options (dict): Opções requeridas incluindo dados de entrada e padrão regex

    Methods:
        __init__(): Inicializa o módulo com metadados e configurações
        run(): Executa o processo de extração de emails
    """
    def __init__(self):
        """
        Inicializa o módulo extrator de emails.
        
        Configura os metadados do módulo e define as opções necessárias,
        incluindo o padrão regex para detecção de emails.
        """
        super().__init__()

        # Define informações de meta do módulo
        self.meta.update({
            "name": "Extractor de Emails",
            "description": "Extrai emails do texto fornecido",
            "author": "MrCl0wn",
            "type": "extractor"
        })

        # Define opções requeridas para este módulo
        self.options = {
            "data": str(),
            "regex": "(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21\\x23-\\x5b\\x5d-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\\x01-\\x08\\x0b\\x0c\\x0e-\\x1f\\x21-\\x5a\\x53-\\x7f]|\\\\[\\x01-\\x09\\x0b\\x0c\\x0e-\\x7f])+)\\])"
        }

    def run(self):
        """
        Executa o processo de extração de emails.
        
        Utiliza os dados fornecidos e o padrão regex configurado para identificar
        e extrair endereços de email válidos. Os emails encontrados são armazenados
        nos resultados do módulo.
        
        O processo inclui:
        1. Verificação da disponibilidade de dados e padrão regex
        2. Compilação do padrão regex com flag IGNORECASE
        3. Busca por emails no texto
        4. Armazenamento dos resultados únicos encontrados
        """
        # Verifica se há dados para processar
        if (target_value := self.options.get("data")) and (regex_data := self.options.get("regex")): 
            regex_data = re.compile(regex_data, re.IGNORECASE)
            if regex_result_list := set(re.findall(regex_data, target_value)):
                for value_regex in regex_result_list:
                    self.set_result(value_regex)
