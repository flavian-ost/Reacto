# from output import Output
# from input import Input
from machine import Timer
from time import localtime

##### CONSTANTS #####
FREQUENCY = int(1000/60)

def main(timer):
    # Input.get_input()
    # Output.set_output()
    print(localtime())

timer = Timer(0)
timer.init(mode= Timer.PERIODIC, period=FREQUENCY, callback=main)

while True:
    pass