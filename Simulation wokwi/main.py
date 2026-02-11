from machine import Pin, ADC
import dht
import time

dht_sensor = dht.DHT22(Pin(4))
light_sensor = ADC(28)
gaz_sensor = ADC(27)



while True:
    try:
        dht_sensor.measure() #init
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        light = int(light_sensor.read_u16() * (100/65535)) # 0 65535
        gaz = int(gaz_sensor.read_u16() * (100/65535))
        print(f'temperature : {temperature} C | humidity : {humidity} % | light : {light} % | gaz :{gaz} %')
    except:
        print("error")

    time.sleep(1)