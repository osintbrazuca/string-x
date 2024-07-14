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
