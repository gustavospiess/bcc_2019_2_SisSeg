import pickle
import click
import logging
import sys
import datetime

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

    logging.debug('Pickling to file "%s"' % (file_path))
    try:
        with open(file_path, 'ab') as file_buf:
            pickle.dump(datetime.datetime.now(), file_buf)
            pickle.dump(evaluated, file_buf)
            logging.debug('Pickling was successful')
    except Exception:
        logging.error('Error pickling')
        logging.debug(sys.exc_info()[1])

    logging.info('process concluded')


if __name__ == '__main__':
    create()
