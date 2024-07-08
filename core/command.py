import shlex
import logging
import argparse
import subprocess
from core.format import Format
from core.func_format import FuncFormat
from core.style_cli import StyleCli

class Command:
    def __init__(self):
        self._format_func = FuncFormat()
        self._cli = StyleCli()
        self._print_func: bool = False
        self._output_func: bool = False
        self.verbose: bool = False
    
    def _shlex(self, command: str) -> list[str]:
        if command:
            return shlex.split(command)

    def _exec_command(self,command: str, pipe_command: str) -> None:
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
                    except subprocess.SubprocessError:
                        self._cli.console.print_exception(max_frames=3)
                    except FileNotFoundError:
                        pass
                    except ValueError:
                        pass
                if result_command.stdout:
                    for line_std in result_command.stdout:
                        if line_std:
                            line_std = Format.clear_value(line_std)
                            logging.info(line_std)
                            if self.verbose:
                                self._cli.console.log(line_std)
                            else:
                                self._cli.console.print(line_std)
            except subprocess.SubprocessError:
                self._cli.console.print_exception(max_frames=3)
            except FileNotFoundError:
                pass
            except ValueError:
                pass

    def _format_function(self, command:str) -> str:
        command_func: str = str()
        if command:
            command_func = self._format_func.func_format(command)
            if self._print_func:
                if self.verbose:
                    if command_func: self._cli.console.log(command_func)
                else:
                     if command_func: self._cli.console.print(command_func)
            if self._output_func and command_func: logging.info(command_func)
        return command_func

    def _command_prepare(self, target: str, command: str) -> str:
        if target and command:
            target = Format.clear_value(target)
            command_target = command.replace(r'{STRING}', target)
            command_target = self._format_function(command_target)
            if command_target:
                return command_target
        return str()

    def command_template(self, target: str, command: str, args: argparse.Namespace):
        if target and command:
            self._print_func = args.pf
            self._output_func = args.of
            try:
                command_target = self._command_prepare(target, command)
                command_pipe = self._command_prepare(target, args.pipe)
                if command: self._cli.verbose(f"[!] TEMPLATE: {command}", self.verbose)
                if command_target: self._cli.verbose(f"[!] COMMAND: {command_target}", self.verbose)
                if command_pipe: self._cli.verbose(f"[!] PIPE: {command_pipe}", self.verbose)
                return self._exec_command(command_target, command_pipe)
            except FutureWarning:
                self._cli.console.print_exception(max_frames=3)