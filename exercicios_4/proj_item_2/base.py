import os
import logging
import csv
import hashlib


default_csv_param = {'delimiter': ',', 'quotechar': '"'}


def load_users(user_name):
    logging.debug('reading users')
    user_map = dict()
    with open('users.csv', newline='') as users_file:
        user_reader = csv.reader(users_file, **default_csv_param)
        for user in user_reader:
            user_map[user[0]] = user[1]

    logging.debug(user_map)

    if user_name not in user_map:
        logging.debug('%s does not exists' % user_name)
        sha = add_user(user_name)
        user_map[user_name] = sha

    return user_map


def add_user(user_name):
    logging.debug('writing users')
    with open('users.csv', 'a', newline='') as users_file:
        user_writer = csv.writer(users_file, **default_csv_param)
        sha = hashlib.sha256(user_name.encode('utf-8')).hexdigest()
        user = (user_name, sha,)
        user_writer.writerow(user)

        logging.debug('added')
        create_user_folder(sha)

        return sha


def create_user_folder(user_id):
    logging.debug('creating folder for %s' % user_id)
    os.mkdir(user_id)
    logging.debug('created folder')


def validate_bases(debug):
    if not os.path.exists('users.csv'):
        open('users.csv', 'w+').close()

    if debug:
        logging.basicConfig(level=logging.DEBUG)

