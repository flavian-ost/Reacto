from modulino import (
    ModulinoButtons,
    ModulinoBuzzer,
    ModulinoKnob,
    ModulinoMovement,
    ModulinoPixels,
)
from lcd_i2c import LCD
from neopixel import NeoPixel
from machine import I2C, Pin


class DeviceManager:
    def __init__(self):
        ##### INSTANTIATE DEVICES #####
        self.Button = Pin("A0", Pin.IN)
        self.Buttons = ModulinoButtons()
        self.Buzzer = ModulinoBuzzer()
        self.Display = LCD(0x27, 16, 2, i2c=I2C(1))
        self.Knob = ModulinoKnob()
        self.Movement = ModulinoMovement()
        self.Pixels = ModulinoPixels()
        self.Ring = NeoPixel(Pin("A2"), 16)

        ##### SETUP DEVICES #####
        self.Display.begin()
        self.Knob.range = (0, 30)


# unique instance for use in other classes
Device = DeviceManager()
