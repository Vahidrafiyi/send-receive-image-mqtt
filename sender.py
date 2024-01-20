import base64
from paho.mqtt import client as mqtt_client
import time


broker_url  = 'broker.hivemq.com'
port        = 1883
topic       = 'image'
client_id   = "client_1"

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

def publish(client: mqtt_client.Client):
    with open('images/logo.jpg', 'rb') as file:
        file_content    = file.read() 
        encoded_content = base64.b64encode(file_content)
        result = client.publish(topic, encoded_content)
        if result[0] == 0:
            print("image sent successfully :)")
        else:
            print("image did not send successfully :(")

if __name__ == '__main__':
    client = create_client()
    client.connect(broker_url, port)
    client.loop_start()
    publish(client)
    client.loop_stop()
