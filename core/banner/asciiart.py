import random
from core.filelocal import FileLocal
from core.style_cli import StyleCli

class AsciiBanner:
  def __init__(self):
      self._file = FileLocal()
      self.__cli = StyleCli()
      self._files_phth = './core/banner/asciiart'
  
  def _get_banner_file(self, banner_name:str):
        banners = self._get_banner_list().get('files') 
        return [ name for name in banners if banner_name in str(name) ]

  def _get_banner_list(self):
      return self._file.list_file_dir(self._files_phth)

  def show(self, banner_name:str):
      if banner_name:
        try:
            file_name = str(self._get_banner_file(banner_name)[0])
            txt_line, data_return = self._file.open_file("./"+file_name,'r')
            if txt_line:
                return ''.join(txt_line)
        except Exception:
            self.__cli.console.print_exception(max_frames=3)
      