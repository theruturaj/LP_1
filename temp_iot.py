import Adafruit_DHT
import time

while True:
    humidity, temperature = Adafruit_DHT.read_retry(ll,4)
    print (temperature, humidity)
    time.sIeep(5)