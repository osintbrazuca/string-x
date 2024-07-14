import time
import shlex
import argparse
import subprocess
import logging.config
from core.format import Format
from core.func_format import FuncFormat
from core.style_cli import StyleCli
from core.filelocal import FileLocal


class Command:
    def __init__(self,):
        self._file = FileLocal()
        self._format_func = FuncFormat()
        self._cli = StyleCli()
        self._print_func: bool = False
        self._output_func: bool = False
        self._filter: str = str()
        self._sleep: int = int()
        self.file_output: str = str()
        self.file_last_output: str = str()
        self.last_value: str = str()
        self.verbose: bool = False
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

    def _set_logging(self):
        logging.basicConfig(
            format='%(message)s',
        )
        logging.config.dictConfig(self._logging_config)
        logging.getLogger()

    def _save_command_log(self, value: str) -> None:
        if value:
            self._file.save_value(f"{value}\n", self.file_output)

    def _save_last_target(self, value: str) -> None:
        if value:
            self.last_value = value
            self._file.save_last_value(f"{value}\n", file=self.file_last_output)

    @staticmethod
    def _shlex(command: str) -> list[str]:
        if command:
            return shlex.split(f"{command}")

    def _exec_command(self, command: str, pipe_command: str) -> None:
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
                            line_std = Format.clear_value(line_std)
                            if self.verbose:
                                self._cli.console.log(line_std)
                            else:
                                self._cli.console.print(line_std)
                            self._save_command_log(line_std)

            except FileNotFoundError as e:
                if not self._print_func:
                    self._cli.console.print(e)
                pass
            except ValueError:
                pass

    def _format_function(self, command: str) -> str:
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
        if target and command:
            target = Format.clear_value(target)
            self._save_last_target(target)
            self._print_func = args.pf
            self._output_func = args.of
            self._filter = args.filter
            self._sleep = args.sleep

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
