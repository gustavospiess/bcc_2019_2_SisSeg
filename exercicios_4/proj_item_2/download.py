import click
import os
import logging

from base import *


@click.command()
@click.option('--file', '-f', 'file_path', help='path to search for the file', prompt='file')
@click.option('--user', '-u', 'user_name', help='user that are using the program', prompt='user')
@click.option('--debug', '-d', 'debug', help='debuging info will be printed', default=False, is_flag=True)
def download(file_path, user_name, debug):
    validate_bases(debug)
    user_map = load_users(user_name)

    path = os.path.join(user_map[user_name], file_path)

    if not os.path.exists(path):
        logging.error('file does not exists')
        return

    logging.info('reading %s/%s' % (user_name, file_path))

    logging.debug('path: %s' % path)
    cmd = 'less %s' % (path)
    logging.debug('command to run: %s' % cmd)
    try:
        os.system(cmd)
    except e:
        loggin.error('unexpecte error')
        loggin.debug(e)


if __name__ == '__main__':
    download()
