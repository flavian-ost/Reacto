from time import sleep
from lcd_i2c import LCD, RGBDisplay
from machine import I2C, Pin
from neopixel import NeoPixel
from modulino import ModulinoPixels, ModulinoBuzzer


class OutputManager:
    def __init__(self):
        ##### CONSTANTS #####
        self.MELODIES = {
            "Dixie": [
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
        }
        self.NOTES = self.Buzzer.NOTES
        self.RING_LED_COUNT = 16
        self.TEXT_ANIMATIONS = {
            "None": 0,
            "Scroll": 1,
            "Type": 2,
        }

        ##### DEVICES #####
        self.Buzzer = ModulinoBuzzer()
        self.Display = LCD(0x27, 16, 2, i2c=I2C(1))  # TODO: replace with RGB display
        self.Pixels = ModulinoPixels()
        self.Ring = NeoPixel(Pin("D8"), self.RING_LED_COUNT)

        ##### SETUP #####
        self.Display.begin()

    def buzzer_play_melody(self, melody):
        for note_name, duration in melody:
            note = self.Buzzer.NOTES[note_name]
            self.Buzzer.tone(note, duration, blocking=True)
            sleep(0.01)
        self.Buzzer.no_tone()

    def buzzer_play_tone(self, note, duration):
        self.Buzzer.tone(note, duration, blocking=True)
        self.Buzzer.no_tone()
    
    def display_show_message(self, message):
        self.Display.clear()
        self.Display.write(message)

    def pixels_set_brightness(self, brightness):
        pass

    def pixels_set_color(self, brightness):
        pass
    
    def ring_set_brightness(self, brightness):
        pass

    def ring_set_color(self, color):
        pass


# singular instance for use in other classes
Output = OutputManager()
