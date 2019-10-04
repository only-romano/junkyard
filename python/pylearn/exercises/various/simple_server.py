from wsgiref.simple_server import make_server
from datetime import datetime
from uuid import uuid4
import os


DATA_FOLDER = 'data/'


def fill_zero(st, size):
    st = str(st)
    ln = len(st)
    if len(st) < size:
        return '0' * (size-ln) + st
    else:
        return st


def gen_file_name(label=''):
    dt = datetime.now()
    uuid = str(uuid4())[0:8]

    year = fill_zero(dt.year, 4)
    month = fill_zero(dt.month, 2)
    day = fill_zero(dt.day, 2)
    hour = fill_zero(dt.hour, 2)
    minute = fill_zero(dt.minute, 2)
    second = fill_zero(dt.second, 2)

    return f'{year}-{month}-{day} {hour}:{minute}:{second} {label}_{uuid}.txt'


def write(data, label=''):
    mode = 'wb' if isinstance(data, bytes) else 'w'
    with open(DATA_FOLDER + gen_file_name(label), mode) as body_file:
        body_file.write(data)


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        request_body_size = 0
    body = environ['wsgi.input'].read(request_body_size)
    head = '\n'.join([f"{key}: {value}" for key, value in environ.items()])

    write(body, label='BODY')
    write(head, label='HEAD')

    start_response(status, headers)
    return [body]


if __name__ == '__main__':
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    with make_server('', 8000, application) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
