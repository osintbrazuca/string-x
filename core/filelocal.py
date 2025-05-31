import csv
import pathlib
import configparser
from core.style_cli import StyleCli


class FileLocal:
    def __init__(self):
        self._cli = StyleCli()

    def open_file(self, filename: str, mode: str):
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
        if value and file:
            try:
                with open(file, mode) as data_return:
                    data_return.writelines(value)
            except Exception:
                self._cli.console.print_exception(max_frames=3)

    def save_last_value(self, value: str, file: str):
        if value and file:
            try:
                data_return = open(file, 'w')
                data_return.write(value)
                data_return.close()
            except Exception:
                self._cli.console.print_exception(max_frames=3)

    def open_file_csv(self, filename: str, mode: str):
        if filename and mode:
            try:
                data_file = open(filename, mode)
                data_return = csv.DictReader(data_file)
                csv_line = data_file
                return csv_line, data_return
            except IOError:
                self._cli.console.print_exception(max_frames=3)

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
                self._cli.console.print_exception(max_frames=3)


class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self


class Configs:

    def __init__(self):
        self._config = configparser.ConfigParser(dict_type=AttrDict)
        self._path = 'config'
        self.file = 'default.ini'

    def open_config(self) -> dict[str]:
        try:
            self._config.read(f'./{self._path}/{self.file}')
            if self._config._sections.general:
                return self._config._sections.general
        except Exception as e:
            print(e)
