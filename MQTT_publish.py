import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("test")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)

flag = 1
while(True):
	if(flag):
		client.publish("test", "OFF")
		flag = 0
	else:
		client.publish("test", "ON")
		flag = 1
	time.sleep(2)
