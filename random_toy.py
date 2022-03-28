import click
import enum
import random
from loguru import logger


class Colors(enum.Enum):
    red = 'red'
    green = 'green'
    blue = 'blue'
    yellow = 'yellow'

class Toys(enum.Enum):
    ball = 'ball'
    angel = 'angel'
    doll = 'doll'
    tree = 'tree'

@click.command()
@click.argument('toy')
def random_toy(toy):
    '''Print random toy'''
    if toy == 'toy':
        print(random.choice(colors), random.choice(toys), sep=' ')
        logger.info('Random toy is finding')

colors = [i.value for i in Colors]
toys = [i.value for i in Toys]
logger.add('logs.log', format='{time} {level} {message}', level='DEBUG')


if __name__ == '__main__':
    random_toy()

