import socketio
import time

sio = socketio.Client()
sio.connect('http://localhost:8000')

@sio.on('to_client_b')
def on_message(data):
    print(f"Received from A: {data}")
    updated_data = {'x': data['x'] + 1, 'y': data['y'] + 1}
    sio.emit('from_client_b', updated_data)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    sio.disconnect()
