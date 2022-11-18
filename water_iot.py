import RPi.GPIO as gpio

gpio. setmode(gpio. BOARD)
gpio.setup(5, gpio.IN)
gpio. setup (7 , gpio. OUT)

while True:
    v=gpio.input(5)

    if (v==0):
    gpio.output(7,True)
    else:
    gpio.output(7,False)