from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', namespace='/interface1')

@app.route('/second')
def second_interface():
    return render_template('second_interface.html', namespace='/interface2')

@socketio.on('message', namespace='/interface1')
def handle_message(message):
    print('Received message:', message)
    socketio.emit('message', message, namespace='/interface2')

@socketio.on('message', namespace='/interface2')
def handle_message(message):
    print('Received message:', message)
    socketio.emit('message', message, namespace='/interface1')

if __name__ == '__main__':
    socketio.run(app)
