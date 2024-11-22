# Simulación de IoT con MQTT

Este proyecto simula una solución IoT con un sensor de luz y un interruptor de luz utilizando el protocolo MQTT.

## Requisitos
- Ubuntu con interfaz gráfica
- Mosquitto (Broker MQTT)
- Python 3
- paho-mqtt
- virtualizar entorno de python

## Instrucciones de ejecución

1. Instalar Mosquitto:
   ```bash
   sudo apt install mosquitto mosquitto-clients

2. Instalar paho-mqtt:
    ```bash
    pip install paho-mqtt

3. Ejecutar el broker Mosquitto:
    ```bash
    sudo systemctl start mosquitto

4. Ejecutar el script del publicador (sensor de luz):
    ```bash
    python sensor_luz.py

5. Ejecutar el script del suscriptor (interruptor de luz):
    ```bash
    python interruptor_luz.py

### Comandos adicionales

6. Para publicar datos desde un script Bash:
    ```bash
    chmod +x publicar_sensor.sh
    chmod +x interruptor_luz.sh
    ./publicar_sensor.sh
    ./interruptor_luz.sh


### Conclusión
Siguiendo estos pasos, habrás creado una solución IoT simple que simula la interacción entre un sensor de luz y un interruptor de luz utilizando MQTT.


