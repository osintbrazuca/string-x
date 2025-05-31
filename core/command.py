"""
Módulo responsável pela execução de comandos e manipulação de templates.

Este módulo contém a classe Command que é responsável por processar templates de comandos,
executar os comandos no sistema operacional e gerenciar a saída dos resultados.
"""
import time
import shlex
import argparse
import subprocess
import logging.config
from core.format import Format
from core.func_format import FuncFormat
from core.style_cli import StyleCli
from core.filelocal import FileLocal
from core.auto_module import AutoModulo

class Command:
    """
    Classe responsável pela execução de comandos e processamento de templates.
    
    Esta classe gerencia a execução de comandos baseados em templates, processamento
    de funções customizadas, módulos automáticos e gerenciamento de logs.
    
    Attributes:
        _file (FileLocal): Instância para manipulação de arquivos
        _format_func (FuncFormat): Instância para formatação de funções
        _cli (StyleCli): Instância para interface CLI estilizada
        _print_func (bool): Flag para imprimir resultados de funções
        _output_func (bool): Flag para salvar resultados de funções
        _print_result_module (bool): Flag para imprimir apenas resultados de módulos
        _filter (str): Filtro para strings de entrada
        _sleep (int): Tempo de delay entre execuções
        file_output (str): Caminho do arquivo de saída
        file_last_output (str): Caminho do arquivo do último valor
        last_value (str): Último valor processado
        verbose (bool): Flag para modo verboso
        _type_module (str): Tipo de módulo a ser executado
    """
    def __init__(self,):
        """
        Inicializa a classe Command com configurações padrão.
        
        Configura todas as variáveis necessárias e inicializa o sistema de logging.
        """
        self._file = FileLocal()
        self._format_func = FuncFormat()
        self._cli = StyleCli()
        self._print_func: bool = False
        self._output_func: bool = False
        self._print_result_module: bool = False
        self._filter: str = str()
        self._sleep: int = int()
        self.file_output: str = str()
        self.file_last_output: str = str()
        self.last_value: str = str()
        self.verbose: bool = False
        self._type_module: str = str()
        
        self._logging_config = {
            "version": 1,
            "handlers": {
                "default": {
                    "class": "logging.StreamHandler",
                    "formatter": "http",
                    "stream": "ext://sys.stderr"
                }
            },
            "formatters": {
                "http": {
                    "format": "%(levelname)s [%(asctime)s] %(name)s - %(message)s",
                    "datefmt": "%Y-%m-%d %H:%M",
                }
            },
            'loggers': {
                'httpx': {
                    'handlers': ['default'],
                    'level': 'CRITICAL',
                },
                'httpcore': {
                    'handlers': ['default'],
                    'level': 'CRITICAL',
                },
            }
        }
        self._set_logging()

    def _set_logging(self) -> None:
        """
        Configura o sistema de logging da aplicação.
        
        Estabelece as configurações de logging para a aplicação e bibliotecas externas,
        definindo níveis críticos para httpx e httpcore para reduzir verbosidade.
        """
        logging.basicConfig(
            format='%(message)s',
        )
        logging.config.dictConfig(self._logging_config)
        logging.getLogger()

    def _save_command_log(self, value: str) -> None:
        """
        Salva o resultado de um comando no arquivo de log.
        
        Args:
            value (str): Valor a ser salvo no arquivo de log
        """
        if value:
            self._file.save_value(f"{value}\n", self.file_output)

    def _save_last_target(self, value: str) -> None:
        """
        Salva o último valor processado em arquivo específico.
        
        Args:
            value (str): Último valor processado
        """
        if value:
            self.last_value = value
            self._file.save_last_value(f"{value}\n", file=self.file_last_output)

    @staticmethod
    def _shlex(command: str) -> list[str]:
        """
        Converte uma string de comando em lista usando shlex.
        
        Args:
            command (str): Comando a ser convertido
            
        Returns:
            list[str]: Lista com os argumentos do comando
        """
        if command:
            return shlex.split(f"{command}")

    def _exec_module(self, _type_module: str, data: str) -> AutoModulo | None:
        """
        Executa um módulo automático com os dados fornecidos.
        
        Args:
            _type_module (str): Tipo do módulo no formato 'tipo:nome'
            data (str): Dados a serem processados pelo módulo
            
        Returns:
            AutoModulo | None: Instância do módulo executado ou None se houver erro
        """
        if not _type_module or ":" not in _type_module or data is None:
            return None
        auto_load = AutoModulo(_type_module)
        if obj_module := auto_load.load_module():
            obj_module.options.update({"data": data})
            obj_module.run()
            return obj_module
        return None

    def _exec_command(self, command: str, pipe_command: str) -> None:
        """
        Executa um comando no sistema operacional com suporte a pipes.
        
        Args:
            command (str): Comando principal a ser executado
            pipe_command (str): Comando de pipe opcional
        """
        if command:
            try:
                result_command = subprocess.Popen(
                    self._shlex(command),
                    stdout=subprocess.PIPE,
                    encoding='utf-8'
                )
                if pipe_command:
                    try:
                        result_command = subprocess.Popen(
                            self._shlex(pipe_command),
                            stdin=result_command.stdout,
                            stdout=subprocess.PIPE,
                            encoding='utf-8'
                        )
                    except FileNotFoundError as e:
                        if not self._print_func:
                            self._cli.console.print(e)
                    except ValueError:
                        pass

                if result_command.stdout:
                    for line_std in result_command.stdout:
                        if line_std:
                            if not self._print_result_module:
                                line_std = Format.clear_value(line_std)
                                self._print_line_std(line_std)
                            if object_module := self._exec_module(self._type_module, line_std):
                                if result_module := object_module.get_result():
                                    result_module = "\n".join(result_module)
                                    self._print_line_std(result_module)

            except FileNotFoundError as e:
                if not self._print_func:
                    self._cli.console.print(e)
                pass
            except ValueError:
                pass

    def _print_line_std(self, line_std) -> None:
        """
        Imprime uma linha de saída padrão e salva no log.
        
        Args:
            line_std: Linha a ser impressa e salva
        """
        if line_std:
            if self.verbose:
                self._cli.console.log(line_std)
            else:
                self._cli.console.print(line_std)
            self._save_command_log(line_std)

    def _format_function(self, command: str) -> str:
        """
        Aplica formatação de funções customizadas em um comando.
        
        Args:
            command (str): Comando a ser formatado
            
        Returns:
            str: Comando formatado com funções processadas
        """
        command_func: str = str()
        try:
            if command:
                command_func = self._format_func.func_format(command)
                if self._print_func:
                    if self.verbose:
                        if command_func: self._cli.console.log(command_func)
                    else:
                        if command_func: self._cli.console.print(command_func)
                if self._output_func and command_func:
                    self._save_command_log(command_func)
            return command_func
        except Exception:
            pass

    def _command_prepare(self, target: str, command: str) -> str:
        """
        Prepara um comando substituindo placeholders e aplicando formatações.
        
        Args:
            target (str): Valor alvo a ser substituído no placeholder {STRING}
            command (str): Template do comando
            
        Returns:
            str: Comando preparado para execução
        """
        try:
            if target and command:
                command_target = command.replace(r'{STRING}', target)
                command_target = self._format_function(command_target)
                if command_target:
                    return command_target
            return str()
        except Exception:
            pass

    def command_template(self, target: str, command: str, args: argparse.Namespace):
        """
        Processa um template de comando com um valor alvo específico.
        
        Este é o método principal que coordena todo o processamento de um comando,
        incluindo filtros, delays, verbose mode e execução de pipes.
        
        Args:
            target (str): Valor alvo para substituição no template
            command (str): Template do comando a ser executado
            args (argparse.Namespace): Argumentos da linha de comando
        """
        if target and command:
            target = Format.clear_value(target)
            self._save_last_target(target)
            self._print_func = args.pf
            self._output_func = args.of
            self._filter = args.filter
            self._sleep = args.sleep
            self._type_module = args.module
            self._print_result_module = args.pm

            if self._sleep: time.sleep(int(self._sleep))

            if self._filter:
                if self._filter not in target:
                    return self._cli.verbose(f"[X] IF VALUE: {target}", self.verbose)
                elif self._filter in target:
                    self._cli.verbose(f"[!] IF VALUE: {target}", self.verbose)

            try:
                command_target = self._command_prepare(target, command)
                command_pipe = self._command_prepare(target, args.pipe)
                if command: self._cli.verbose(f"[!] TEMPLATE: {command}", self.verbose)
                if command_target: self._cli.verbose(f"[!] COMMAND: {command_target}", self.verbose)
                if command_pipe: self._cli.verbose(f"[!] PIPE: {command_pipe}", self.verbose)
                return self._exec_command(command_target, command_pipe)
            except Exception:
                pass
