import os
import logging
import csv


default_csv_param = {'delimiter': ',', 'quotechar': '"'}


def load_users(user_name):
    logging.debug('reading users')
    user_set = set()
    with open('users.csv', newline='') as users_file:
        user_reader = csv.reader(users_file, **default_csv_param)
        for user in user_reader:
            user_set.add(user[0])

    logging.debug(user_set)

    if user_name not in user_set:
        logging.debug('%s does not exists' % user_name)
        add_user(user_name)
        user_set.add(user_name)

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


def validate_bases(debug):
    if not os.path.exists('users.csv'):
        open('users.csv', 'w+').close()

    if debug:
        logging.basicConfig(level=logging.DEBUG)

