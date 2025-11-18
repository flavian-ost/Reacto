from modulino import ModulinoPixels, ModulinoBuzzer
from lcd_i2c import LCD
from machine import I2C

display = LCD(0x27, 16, 2, i2c=I2C(1))
display.begin()

class Output:
    def set_output():
        print("setting output...")
    
    def display_message(message):
        display.print(message)