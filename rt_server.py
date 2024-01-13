import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

clients = {}

@sio.event
async def connect(sid, environ):
    print(f"Client {sid} connected")
    clients[sid] = sid

@sio.event
async def disconnect(sid):
    print(f"Client {sid} disconnected")
    clients.pop(sid, None)

@sio.event
async def from_client_a(sid, data):
    print(f"Received from A: {data}")
    for client_sid in clients:
        if client_sid != sid:
            await sio.emit('to_client_b', data, room=client_sid)

@sio.event
async def from_client_b(sid, data):
    print(f"Received from B: {data}")
    for client_sid in clients:
        if client_sid != sid:
            await sio.emit('to_client_a', data, room=client_sid)

if __name__ == '__main__':
    web.run_app(app, host='127.0.0.1', port=8000)
