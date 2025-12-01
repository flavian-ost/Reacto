from io.devices import Buzzer, Display, Pixels, Ring
from timer import Timer
from menu import VerticalMenu, HorizontalMenu
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

    ##### METHODS #####
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
        Display.set_cursor(location)
        Display.print(message)

    def pixels_set_brightness(self, brightness):
        pass

    def pixels_set_color(self, brightness):
        pass

    def ring_set_brightness(self, brightness):
        pass

    def ring_set_color(self, color):
        pass

    def create_menu_horizontal(self, message, option_left, option_right):
        Menu = HorizontalMenu(Display, message, option_left, option_right)
        return Menu

    def create_menu_vertical(self, message, options):
        Menu = VerticalMenu(Display, message, options)
        return Menu

    def create_timer(self, message, time, on_timer_end):
        timer = Timer(Display, message, time, on_timer_end)
        return timer


# singular instance for use in other classes
Output = OutputManager()
