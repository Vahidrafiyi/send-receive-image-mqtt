import base64
from paho.mqtt  import client as mqtt_client
from datetime   import datetime


broker_url  = 'broker.hivemq.com'
port        = 1883
topic       = 'image'
client_id   = "client_2"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("client connected to the broker successfully :)")
    else:
        print("client could not connect to the broker :(")

def create_client():
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.username_pw_set('vahid', 'vahid')
    return client

def on_message(client: mqtt_client.Client, userdata, msg):
    image_data = msg.payload.decode()
    msg = str(image_data)
    img = msg.encode('ascii')

    now = datetime.now()
    filename = now.strftime('%m%d%Y-%H%M%S.jpg')

    file = open(f'images/{filename}', 'wb')
    final_img = base64.b64decode(img)
    file.write(final_img)
    file.close()

if __name__ == '__main__':
    client = create_client()
    client.connect(broker_url, port)
    client.subscribe(topic)
    client.on_message = on_message
    client.loop_forever()
