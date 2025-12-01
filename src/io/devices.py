from lib.modulino import ModulinoButtons, ModulinoBuzzer, ModulinoKnob, ModulinoMovement, ModulinoPixels
from lib.i2c_lcd import RGBDisplay
from lib.lcd_i2c import LCD
from lib.neopixel import NeoPixel
from machine import I2C, Pin

##### INSTANTIATE DEVICES #####
try:
    Button = Pin("D2", Pin.IN)
except Exception:
    print("[WARN] No Button found!")
try:
    Display = LCD(0x27, 16, 2, i2c=I2C(1))  # TODO: replace with RGB display
    #Display = RGBDisplay(I2C(1))
except Exception:
    print("[WARN] No Display found!")
try:
    Buttons = ModulinoButtons()
except Exception:
    print("[WARN] No Buttons found!")
try:
    Buzzer = ModulinoBuzzer()
except:
    print("[WARN] No Buzzer found!")
try:
    Knob = ModulinoKnob()
except Exception:
    print("[WARN] No Knob found!")
try:
    Movement = ModulinoMovement()
except Exception:
    print("[WARN] No Movement found!")
try:
    Pixels = ModulinoPixels()
except Exception:
    print("[WARN] No Pixels found!")
try:
    Ring = NeoPixel(Pin("D8"), 16)
except Exception:
    print("[WARN] No Ring found!")

##### SETUP DEVICES #####
Display.begin()
Display.no_blink()
Display.no_cursor()
Display.no_autoscroll()
Knob.range = (0, 30)