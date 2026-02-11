import network
from simple import MQTTClient
import dht
import time
from machine import Pin, ADC
import random
import ujson

dht_sensor = dht.DHT22(Pin(4))
light_sensor = ADC(28)
gaz_sensor = ADC(27)

# ====== Configuration du Wi-Fi ======
SSID = "TOPNET_9220"
PASSWORD = "xg6cpb4665"

wlan = network.WLAN(network.STA_IF) 
wlan.active(True)

try:
    print("Connexion au Wi-Fi...")
    wlan.connect(SSID, PASSWORD)

    
    max_wait = 5
    while max_wait > 0:
        if wlan.isconnected():
            break
        print("En attente de connexion...")
        time.sleep(1)
        max_wait -= 1

    if wlan.isconnected():
        print("Connecté au Wi-Fi !")
        print("Adresse IP :", wlan.ifconfig()[0])
    else:
        print(" Échec de connexion au Wi-Fi.")

except Exception as e:
    print("Erreur de connexion Wi-Fi :", e)
    
    
mqtt_server = 'broker.emqx.io'
client_id = 'aziz'
pub_topic = b'pico/data'






def mqtt_connect():
    try:
        client = MQTTClient(client_id, mqtt_server, keepalive=3600)
        client.connect()
        print(f"Connected to {mqtt_server} MQTT Broker")
        return client
    except Exception as e:
        print(f" Failed to connect to MQTT Broker: {e}")
        reconnect()

def reconnect():
    print("Reconnecting to MQTT Broker in 5 seconds...")
    time.sleep(5)
    try:
        return mqtt_connect()  # On tente de se reconnecter
    except Exception as e:
        print(f"️ Reconnection failed: {e}")
        time.sleep(5)
        return reconnect()     # Relance jusqu’à succès

client = mqtt_connect()
  


while True:
    dht_sensor.measure() #init
    temperature = dht_sensor.temperature()
    humidity = dht_sensor.humidity()
    light = int(light_sensor.read_u16() * (100/65535)) # 0 65535
    gaz = int(gaz_sensor.read_u16() * (100/65535))
   
    #temperature = random.randint(0,100)
    #humidity = random.randint(0,100)
    #light = random.randint(0,100) # 0 65535
    #gaz = random.randint(0,100)
    #print(f'temperature : {temperature} C | humidity : {humidity} % | light : {light} % | gaz :{gaz} %')
    
    my_data = ujson.dumps(
        {
            "temperature": temperature,
            "humidity": humidity,
            "light": light,
            "gaz": gaz
            })
    client.publish(pub_topic, my_data.encode()) 
    print("data published")
    time.sleep(5)
   
   
   
   
   
   
   
   
   



