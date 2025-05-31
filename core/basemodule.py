"""
Módulo base para criação de módulos auxiliares.

Este módulo contém a classe BaseModule que serve como classe base para todos
os módulos auxiliares do sistema String-X. Define a interface comum e estrutura
básica que todos os módulos devem seguir.
"""

class BaseModule:
    """
    Classe base para criação de módulos com funcionalidades específicas.
    
    Cada módulo deve herdar desta classe e implementar o método `run`.
    Fornece estrutura comum para armazenamento de resultados, opções
    e metadados do módulo.
    
    Attributes:
        _result (dict): Dicionário para armazenar resultados, inicializado 
                       com o nome da classe como chave
        options (dict): Dicionário para definir opções específicas do módulo
        meta (dict): Dicionário para armazenar meta-informações sobre o módulo
    
    Methods:
        set_result(value: str): Adiciona um resultado ao dicionário _result
        get_result(): Retorna a lista de resultados armazenados
        _get_cls_name(): Retorna o nome da classe
        run(**kwargs): Método abstrato que deve ser implementado pelas subclasses
    """
    def __init__(self):
        """
        Inicializa a classe BaseModule.
        
        Configura estruturas básicas para resultados, opções e metadados
        que serão utilizadas pelos módulos filhos.
        """
        self._result = {f"{self._get_cls_name()}": []}

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

    def set_result(self, value: str):
        """
        Adiciona um resultado à lista de resultados do módulo.
        
        Args:
            value (str): Valor a ser adicionado aos resultados
        """
        if value:
            self._result.get(self._get_cls_name()).append(value)

    def get_result(self):
        """
        Retorna a lista de resultados armazenados no módulo.
        
        Returns:
            list: Lista contendo todos os resultados encontrados pelo módulo
        """
        return list(self._result.values())[0]

    def _get_cls_name(self):
        """
        Retorna o nome da classe atual.
        
        Returns:
            str: Nome da classe que herda de BaseModule
        """
        return self.__class__.__name__
        
    def run(self, **kwargs):
        """
        Método abstrato que define o comportamento do módulo.
        
        Este método deve ser implementado por todas as subclasses para
        definir a funcionalidade específica do módulo.
        
        Args:
            **kwargs: Argumentos específicos do módulo
            
        Raises:
            NotImplementedError: Se a subclasse não implementar este método
        """
        raise NotImplementedError("Subclasses devem implementar o método run()")