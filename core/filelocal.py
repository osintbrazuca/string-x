import csv
import pathlib
from core.style_cli import StyleCli


class FileLocal:
    def __init__(self):
        self.__cli = StyleCli()
        self.file_skipe = None

    def open_file(self, filename: str, mode: str):
        if filename and mode:
            try:
                data_return = open(filename, mode, encoding="utf8")
                txt_line = (data_return.readlines())
                return txt_line, data_return
            except FileNotFoundError:
                self.__cli.console.print_exception(max_frames=3)
            except PermissionError:
                self.__cli.console.print_exception(max_frames=3)
            except Exception:
                self.__cli.console.print_exception(max_frames=3)
            finally:
                data_return.close()

    def save_value(self, value: str, file: str):
        if value and file:
            try:
                _, data_return = self.open_file(file, 'a+')
                data_return.writelines(value)
                data_return.close()
            except IOError:
                self.__cli.console.print_exception(max_frames=3)

    def open_file_csv(self, filename: str, mode: str):
        if filename and mode:
            try:
                # TODO
                # Refazer função
                _, data_file = self.open_file(filename, mode)
                data_return = csv.DictReader(data_file)
                csv_line = data_file
                return csv_line, data_return
            except IOError:
                self.__cli.console.print_exception(max_frames=3)

    def list_file_dir(self, dir_str: str) -> dict[list[str], list[str] | str]:
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
                self.__cli.console.print_exception(max_frames=3)
