import json
import click
import logging
import sys
import os # for creating the vulnerability 
import datetime


def base(debug, info):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    elif info:
        logging.basicConfig(level=logging.INFO)


@click.command()
@click.option('--file', '-f', 'file_path', help='file to be loaded', prompt='file')
@click.option('--debug', '-d', 'debug', help='debugging info will be printed', default=False, is_flag=True)
@click.option('--info', '-i', 'info', help='general info will be printed', default=False, is_flag=True)
def load(file_path, debug, info):
    base(debug, info)
    logging.debug('Debug mode is on, debug info is going to be printed')
    logging.debug('parameters: "%s"' % (file_path,))

    logging.info('Info mode is on, general info is going to be printed')
    logging.info('process started')

    logging.debug('Reading JSON file "%s"' % (file_path))
    try:
        with open(file_path, 'r') as file_buf:
            data = json.load(file_buf)['data']
            logging.info('read "%s"' % (str(data)))
            for sub in data:
                info = sub['info']
                date = eval(sub['date'])
                logging.info('date "%s"' % (str(date)))
                logging.info('processing "%s"' % (str(info)))
                if callable(info):
                    logging.info('Executing it')
                    info()
    except Exception:
        logging.error('Error reading JSON')
        logging.debug(sys.exc_info()[0])
        logging.debug(sys.exc_info()[1])

    logging.info('process concluded')


if __name__ == '__main__':
    load()
