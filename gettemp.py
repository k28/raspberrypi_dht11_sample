# coding: utf-8
# get temp and humidity data from DHT11
#
# before use this script
# wget http://osoyoo.com/driver/dht11.py
#

import time
import dht11
import RPi.GPIO as GPIO

# define GPIO 14 as DHT11 data pin
Temp_sensor=14

def main():
    # Main program
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)  # Use BCM GPIO numbers

    instance = dht11.DHT11(pin = Temp_sensor)

    while True:
        # get DHT11 sensor value
        result = instance.read()
        # センサーが0を返す事が多々あるので、0の時には無視...
        if result.humidity == 0:
            continue
        print("Temperature={}C Humidity={}%".format(result.temperature, result.humidity))
        time.sleep(1)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass



