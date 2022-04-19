from flask import request
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from app import db_m
@socketio.on('postmessage',namespace='/bot/chat')
def postmessage(message):
    mess=message['msg']
    print(mess)
    
    search_query = {'ip':request.remote_addr}
    cnt=0
    for x in db_m.find(search_query):
        print(x)
        cnt+=1
    if cnt==0:
        mydict = { "ip": request.remote_addr , "message": [mess] }
        x = db_m.insert_one(mydict)
    else:
        query = {"ip": request.remote_addr}
        current = db_m.find(query)[0]
        current['message'].append(mess)
        update = {"$set":{"message":current['message']}}
        db_m.update_one(db_m.find(query)[0],update)
    print(request.remote_addr)


