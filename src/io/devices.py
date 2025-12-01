from lib.modulino import ModulinoButtons, ModulinoBuzzer, ModulinoKnob, ModulinoMovement, ModulinoPixels
from lib.i2c_lcd import RGBDisplay
from lib.lcd_i2c import LCD
from lib.neopixel import NeoPixel
from lib.machine import I2C, Pin


Button = Pin("D2", Pin.IN)
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
Ring = NeoPixel(Pin("D8"), 16)