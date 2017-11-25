# ! -*- coding:utf-8 -*-
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import time
import json
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)
t = time.time()
nowTime = lambda: int(round(t * 1000))

data_chart = {
        "data": [
            {"name": "allpe", "num": 100},
            {"name": "peach", "num": 123},
            {"name": "Pear", "num": 234},
            {"name": "avocado", "num": 20},
            {"name": "cantaloupe", "num": 30},
            {"name": "Banana", "num": 77},
            {"name": "Grape", "num": 43},
            {"name": "apricot", "num": 22}
        ]
    }

name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

@app.route('/')
def index():
    return render_template('test.html')

@socketio.on('my event', namespace='/test')#对my_event事件进行监控
def handle_my_custom_event(message):
    print message['data'] + ':' + str(nowTime())
    emit('connect', "I am server!")#将信息发送到connect事件上

# @socketio.on('my json', namespace='/test')
# def handle_json(message):
#     print message + ':' + str(nowTime())
#     data = [{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}]
#     json_data = json.dumps(data)
#     emit('my json', json_data)

@socketio.on('my chart', namespace='/test')
def handle_json(message):
    print message + ':' + str(nowTime())
    msg = str(message)
    print msg, len(msg), 'next', len('next')

    if msg == 'next':
        production()
        emit('my chart', json.dumps(data_chart))
    else:
        emit('my chart', json.dumps(data_chart))

def production():
    list_add = {}
    i = random.randint(0, 25)
    j = random.randint(0, 25)
    new_name = name[i] + name[j]
    list_add['name'] = new_name
    list_add['num'] = random.randint(0, 500)
    data_chart['data'].append(list_add)
    data_chart['data'].pop(0)


if __name__ == '__main__':
    socketio.run(app)
