from pathlib import Path
from loguru import logger


logger.add('logs.log', format='{time} {level} {message}', level='DEBUG')

@logger.catch()
def restructurizer(d):
    f = directory
    for file in d.iterdir():
        for fragm in file.name.split('-'):
            if '.txt' in fragm:
                file.replace(f/fragm)
                f = directory
            elif not (f / fragm).exists():
                (f / fragm).mkdir()
                f = f / fragm
            else:
                f = f / fragm


directory = Path.cwd() / 'directory'
restructurizer(directory)
logger.info('Finish restructurizing')

