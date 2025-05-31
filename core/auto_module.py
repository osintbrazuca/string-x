"""
Módulo responsável pelo carregamento automático de módulos auxiliares.

Este módulo contém a classe AutoModulo que é utilizada para importar automaticamente
módulos e instanciar suas classes. Utiliza importação dinâmica baseada no tipo e nome
do módulo para carregar e executar funcionalidades específicas.
"""
import importlib
import inspect
from core.style_cli import StyleCli

class AutoModulo:
    """
    Classe responsável pelo carregamento automático de módulos.

    Esta classe é utilizada para importar automaticamente um módulo e instanciar sua classe.
    Utiliza o nome do módulo e nome da classe para carregar dinamicamente o módulo e criar
    uma instância da classe.

    Attributes:
        _cli (StyleCli): Instância para interface CLI estilizada
        _valid_type_module (bool): Flag indicando se o módulo é válido
        type_module (str): Tipo do módulo (ex: "extractor", "scanner")
        name_module (str): Nome do módulo (ex: "email", "domain")
        class_instance: Instância da classe carregada
    """
    def __init__(self, type_module_name_module: str):
        """
        Inicializa o AutoModulo com o tipo e nome do módulo.
        
        Args:
            type_module_name_module (str): String no formato 'tipo:nome' do módulo
        """
        self._cli = StyleCli()
        self._valid_type_module = self._check_type_module_name_module(type_module_name_module)

    def _check_type_module_name_module(self,type_module_name_module: str) -> bool:
        """
        Verifica se o tipo de módulo e nome do módulo são válidos.
        
        O tipo de módulo deve ser um tipo válido (ex: "extractor", "scanner", etc.)
        e o nome do módulo deve ser um nome válido (ex: "email", "domain", etc.).
        
        Args:
            type_module_name_module (str): String no formato 'tipo:nome'
            
        Returns:
            bool: True se o formato for válido, False caso contrário
        """
        if ":" not in type_module_name_module:
            self._cli.console.print("[!] Invalid type_module_name_module format. Expected 'type_module:name_module'")
            return False
        type_module, name_module = type_module_name_module.split(':')
        self.type_module = type_module # e.g., "extractor"
        self.name_module = name_module # e.g., "email"
        self.class_instance = None
        if not self.type_module or not self.name_module:
            self._cli.console.print("[!] Invalid type_module or name_module")
            return False
        return True

    def load_module(self):
        """
        Carrega o módulo e instancia a classe definida nele.
        
        O módulo deve estar no formato utils.auxiliary.{type_module}.{name_module}.
        
        Returns:
            object | None: Instância da classe carregada ou None se houver erro
        """
        if not self._valid_type_module:
            self._cli.console.print("[!] Invalid type_module or name_module format")
            return None
        try:
            # self._cli.console.print(f"[*] Importando módulo: {self.type_module}:{self.name_module}")
            obj_centrao = self._instantiate_class()
            if obj_centrao:
                self.class_instance = obj_centrao
                return obj_centrao
            else:
                self._cli.console.print("[!] Failed to instantiate class from module")
                return None
        except ImportError as e:
            self._cli.console.print(f"[!] ImportError: {e}")
            return None
        

    def _import_module(self):
        """
        Importa o módulo usando importlib.
        
        Raises:
            ImportError: Se o módulo não puder ser importado
        """
        try:
            self.module = importlib.import_module(f"utils.auxiliary.{self.type_module}.{self.name_module}")
            # self._cli.console.print(f"[*] Executando módulo: {self.module.__name__}")
        except ImportError as e:
            self._cli.console.print(f"[!] ImportError: {e}")
            raise e

    def _instantiate_class(self):
        """
        Instancia automaticamente a classe encontrada no módulo.
        
        Procura por classes no módulo importado e instancia a primeira classe
        que pertence ao módulo (não importada de outro lugar).
        
        Returns:
            object | None: Instância da classe ou None se não encontrar
        """
        try:
            self._import_module()
            classes = inspect.getmembers(self.module, inspect.isclass)
            for class_name, class_obj in classes:
                if class_obj.__module__ == self.module.__name__:
                    # self._cli.console.print(f"[*] Found class: {class_name}")
                    obj_centrao = class_obj()  # Instantiate the class automatically
                    break
            if not obj_centrao:
                self._cli.console.print("[!] No suitable class found in the module")
            return obj_centrao
        except Exception as e:
            self._cli.console.print(f"[!] Error instantiating class: {e}")
            return None