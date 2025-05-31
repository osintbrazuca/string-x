class BaseModule:
    """
    BaseModule is a base class for creating modules with specific functionalities. 
    Each module should inherit from this class and implement the `run` method.
    Attributes:
        _result (dict): A dictionary to store results, initialized with the class name as the key.
        options (dict): A dictionary to define module-specific options.
        meta (dict): A dictionary to store meta-information about the module.
    Methods:
        set_result(value: str):
            Adds a result to the _result dictionary under the class name key.
        get_result():
            Returns the list of results stored in the _result dictionary.
        _get_cls_name():
            Returns the name of the class.
        run(**kwargs):
            Abstract method that should be implemented by subclasses to define the module's behavior.
    """
    def __init__(self):

        self._result = {f"{self._get_cls_name()}" : []}

        # Cada módulo deverá definir suas opções (chave: dict com required, description, value)
        self.options = {
            "data": None
        }

        # Meta-informações do módulo
        self.meta = {
            "name": None, 
            "description": None, 
            "author": None,
            "version": 1.0,
            "type": None
        }

    def set_result(self, value:str):
         if value:
            self._result.get(self._get_cls_name()).append(value)

    def get_result(self):
        return list(self._result.values())[0]

    def _get_cls_name(self):
        return self.__class__.__name__
        
    def run(self, **kwargs):
        raise NotImplementedError("Subclasses devem implementar o método run()")