from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('postmessage',namespace='/bot/chat')
def postmessage(message):
    mess=message['msg']
    


