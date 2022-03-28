import argparse
import datetime
from loguru import logger


logger.add('logs.log', format='{time} {level} {message}', level='DEBUG')
parser = argparse.ArgumentParser()
parser.add_argument('newyear', type=str, help='Show days quantity from current to NY')
parser.add_argument('--hours', action='store_true', help='Add hours parametr')
args = parser.parse_args()



today = datetime.datetime.today()
NY = datetime.datetime(2023, 1, 1, 00, 00, 00)
delta = NY - today

if args.hours is False:
    print(delta.days, 'days')
elif args.hours is True:
    print(f'{delta.days} days, {delta.seconds // 3600} hours')

logger.info('Time to NY is counted')