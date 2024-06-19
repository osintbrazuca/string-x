import shlex
import logging
import subprocess
from core.format import Format
from core.style_cli import StyleCli

class Command:
    def __init__(self):
        self.__cli = StyleCli()
        self.pipe: str = str
        self.verbose: bool = False
    
    def exec_command(self,command_str: str) -> None:
        if command_str:
            try:
                cmd_shlex = shlex.split(f'{command_str}')
                rest_spn = subprocess.Popen(
                    cmd_shlex,
                    stdout=subprocess.PIPE,
                    encoding='utf-8'
                )
                if self.pipe:
                    try:
                        cmd_shlex_pipe = shlex.split(self.pipe)
                        rest_spn = subprocess.Popen(
                            cmd_shlex_pipe,
                            stdin=rest_spn.stdout,
                            stdout=subprocess.PIPE,
                            encoding='utf-8'
                        )
                        self.__cli.verbose(f"[!] PIPE: {self.pipe}", self.verbose)
                    except subprocess.SubprocessError:
                        self.__cli.console.print_exception(max_frames=3)
                if rest_spn.stdout:
                    for line_std in rest_spn.stdout:
                        if line_std:
                            line_std = Format.clear_value(line_std)
                            logging.info(line_std)
                            (self.__cli.console.log(line_std) if self.verbose else self.__cli.console.print(line_std))
            except subprocess.SubprocessError:
                self.__cli.console.print_exception(max_frames=3)

    def command_prepare(self, target_str: str, command_str:str) -> str:
        if target_str and command_str:
            target_str = Format.clear_value(target_str)
            command_target_str = command_str.replace(r'{STRING}', target_str)
            return command_target_str
        
    def command_template(self, target_str: str, command_str: str, _mix):
        if target_str and command_str:
            try:
                command_target_str = self.command_prepare(target_str, command_str)
                self.__cli.verbose(f"[!] TEMPLATE: {command_str}", self.verbose)
                self.__cli.verbose(f"[!] COMMAND: {command_target_str}", self.verbose)
                return self.exec_command(command_target_str)
            except FutureWarning:
                self.__cli.console.print_exception(max_frames=3)