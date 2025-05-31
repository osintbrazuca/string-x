"""
Módulo responsável pela manipulação de arquivos locais.

Este módulo contém classes para operações de arquivo, incluindo leitura, escrita,
manipulação de CSV e navegação em diretórios, além de configurações INI.
"""
import csv
import pathlib
import configparser
from core.style_cli import StyleCli


class FileLocal:
    """
    Classe responsável por operações de arquivo local.
    
    Esta classe fornece métodos para abrir, ler, escrever arquivos de texto,
    manipular arquivos CSV e navegar em estruturas de diretórios.
    
    Attributes:
        _cli (StyleCli): Instância para interface CLI estilizada
    """
    def __init__(self):
        """
        Inicializa a classe FileLocal.
        """
        self._cli = StyleCli()

    def open_file(self, filename: str, mode: str):
        """
        Abre um arquivo e retorna suas linhas e handle.
        
        Args:
            filename (str): Caminho para o arquivo
            mode (str): Modo de abertura do arquivo ('r', 'w', 'a', etc.)
            
        Returns:
            tuple: Tupla contendo (linhas_do_arquivo, handle_do_arquivo)
        """
        if filename and mode:
            try:
                data_return = open(filename, mode, encoding="utf8")
                txt_line = (data_return.readlines())
                return txt_line, data_return
            except FileNotFoundError:
                self._cli.console.print_exception(max_frames=3)
            except PermissionError:
                self._cli.console.print_exception(max_frames=3)
            except Exception:
                self._cli.console.print_exception(max_frames=3)

    def save_value(self, value: str, file: str, mode: str = 'a+'):
        """
        Salva um valor em um arquivo.
        
        Args:
            value (str): Valor a ser salvo
            file (str): Caminho do arquivo de destino
            mode (str, optional): Modo de abertura. Defaults to 'a+'.
        """
        if value and file:
            try:
                with open(file, mode) as data_return:
                    data_return.writelines(value)
            except Exception:
                self._cli.console.print_exception(max_frames=3)

    def save_last_value(self, value: str, file: str):
        """
        Salva o último valor processado sobrescrevendo o arquivo.
        
        Args:
            value (str): Valor a ser salvo
            file (str): Caminho do arquivo de destino
        """
        if value and file:
            try:
                data_return = open(file, 'w')
                data_return.write(value)
                data_return.close()
            except Exception:
                self._cli.console.print_exception(max_frames=3)

    def open_file_csv(self, filename: str, mode: str):
        """
        Abre um arquivo CSV e retorna reader configurado.
        
        Args:
            filename (str): Caminho para o arquivo CSV
            mode (str): Modo de abertura do arquivo
            
        Returns:
            tuple: Tupla contendo (handle_do_arquivo, csv_reader)
        """
        if filename and mode:
            try:
                data_file = open(filename, mode)
                data_return = csv.DictReader(data_file)
                csv_line = data_file
                return csv_line, data_return
            except IOError:
                self._cli.console.print_exception(max_frames=3)

    def list_file_dir(self, dir_str: str) -> dict[list[str], list[str] | str]:
        """
        Lista arquivos e diretórios recursivamente em um diretório.
        
        Args:
            dir_str (str): Caminho do diretório a ser listado
            
        Returns:
            dict: Dicionário com chaves 'dirs' e 'files' contendo listas de caminhos
        """
        dir_list: list = []
        file_list: list = []
        skipe_list: list = ["etc", "bin", "home"]
        if dir_str:
            try:
                obj_path = pathlib.Path(dir_str)
                path_tree_list = list(obj_path.rglob("*"))
                for dir_file in path_tree_list:
                    if set(dir_file.parts).isdisjoint(skipe_list):
                        if dir_file.is_dir():
                            dir_list.append(dir_file)
                        elif dir_file.is_file():
                            file_list.append(dir_file)
                return {'dirs': dir_list, 'files': file_list}
            except Exception:
                self._cli.console.print_exception(max_frames=3)


class AttrDict(dict):
    """
    Dicionário que permite acesso aos atributos via notação de ponto.
    
    Esta classe estende dict para permitir acesso aos valores usando
    notação de atributo (obj.key) além da notação de dicionário (obj['key']).
    """
    def __init__(self, *args, **kwargs):
        """
        Inicializa AttrDict com os mesmos parâmetros de dict.
        """
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Configs:
    """
    Classe responsável pelo gerenciamento de arquivos de configuração INI.
    
    Esta classe fornece métodos para ler e processar arquivos de configuração
    no formato INI, retornando as configurações como dicionários.
    
    Attributes:
        _config (configparser.ConfigParser): Parser de configuração
        _path (str): Caminho para o diretório de configurações
        file (str): Nome do arquivo de configuração
    """

    def __init__(self):
        """
        Inicializa a classe Configs com configurações padrão.
        """
        self._config = configparser.ConfigParser(dict_type=AttrDict)
        self._path = 'config'
        self.file = 'default.ini'

    def open_config(self) -> dict[str]:
        """
        Abre e processa o arquivo de configuração.
        
        Returns:
            dict[str]: Dicionário com as configurações da seção 'general'
        """
        try:
            self._config.read(f'./{self._path}/{self.file}')
            if self._config._sections.general:
                return self._config._sections.general
        except Exception as e:
            print(e)
