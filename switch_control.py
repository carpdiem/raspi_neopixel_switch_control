import gpiozero as g
import numpy as np
import requests as r
from time import sleep

def switch_turning_on(switch, color_temp = None, brightness = None, sleep_time = 1.0):
    sleep(sleep_time)
    if switch.is_active: 
        if color_temp == None and brightness == None:
            color_temp = 2900
            brightness = 0.7
        r1 = r.post("http://northwall-bedroom.local:5000/lights_on", data = {'color_temp': str(color_temp), 'brightness': str(brightness)})
        r2 = r.post("http://southwall-bedroom.local:5000/lights_on", data = {'color_temp': str(color_temp), 'brightness': str(brightness)})

def switch_turning_off(switch):
    r1 = r.post("http://northwall-bedroom.local:5000/lights_off")
    r2 = r.post("http://southwall-bedroom.local:5000/lights_off")

def plancksLaw(t):
    lambda_red = 630. * 10**-9
    lambda_green = 530. * 10**-9
    lambda_blue = 475. * 10**-9
    def planck(l, t):
        hc = 1.98644568 * 10**-25
        kb = 1.38064852 * 10**-23
        return 1. / (l**5.0 * (np.exp(hc / (l * kb * t)) - 1.0))
    red = planck(lambda_red, t)
    green = planck(lambda_green, t)
    blue = planck(lambda_blue, t)
    max = np.max([red, green, blue])
    return (red / max, green / max, blue / max)

def logarithmic_intensity(x):
    return 255 * (2**(5. * x) - 1) / (2**5. - 1) 

if __name__ == "__main__":
    switch_pin = g.DigitalInputDevice(5)
    switch_pin.when_activated = (lambda : switch_turning_on(switch_pin))
    switch_pin.when_deactivated = (lambda : switch_turning_off(switch_pin))
    while True:
        sleep(1)
