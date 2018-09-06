import gpiozero as g
import numpy as np
import requests as r
from time import sleep

def switch_turning_on():
    r1 = r.post("http://northwall-bedroom:5000/lights_on", data = {'color_temp': '3300', 'brightness': '0.5'})
    r2 = r.post("http://southwall-bedroom:5000/lights_on", data = {'color_temp': '3300', 'brightness': '0.5'})

def switch_turning_off():
    r1 = r.post("http://northwall-bedroom:5000/lights_off")
    r2 = r.post("http://southwall-bedroom:5000/lights_off")


if __name__ == "__main__":
    switch_pin = g.DigitalInputDevice(5)
    switch_pin.when_activated = switch_turning_on
    switch_pin.when_deactivated = switch_turning_off
    while True:
        sleep(1)
