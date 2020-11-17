import RPi.GPIO as GPIO
gpio_pin = 18


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(gpio_pin, GPIO.OUT)
    GPIO.output(gpio_pin, GPIO.LOW)
    print ('using pin%d'%gpio_pin)

def turn_on():
    GPIO.output(gpio_pin, GPIO.HIGH)
    print ('lights on >>>')

def turn_off():
    GPIO.output(gpio_pin, GPIO.LOW)
    print ('lights off >>>')


def destroy():
    GPIO.cleanup()