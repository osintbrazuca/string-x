
"""
Módulo de formatação de funções.

Este módulo contém a classe FuncFormat responsável por detectar e processar
funções especiais dentro de strings de comando, permitindo a execução de
transformações dinâmicas nos dados.
"""
import re
from utils.helper.functions import Funcs


class FuncFormat:
    """
    Classe para formatação e processamento de funções em strings.
    
    Esta classe detecta padrões de função dentro de strings de comando e
    executa as funções correspondentes, substituindo os padrões pelos
    resultados das execuções.
    
    Attributes:
        _func_name_list (list): Lista de nomes de funções disponíveis
        is_func (bool): Flag indicando se funções foram detectadas
    """
    def __init__(self):
        """
        Inicializa FuncFormat com lista de funções disponíveis.
        """
        self._func_name_list: list = [func for func in dir(Funcs) if func.startswith('_') is False] 
        self.is_func: bool = False

    def _find_func(self, func_name: str, value: str) -> str:
        """
        Encontra e executa uma função específica.
        
        Args:
            func_name (str): Nome da função a ser executada
            value (str): Valor a ser passado como parâmetro
            
        Returns:
            str: Resultado da execução da função ou string vazia
        """
        if func_name and value:
            for attribute in self._func_name_list:
                # atributo é uma string que representa o nome do função / method
                if (attribute == str(func_name.split("(")[0])):
                    attribute_value = getattr(Funcs, attribute)
                    return attribute_value(value)
        return str()
                
    def _detect_func(self, text: str, func_name: str) -> list[str]:
        """
        Detecta padrões de função em um texto.
        
        Args:
            text (str): Texto onde buscar padrões de função
            func_name (str): Nome da função a ser detectada
            
        Returns:
            list[str]: Lista de tuplas com função e parâmetros ou None
        """
        if text and func_name:
            # procurando padrão de função na string {text}
            findall = re.findall(rf'({func_name}\((.*?)\))',text,re.MULTILINE)
            if findall:
                return list(set(findall))
            self.is_func = False
            return None
    
    def func_format(self,cmd_str: str) -> str:
        """
        Processa todas as funções detectadas em uma string de comando.
        
        Este método detecta todas as funções presentes na string de comando,
        executa-as e substitui os padrões pelos resultados das execuções.
        
        Args:
            cmd_str (str): String de comando contendo padrões de função
            
        Returns:
            str: String processada com funções substituídas por seus resultados
        """
        if cmd_str:
            func_detect_list = [] 
            for func_name in self._func_name_list:
                detect_func = self._detect_func(cmd_str, func_name)
                if detect_func: func_detect_list.extend(detect_func)
            if func_detect_list:
                for func_detect,value_func in func_detect_list:
                    if func_detect and value_func:
                        self.is_func = True
                        cmd_str = cmd_str.replace(
                            str(func_detect),
                            str(self._find_func(func_detect,value_func))
                        )
            if cmd_str:            
                return cmd_str
        return str()
    

