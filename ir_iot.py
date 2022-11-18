import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

gpio.setup(3, gpio.IN)
gpio.setup(5, gpio.OUT)

while True:
    v=gpio.input(3,gpio.IN)
    if (v==0):
    gpio.output(5,gpio.False)
    else:
    gpio. output (5,gpio.True)
