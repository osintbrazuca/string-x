"""
Módulo de banners ASCII.

Este módulo contém a classe AsciiBanner responsável por carregar e exibir
banners ASCII armazenados em arquivos, incluindo seleção aleatória de banners.
"""
import random
from core.filelocal import FileLocal
from core.style_cli import StyleCli


class AsciiBanner:
    """
    Classe para gerenciamento de banners ASCII.
    
    Esta classe permite carregar banners ASCII de arquivos e exibi-los
    no terminal, incluindo funcionalidade de seleção aleatória.
    
    Attributes:
        _file (FileLocal): Instância para manipulação de arquivos
        _cli (StyleCli): Instância para interface CLI estilizada
        _files_path (str): Caminho para diretório dos banners
    """
    def __init__(self):
        """
        Inicializa AsciiBanner com configurações padrão.
        """
        self._file = FileLocal()
        self._cli = StyleCli()
        self._files_path = './core/banner/asciiart'

    def _get_banner_file(self, banner_name: str):
        """
        Busca arquivo de banner por nome.
        
        Args:
            banner_name (str): Nome do banner a ser buscado
            
        Returns:
            list: Lista de arquivos que correspondem ao nome
        """
        banners = self._get_banner_list().get('files')
        return [name for name in banners if banner_name in str(name)]

    def _get_banner_list(self):
        """
        Obtém lista de arquivos de banner disponíveis.
        
        Returns:
            dict: Dicionário com lista de arquivos de banner
        """
        return self._file.list_file_dir(self._files_path)

    def show(self, banner_name: str):
        """
        Exibe um banner específico.
        
        Args:
            banner_name (str): Nome do banner a ser exibido
            
        Returns:
            str: Conteúdo do banner ou None se não encontrado
        """
        if banner_name:
            try:
                file_name = str(self._get_banner_file(banner_name)[0])
                txt_line, data_return = self._file.open_file("./" + file_name, 'r')
                if txt_line:
                    return ''.join(txt_line)
            except Exception:
                self._cli.console.print_exception(max_frames=3)

    def show_random(self):
        """
        Exibe um banner selecionado aleatoriamente.
        
        Returns:
            str: Conteúdo do banner aleatório
        """
        banner_list = self._get_banner_list()
        random.shuffle(banner_list.get('files'))
        banner_file_name = banner_list.get('files')[0].stem
        return self.show(banner_file_name)

