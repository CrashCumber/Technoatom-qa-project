from os import abort
import json
import threading

from mysql import connector
import sys
from flask import Flask, request, Request, Response, make_response

app = Flask(__name__)

import mysql.connector

def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/')
def index():
    return 'Hello World! Docker-Compose for Flask & Mysql\n'


@app.route('/shutdown')
def shutdown():
    shutdown_mock()


@app.route('/vk_id/<username>')
def get_id(username: str):
    config = {
        'user': 'test_qa',
        'password': 'qa_test',
        'host': 'db',
        'port': '3306',
        'database': 'technoatom'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute(f'SELECT id FROM test_users WHERE username="{username}";')
    user_id = cursor.fetchone()
    result = {}
    if user_id:
        result = {'vk_id': user_id[0]}
        cursor.close()
        connection.close()
        res = make_response(result)
        res.headers['Status'] = '200 OK'
        res.headers['Content-Type'] = 'application/json'
        res.headers['Response'] = result
        return res
    else:
        cursor.close()
        connection.close()
        res = make_response(result)
        res.headers['Status'] = '400 Not Found'
        res.headers['Content-Type'] = 'application/json'
        res.headers['Response'] = result
        # abort(404)
        return res


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)





















#
# def run_mock():
#     server = threading.Thread(target=app.run, kwargs={'host': host, 'port': port, 'debug': True})
#     server.start()
#     return server




# @app.route('/post')
# def post_user():
#     try:
#         data = {'v': 2}
#         user_data.update(data)
#     except :
#         pass
#     return json.dumps(user_data)

# user_data = {'Ilya' :'1'}
# @app.route('/vk_id/<username>')
# def get_id(username: str):
#     user_id = user_data.get(username, None)
#     if user_id:
#         print(user_id)
#         return {'vk_id': user_id}
#     else:
#         abort(404)
#         return {}


