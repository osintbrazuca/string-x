"""
Módulo de configuração global para String-X.

Este módulo contém todas as configurações globais utilizadas pela ferramenta String-X,
incluindo configurações de logs, banners e threads.

Variables:
    TIME (str): Timestamp atual no formato DD-MM-YYYY-HH para nomenclatura de arquivos
    LOG_DIRECTORY (str): Diretório onde serão salvos os arquivos de log
    LOG_FILE_LAST (str): Nome do arquivo que armazena o último valor processado
    LOG_FILE_OUTPUT (str): Nome do arquivo de saída com timestamp
    BANNER (AsciiBanner): Instância da classe de banners ASCII
    BANNER_DEFAULT (str): Banner padrão a ser exibido
    BANNER_RANDOM (bool): Flag para exibir banner aleatório
    BANNER_HELP (str): Banner que será exibido na ajuda
    THREAD_MAX (int): Número máximo de threads permitidas
"""
from datetime import datetime
from core.banner.asciiart import AsciiBanner

# LOGS
TIME = datetime.now().strftime("%d-%m-%Y-%H")
LOG_DIRECTORY = './output'
LOG_FILE_LAST = 'output-last-value.log'
LOG_FILE_OUTPUT = f'{LOG_DIRECTORY}/output-{TIME}.log'

# BANNERS
BANNER = AsciiBanner()
BANNER_DEFAULT = 'strx'
BANNER_RANDOM = False
BANNER_HELP = (
    BANNER.show_random() if BANNER_RANDOM is True else BANNER.show(BANNER_DEFAULT)
)

# THREADS
THREAD_MAX = 10
