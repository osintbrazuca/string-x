import re
from utils.functions import Funcs


class FuncFormat:
    def __init__(self):
        self._func_name_list = [func for func in dir(Funcs) if func.startswith('_') is False] 

    def __find_func(self, func_name: str, value: str) -> str:
        if func_name and value:
            for attribute in self._func_name_list:
                # atributo é uma string que representa o nome do função / method
                if attribute in func_name:
                    attribute_value = getattr(Funcs, attribute)
                    return attribute_value(value)
    @staticmethod
    def __detect_func(text: str, func_name: str) -> list[any]:
        if text and func_name:
            # procurando padrão de função na string {text}
            findall = re.findall(rf'({func_name}\((.*?)\))',text,re.MULTILINE)
            return findall
    
    def func_format(self,cmd_str:str) -> str: 
        if cmd_str:  
            func_detect_list = [] 
            [ func_detect_list.extend(self.__detect_func(cmd_str, func_name)) for func_name in self._func_name_list ]
            for func_detect,value_func in func_detect_list:
                cmd_str = cmd_str.replace(
                    func_detect,
                    self.__find_func(func_detect,value_func)
                )
            return cmd_str
    

