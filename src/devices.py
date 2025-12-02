from modulino import (
    ModulinoButtons,
    ModulinoBuzzer,
    ModulinoKnob,
    ModulinoMovement,
    ModulinoPixels,
)
from i2c_lcd import RGBDisplay
from neopixel import NeoPixel
from machine import I2C, Pin

##### INSTANTIATE DEVICES #####
try:
    Button = Pin("D2", Pin.IN)
except Exception:
    print("[WARN] No Button found!")
    Button = {}
try:
    Buttons = ModulinoButtons()
except Exception:
    print("[WARN] No Buttons found!")
    Buttons = {}
try:
    Buzzer = ModulinoBuzzer()
except:
    print("[WARN] No Buzzer found!")
    Buzzer = {}
try:
    Display = RGBDisplay(I2C(1))
    Display.display(True)
    Display.autoscroll(False)
    Display.blink_cursor(False)
    Display.cursor(False)
except Exception:
    print("[WARN] No Display found!")
    Display = {}
try:
    Knob = ModulinoKnob()
    Knob.range = (0, 30)
except Exception:
    print("[WARN] No Knob found!")
    Knob = {}
try:
    Movement = ModulinoMovement()
except Exception:
    print("[WARN] No Movement found!")
    Movement = {}
try:
    Pixels = ModulinoPixels()
except Exception:
    print("[WARN] No Pixels found!")
    Pixels = {}
try:
    Ring = NeoPixel(Pin("D8"), 16)
except Exception:
    print("[WARN] No Ring found!")
    Ring = {}
