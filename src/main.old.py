from time import sleep
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
from device_manager import Device


##### CONSTANTS #####
MAX_PLAYER_COUNT = 6
MIN_PLAYER_COUUNT = 1

##### INSTANTIATE DEVICES #####
Button = Pin("A0", Pin.IN)
Buttons = ModulinoButtons()
Buzzer = ModulinoBuzzer()
Display = LCD(0x27, 16, 2, i2c=I2C(1))
Knob = ModulinoKnob()
Movement = ModulinoMovement()
Pixels = ModulinoPixels()
Ring = NeoPixel(Pin("A2"), 16)

player_count = 1

def setup_devices():
    Display.begin()
    Knob.range = (0, 30)

def on_power_on():
    melody = [
                ("G5", 100),
                ("E5", 100),
                ("C5", 200),
                ("C5", 200),
                ("C5", 100),
                ("D5", 100),
                ("E5", 100),
                ("F5", 100),
                ("G5", 200),
                ("G5", 200),
                ("G5", 200),
                ("E5", 200),
            ]
    for note_name, duration in melody:
        note = Buzzer.NOTES[note_name]
        Buzzer.tone(note, duration, blocking=True)
        sleep(0.01)
    Buzzer.no_tone()
    Display.clear()
    Display.set_cursor(0, 0)
    Display.print("  Welcome to   ")
    Display.set_cursor(0, 1)
    Display.print("==== REACTO ====")

def player_menu():
    Display.clear()
    Display.set_cursor(0, 0)
    Display.print("Player Count:")
    Display.set_cursor(0, 1)
    Display.print(str(player_count))

def player_menu_increase():
    global player_count
    player_count += 1
    if player_count > MAX_PLAYER_COUNT:
        player_count = MAX_PLAYER_COUNT

def player_menu_decrease():
    global player_count
    player_count -= 1
    if player_count < MIN_PLAYER_COUUNT:
        player_count = MIN_PLAYER_COUUNT

def player_selection():
    player_menu()
    Knob.on_rotate_clockwise = player_menu_decrease
    Knob.on_rotate_counter_clockwise = player_menu_increase
    while True:
        player_menu()
        sleep(0.1)

def main():
    setup_devices()
    # on_power_on()
    # sleep(5)
    player_selection()

main()
