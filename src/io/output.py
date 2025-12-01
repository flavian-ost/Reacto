from io.devices import Buzzer, Display, Pixels, Ring
from time import sleep


class OutputManager:
    def __init__(self): 
        ##### CONSTANTS #####
        self.BUZZER_MELODIES = {
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
        self.BUZZER_NOTES = Buzzer.NOTES
        self.DISPLAY_ANIMATIONS = {
            "None": 0,
            "Scroll": 1,
            "Type": 2,
        }
        self.DISPLAY_COLORS = {
            "Blue": (0, 0, 255),
            "Green": (0, 255, 0),
            "Red": (255, 0, 0),
            "White": (255, 255, 255),
        }

        ##### SETUP #####
        Display.begin()
        Display.no_blink()
        Display.cursor(False)
        Display.display(True)

    def buzzer_play_melody(self, melody):
        for note_name, duration in melody:
            note = Buzzer.NOTES[note_name]
            Buzzer.tone(note, duration, blocking=True)
            sleep(0.01)
        Buzzer.no_tone()

    def buzzer_play_tone(self, note, duration):
        Buzzer.tone(note, duration, blocking=True)
        Buzzer.no_tone()

    def display_show_message(self, message, location=(0, 0)):
        Display.clear()
        Display.print(message)

    def display_menu_horizontal_show(self, message, option_left, option_right):
        Display.set_cursor(0, 0)
        Display.print(message)
        Display.set_cursor(0, 1)
        Display.print(f">{option_left[:7]}")
        Display.set_cursor(8, 1)
        Display.print(f" {option_right[:7]}")

    def display_menu_vertical_show(self, message, options):
        pass

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
