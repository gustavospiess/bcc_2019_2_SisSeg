import json
import click
import logging
import sys
import datetime
import os

def base(debug, info):
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    elif info:
        logging.basicConfig(level=logging.INFO)

@click.command()
@click.option('--file', '-f', 'file_path', help='file to be created', prompt='file')
@click.option('--content', '-c', 'content', help='content to be saved (must be evaluateble)', prompt='content')
@click.option('--debug', '-d', 'debug', help='debugging info will be printed', default=False, is_flag=True)
@click.option('--info', '-i', 'info', help='general info will be printed', default=False, is_flag=True)
def create(file_path, content, debug, info):
    base(debug, info)
    logging.debug('Debug mode is on, debug info is going to be printed')
    logging.debug('parameters: "%s", "%s"' % (file_path, content))

    logging.info('Info mode is on, general info is going to be printed')
    logging.info('process started')

    logging.debug('Evaluating expression "%s"' % (content))
    evaluated = eval(content)
    logging.debug('Evaluated value: "%s"' % (evaluated))

    logging.debug('Writing to JSON file "%s"' % (file_path))

    previous = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file_buf:
            previous = json.load(file_buf)['data']

    try:
        with open(file_path, 'w') as file_buf:
            data = {'data': [*previous, {'date': repr(datetime.datetime.now()), 'info': evaluated}]}
            json.dump(data, file_buf)
            logging.debug('Writing JSON was successful')
    except Exception:
        logging.error('Error writing JSON')
        logging.debug(sys.exc_info()[1])

    logging.info('process concluded')


if __name__ == '__main__':
    create()
