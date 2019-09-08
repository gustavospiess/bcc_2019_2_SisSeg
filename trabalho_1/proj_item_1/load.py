import pickle
import click
import logging
import sys
import os # for creating the vulnerability 


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

    logging.debug('Unpickling file "%s"' % (file_path))
    try:
        with open(file_path, 'rb') as file_buf:
            while True:
                # Exists when an Exception (EOFError)
                data = pickle.load(file_buf)
                logging.info('Unpickled "%s"' % (str(data)))
                if callable(data):
                    logging.info('Executing it')
                    data()
    except EOFError:
        logging.debug('End of file')
        logging.debug(sys.exc_info()[1])
    except Exception:
        logging.error('Error unpickling')
        logging.debug(sys.exc_info()[1])

    logging.info('process concluded')


if __name__ == '__main__':
    load()
