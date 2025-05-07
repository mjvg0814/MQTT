import paho.mqtt.client as paho
import time
import streamlit as st
import json

values = 0.0
act1 = "OFF"

def on_publish(client, userdata, result):
    print("El dato ha sido publicado.\n")
    pass

def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(f"Mensaje recibido: {message_received}")

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("IDENTIFICADOR_A")
client1.on_message = on_message

st.title("🛰 Control MQTT")

st.subheader("Control del Dispositivo")
col1, col2 = st.columns(2)

with col1:
    if st.button('Encender'):
        act1 = "ON"
        client1 = paho.Client("IDENTIFICADOR_A")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("topico2_A", message)
        st.success("Dispositivo encendido.")
        
with col2:
    if st.button('Apagar'):
        act1 = "OFF"
        client1 = paho.Client("IDENTIFICADOR_A")
        client1.on_publish = on_publish
        client1.connect(broker, port)
        message = json.dumps({"Act1": act1})
        ret = client1.publish("topico2_A", message)
        st.success("Dispositivo apagado.")

st.subheader("Enviar Valor Analógico")
values = st.slider('Selecciona el rango de valores', 0.0, 100.0, step=0.1)
st.write('Valor seleccionado:', values)

if st.button('Enviar valor analógico'):
    client1 = paho.Client("IDENTIFICADOR_A")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("topico1_A", message)
    st.success("Valor analógico enviado.")






