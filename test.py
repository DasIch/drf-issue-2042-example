import os
import sys
import time
import errno
from subprocess import Popen, call
from contextlib import contextmanager

import django
import requests


MANAGE_FILE = os.path.join(os.path.dirname(__file__), 'manage.py')


def test():
    s = requests.session()
    response = s.post('http://localhost:8000/a', json={})
    assert response.status_code == 201, response.status_code
    id = response.json()['id']

    response = s.post('http://localhost:8000/b', json={'a': id})
    assert response.status_code == 201, response.status_code


def remove_database():
    database_file = os.path.join(os.path.dirname(__file__), 'db.sqlite3')
    try:
        os.remove(database_file)
    except EnvironmentError as error:
        if error.errno != errno.ENOENT: # file not found
            raise


def init_database():
    if django.VERSION >= (1, 7):
        call([sys.executable, MANAGE_FILE, 'migrate'])
    else:
        call([sys.executable, MANAGE_FILE, 'syncdb'])


@contextmanager
def run_server():
    process = Popen([
        sys.executable, MANAGE_FILE, 'runserver'
    ])
    time.sleep(1) # give server some time to start
    try:
        yield
    finally:
        process.terminate()


def main():
    remove_database()
    init_database()
    with run_server():
        test()


if __name__ == '__main__':
    main()