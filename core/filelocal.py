import csv
from core.style_console import StyleConsole


class FileLocal:
    def __init__(self):
        self.__style_cli = StyleConsole()

    def open_file(self, filename: str, mode: str):
        if filename and mode:
            try:
                data_return = open(filename, mode, encoding="utf8")
                txt_line = (data_return.readlines())
                return txt_line, data_return
            except FileNotFoundError:
                self.__style_cli.console.print_exception(max_frames=3)
            except PermissionError:
                self.__style_cli.console.print_exception(max_frames=3)
            finally:
                data_return.close()

    def save_value(self, value: str, file: str):
        if value and file:
            try:
                txt_line, data_return = self.open_file(file, 'a+')
                data_return.writelines(value)
                data_return.close()
            except IOError:
                self.__style_cli.console.print_exception(max_frames=3)

    @staticmethod
    def open_fileCsv(filename: str, mode: str):
        if filename and mode:
            try:
                data_file = open(filename, mode)
                data_return = csv.DictReader(data_file)
                csv_line = data_file
                return csv_line, data_return
            except IOError:
                self.__style_cli.console.print_exception(max_frames=3)