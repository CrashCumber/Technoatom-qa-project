import threading
from flask import Flask, request, make_response, abort

app = Flask(__name__)

CONFIG = {
        'host': '0.0.0.0',
        'port': '5000',
}


def run_mock():
    server = threading.Thread(target=app.run, kwargs={'host': CONFIG["host"], 'port': CONFIG["port"]})
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


users = {'valentina': 1}


@app.route('/vk_id/<username>')
def get_user_by_id(username: str):
    user = users.get(username, None)
    result = {}
    if user:
        result = {'vk_id': user}
        res = make_response(result)
        res.headers['Status'] = '200 OK'
        res.headers['Content-Type'] = 'application/json'
        res.headers['Response'] = result
        return res
    else:
        res = make_response(result)
        res.headers['Status'] = '400 Not Found'
        res.headers['Content-Type'] = 'application/json'
        res.headers['Response'] = result
        return res


@app.route('/update/<username>')
def update_users(username: str):
    id = max(users.values()) + 1
    users.update({username: id})
    return users



@app.route('/shutdown')
def shutdown():
    shutdown_mock()


if __name__ == '__main__':
    run_mock()

