import socketio
import time

sio = socketio.Client()
sio.connect('http://localhost:8000')

sio.emit('from_client_a', {'x': 1.0, 'y': 2.0})

@sio.on('to_client_a')
def on_message(data):
    print(f"Received from B: {data}")
    updated_data = {'x': data['x'] + 1, 'y': data['y'] + 1}
    sio.emit('from_client_a', updated_data)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    sio.disconnect()
