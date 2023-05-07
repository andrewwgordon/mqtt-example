import sys
import paho.mqtt.client as mqtt

def on_connect(mqttc, obj, flags, rc):
    if rc == 5:
        print('Unauthorised')
        sys.exit()

def on_message(mqttc, obj, msg):
    print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

def on_publish(mqttc, obj, mid):
    print("mid: "+str(mid))

def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: "+str(mid)+" "+str(granted_qos))

def on_log(mqttc, obj, level, string):
    print(string)


mqtt_client = mqtt.Client('andrewwgordon',transport='websockets')
mqtt_client.on_message = on_message
mqtt_client.on_connect = on_connect
mqtt_client.on_publish = on_publish
mqtt_client.on_subscribe = on_subscribe
mqtt_client.ws_set_options(path=sys.argv[2],headers=None)
mqtt_client.username_pw_set(username=sys.argv[3],password=sys.argv[4])
mqtt_client.tls_set()
mqtt_client.connect(sys.argv[1],443,60)
if mqtt_client.is_connected:
    print('Connected')
    mqtt_client.subscribe('test')
    mqtt_client.loop_forever()
else:
    print('Not connected')