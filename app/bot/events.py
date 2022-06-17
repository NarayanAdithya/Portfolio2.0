from flask import request
from flask_socketio import emit, join_room, leave_room
import json
from .. import socketio
from app import app,db_m
import requests
import os

@socketio.on('postmessage',namespace='/bot/chat')
def postmessage(message):
    mess=message['msg']
    search_query = {'ip':request.remote_addr}
    cnt=0
    for x in db_m.find(search_query):
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
    print("About to Execute Response")
    try:
        response=requests.post(app.config['ADI_BOT_URL'],data=json.dumps({'sender':hash(request.remote_addr),'message':mess}))
    except requests.exceptions.ConnectionError:
        response={'text':'Connection to Bot Failed, Sorry!'}
    print("Emitted")
    emit('received_message',response)