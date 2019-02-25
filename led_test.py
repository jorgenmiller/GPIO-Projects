#Raspberry Pi GPIO led test
#turns on an led
#B17 -> led -> 200 ohm resistor -> ground

import RPi.GPIO as GPIO

def setup():
    GPIO.setmode(GPIO.BCM) #pins identified by BCM numbering system
    GPIO.setup(17, GPIO.OUT, initial=GPIO.LOW) #led starts as off

def main():
    GPIO.output(17, GPIO.HIGH) #led on

try:
    setup()
    main()

finally: #before quitting due to error
    print("exiting")
    GPIO.cleanup() #undo pin asignments
