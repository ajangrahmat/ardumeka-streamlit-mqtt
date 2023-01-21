import streamlit as st
from paho.mqtt import client as mqtt


def on_connect(client, userdata, flags, rc):
    st.success("Subscribed to " + subscribeTopic)


def on_disconnect(client, userdata, flags, rc):
    st.write("Disconnected")


def get_mqtt_client():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_publish = on_publish
    return client

def on_publish(client, userdata, mid):
    print("mid: " + str(mid))


dataSuhu = st.empty()
def on_message(client, userdata, msg):
    dataSuhu.metric("Suhu", msg.payload.decode("utf-8"), "°C")

broker = "mqtt.ardumeka.com"
port = 11219
publishTopic = "ardumeka/h*&*&@!H!/led"
subscribeTopic = "ardumeka/jMKl8821*&^%/suhu"
client = get_mqtt_client()
client.on_publish = on_publish
client.connect(broker, int(port), 60)

st.title("ArduMeka")
st.subheader("Belajar Arduino dan Mekatonika")

st.sidebar.title("Menu")

if st.button("Lampu ON"):
    client.publish(publishTopic, "on")

if st.button("Lampu OFF"):
    client.publish(publishTopic, "off")

if st.button("RUN"):
    client = get_mqtt_client()
    client.on_message = on_message
    client.connect(broker, port, 60)
    client.subscribe(subscribeTopic)
    client.loop_forever()
