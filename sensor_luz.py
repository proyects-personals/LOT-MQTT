import paho.mqtt.client as mqtt
import json
from time import sleep

# Configuración del broker MQTT
broker = "localhost"  # Dirección del broker (localhost si está en la misma máquina)
puerto = 1883         # Puerto por defecto de MQTT
tema = "sensor/luz"   # Tema donde el sensor publicará los datos

# Función para publicar datos
def publicar_datos():
    client = mqtt.Client()
    client.connect(broker, puerto)

    while True:
        # Datos del sensor (simulando datos de luz)
        datos_sensor = {
            "device_id": "5ee9df89-a719-4e9a-ac54-84b9c3096f40",
            "event_time": "2025-06-12 14:07:46.580465000",
            "value": 60,  # Simulando el valor del sensor de luz
            "accuracy": 0.98
        }

        # Convertir el diccionario a JSON
        mensaje = json.dumps(datos_sensor)
        
        # Publicar el mensaje en el tema 'sensor/luz'
        client.publish(tema, mensaje)
        print("Publicado:", mensaje)
        sleep(5)  # Publicar cada 5 segundos (simulando actualización del sensor)

if __name__ == "__main__":
    publicar_datos()
