import paho.mqtt.client as mqtt
import json

# Configuración del broker MQTT
broker = "localhost"  # Dirección del broker (localhost si está en la misma máquina)
puerto = 1883         # Puerto por defecto de MQTT
tema = "sensor/luz"   # Tema donde el sensor publica los datos

# Función para procesar los mensajes recibidos
def on_message(client, userdata, message):
    mensaje = message.payload.decode("utf-8")  # Decodificar el mensaje recibido
    datos = json.loads(mensaje)  # Convertir el JSON a diccionario

    valor_luz = datos['value']
    precision = datos['accuracy']

    # Controlar las luces
    if valor_luz < 50 and precision > 0.9:
        print("Las luces se encenderán.")
    else:
        print("Las luces se apagarán.")

# Configuración del cliente MQTT
def iniciar_subscriptor():
    client = mqtt.Client()
    client.connect(broker, puerto)

    # Configurar el callback para cuando se recibe un mensaje
    client.on_message = on_message

    # Suscribirse al tema 'sensor/luz'
    client.subscribe(tema)

    # Mantener la conexión y esperar mensajes
    client.loop_forever()

if __name__ == "__main__":
    iniciar_subscriptor()
