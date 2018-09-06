import gpiozero as g
import numpy as np
import requests as r
from time import sleep

def switch_turning_on(color_temp = None, brightness = None):
    if color_temp == None and brightness == None:
        color_temp = 3300
        brightness = 0.5
    r1 = r.post("http://northwall-bedroom:5000/lights_on", data = {'color_temp': str(color_temp), 'brightness': str(brightness)})
    r2 = r.post("http://southwall-bedroom:5000/lights_on", data = {'color_temp': str(color_temp), 'brightness': str(brightness)})

def switch_turning_off():
    r1 = r.post("http://northwall-bedroom:5000/lights_off")
    r2 = r.post("http://southwall-bedroom:5000/lights_off")

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
    return 255 * (2^(10 * x) - 1) / (2^10. - 1) 

if __name__ == "__main__":
    switch_pin = g.DigitalInputDevice(5)
    switch_pin.when_activated = switch_turning_on
    switch_pin.when_deactivated = switch_turning_off
    while True:
        sleep(1)
