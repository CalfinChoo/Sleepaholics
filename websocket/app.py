from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send, join_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('join_room')
def handle_join_room_event(data):
    print("User connected to room {}".format(data["room"]))
    join_room(data['room'])
    socketio.emit('room_announcement', room=data["room"])

@socketio.on('send_message')
def handle_send_message_event(data):
    socketio.emit('receive_message', data, room=data["room"])

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/chat')
def chat():
    print(request.args)
    room = request.args.get('room')
    if room:
        return render_template('room.html', room=room)
    else:
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.debug = True
    socketio.run(app)