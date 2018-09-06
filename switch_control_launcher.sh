#!/bin/bash

if pgrep -x "python" > /dev/null
then
	echo "Running"
else
	echo "Failed to find switch control program"
	echo "Trying to restart"
	echo date
	python /home/pi/raspi_neopixel_switch_control/switch_control.py &
