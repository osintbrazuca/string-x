import time
import threading
from concurrent.futures import ThreadPoolExecutor
from core.style_cli import StyleCli


class ThreadProcess:
    def __init__(self):
        self.max_thread = 50
        self.__sleep = 0
        self.__cli = StyleCli()

    def exec_thread(self, _function_name, _command_str, _target_list, _mix):
        if _function_name and _command_str and _target_list:
            try:
                list_threads = []
                for tgt_str in _target_list:
                    if tgt_str:
                        while threading.active_count() > self.max_thread:
                            time.sleep(self.__sleep)
                        thread = threading.Thread(
                            target=_function_name, args=(
                                tgt_str, _command_str, _mix,)
                        )
                        list_threads.append(thread)
                        thread.start()
                for thread in list_threads:
                    thread.join()
            except FutureWarning:
                self.__cli.console.print_exception(max_frames=3)

    def main_pool_thread(self, _function_name, _target, _command, _exploit: list):
        return self.setting_main_pool_thread(_function_name, [_target], [_command], [_exploit])

    def setting_main_pool_thread(self, _function_name, _target, _command, _exploit: list):
        try:
            executor = ThreadPoolExecutor(max_workers=self.max_conection)
            executor.map(_function_name, _target, _command, _exploit)
            executor.shutdown(wait=True)
            executor.shutdown()
        except Exception as err:
            self.__cli.console.print_exception(max_frames=3)
