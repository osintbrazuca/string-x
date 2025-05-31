import importlib
import inspect
from core.style_cli import StyleCli

class AutoModulo:
    """
    This class is used to automatically import a module and instantiate its class.
    It uses the module name and class name to dynamically load the module and create an instance of the class.
    """
    def __init__(self, type_module_name_module: str):
        self._cli = StyleCli()
        self._valid_type_module = self._check_type_module_name_module(type_module_name_module)

    def _check_type_module_name_module(self,type_module_name_module: str) -> bool:
        """
        Check if the type_module and name_module are valid.
        The type_module should be a valid module type (e.g., "extractor", "scanner", etc.)
        and the name_module should be a valid module name (e.g., "email", "domain", etc.).
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
        Load the module and instantiate the class defined in it.
        The module is expected to be in the format utils.auxiliary.{type_module}.{name_module}.
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
        try:
            self.module = importlib.import_module(f"utils.auxiliary.{self.type_module}.{self.name_module}")
            # self._cli.console.print(f"[*] Executando módulo: {self.module.__name__}")
        except ImportError as e:
            self._cli.console.print(f"[!] ImportError: {e}")
            raise e

    def _instantiate_class(self):
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