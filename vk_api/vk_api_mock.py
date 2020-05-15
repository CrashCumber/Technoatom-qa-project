
import json
import mysql.connector
from flask import Flask, request, make_response
import datetime

app = Flask(__name__)

CONFIG = {
        'user': 'test_qa',
        'password': 'qa_test',
        'host': 'db',
        'port': '3306',
        'database': 'technoatom'
}


@app.route('/')
def index():
    return 'Hello World! Docker-Compose for Flask & Mysql\n'


@app.route('/vk_id/<username>')
def get_id(username: str):
    connection = mysql.connector.connect(**CONFIG)
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
        return res


@app.route('/get_user/<username>')
def get_user(username: str):
    connection = mysql.connector.connect(**CONFIG)
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM test_users WHERE username="{username}";')
    user = cursor.fetchone()
    if not user:
        cursor.close()
        connection.close()
        res = make_response(json.dumps('0'), 404)
        res.headers['Content-Type'] = 'application/json'
        return res
    cursor.close()
    connection.close()
    time = user[6]
    if time:
        time = user[6].strftime('%Y-%d-%m %H:%M:%S')
    data = {
            "id": user[0],
            "username": user[1],
            "password": user[2],
            "email": user[3],
            "access": user[4],
            "active": user[5],
            "start_active_time": time
            }
    res = make_response(json.dumps(data), 201)
    res.headers['Content-Type'] = 'application/json'
    return res


@app.route('/insert_user/', methods=['POST', 'GET'])
def insert_user():
    data = request.get_json()
    data = json.loads(data)
    connection = mysql.connector.connect(**CONFIG)
    cursor = connection.cursor()
    insert = f"""
                   INSERT INTO `test_users` (
                    `username`,
                    `password`,
                    `email`,
                    `access`
                    )
                    VALUES (
                    '{data["username"]}',
                    '{data["password"]}',
                    '{data["email"]}',
                     {data["access"]}
                    );
               """
    cursor.execute(insert)
    connection.commit()
    cursor.close()
    connection.close()
    return 'Successful'


@app.route('/delete_user/<username>')
def delete_user(username: str):
    connection = mysql.connector.connect(**CONFIG)
    cursor = connection.cursor()
    cursor.execute(f" DELETE FROM `test_users` WHERE username='{username}';")
    connection.commit()
    cursor.close()
    connection.close()
    return 'Successful'


@app.route('/make_user_active/<username>')
def active_user(username: str):
    connection = mysql.connector.connect(**CONFIG)
    cursor = connection.cursor()
    cursor.execute(f"UPDATE `test_users` SET active=1, start_active_time=CURRENT_TIMESTAMP WHERE username='{username}';")
    connection.commit()
    cursor.close()
    connection.close()
    return 'Successful'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)







#
#
#
# @app.route('/uns')
# def u_user():
#     _request()
#     return 'Successful'











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
#
# def shutdown_mock():
#     terminate_func = request.environ.get('werkzeug.server.shutdown')
#     if terminate_func:
#         terminate_func()
# @app.route('/shutdown')
# def shutdown():
#     shutdown_mock()


