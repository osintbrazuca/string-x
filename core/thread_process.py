import time
import threading
from concurrent.futures import ThreadPoolExecutor
from core.style_cli import StyleCli


class ThreadProcess:
    def __init__(self):
        self.max_thread = 10
        self._sleep = 0
        self._cli = StyleCli()

    def exec_thread(self, function_name, command_str, target_list, argparse):
        if function_name and command_str and target_list:
            try:
                list_threads = []
                for tgt_str in target_list:
                    if tgt_str:
                        while threading.active_count() > self.max_thread:
                            time.sleep(self._sleep)
                        thread = threading.Thread(
                            target=function_name, args=(
                                tgt_str, command_str, argparse,)
                        )
                        list_threads.append(thread)
                        thread.start()
                for thread in list_threads:
                    thread.join()
            except FutureWarning:
                self._cli.console.print_exception(max_frames=3)

    def main_pool_thread(self, function_name, target, command, exploit: list):
        return self.setting_main_pool_thread(function_name, [target], [command], [exploit])

    def setting_main_pool_thread(self, function_name, target, command, exploit: list):
        try:
            executor = ThreadPoolExecutor(max_workers=self.max_thread)
            executor.map(function_name, target, command, exploit)
            executor.shutdown(wait=True)
            executor.shutdown()
        except Exception as err:
            self._cli.console.print_exception(max_frames=3)
