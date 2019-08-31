import click
import os
import logging
import csv


default_csv_param = {'delimiter': ',', 'quotechar': '"'}


@click.command()
@click.option('--file', '-f', 'file_path', help='path to save the file', prompt='file')
@click.option('--content', '-c', 'content', help='content to be saved', prompt='content')
@click.option('--user', '-u', 'user_name', help='user that are using the program', prompt='user')
@click.option('--debug', '-d', 'debug', help='debuging info will be printed', default=False, is_flag=True)
def upload(file_path, content, user_name, debug):
    if debug:
        logging.basicConfig(level=logging.DEBUG)

    validate_bases()

    user_set = load_users()
    if user_name not in user_set:
        add_user(user_name)
        user_set.add(user_name)

    path = os.path.join(user_name, file_path)
    logging.debug('path: %s' % path)
    cmd = 'echo %s > %s' % (content, path)
    logging.debug('command to run: %s' % cmd)
    os.system(cmd)


def load_users():
    logging.debug('reading users')
    user_set = set()
    with open('users.csv', newline='') as users_file:
        user_reader = csv.reader(users_file, **default_csv_param)
        for user in user_reader:
            user_set.add(user[0])

    logging.debug(user_set)
    return user_set


def add_user(user_name):
    logging.debug('writing users')
    with open('users.csv', 'a', newline='') as users_file:
        user_writer = csv.writer(users_file, **default_csv_param)
        user = (user_name,)
        user_writer.writerow(user)

    logging.debug('added')
    create_user_folder(user_name)


def create_user_folder(user_name):
    logging.debug('creating folder for %s' % user_name)
    os.mkdir(user_name)
    logging.debug('created folder')


def validate_bases():
    if not os.path.exists('users.csv'):
        open('users.csv', 'w+').close()


if __name__ == '__main__':
    upload()
