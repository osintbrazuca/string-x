
import re
from utils.helper.functions import Funcs

class FuncFormat:
    def __init__(self):
        self._func_name_list: list = [func for func in dir(Funcs) if func.startswith('_') is False] 
        self.is_func: bool = False

    def _find_func(self, func_name: str, value: str) -> str:
        if func_name and value:
            for attribute in self._func_name_list:
                # atributo é uma string que representa o nome do função / method
                if (attribute == str(func_name.split("(")[0])):
                    attribute_value = getattr(Funcs, attribute)
                    return attribute_value(value)
        return str()
                
    def _detect_func(self, text: str, func_name: str) -> list[str]:
        if text and func_name:
            # procurando padrão de função na string {text}
            findall = re.findall(rf'({func_name}\((.*?)\))',text,re.MULTILINE)
            if findall:
                return list(set(findall))
            self.is_func = False
            return None
    
    def func_format(self,cmd_str: str) -> str: 
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
    

