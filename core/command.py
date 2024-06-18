import shlex
import subprocess
from core.thread_process import ThreadProcess
from core.format import Format

class Command:
    def __init__(self):
        ...
    

    def command_prepare(target_str: str, command_str:str) -> str:
        if target_str and command_str:
            target_str = Format.clear_value(target_str)
            command_target_str = command_str.replace(r'{STRING}', target_str)
            return command_target_str
