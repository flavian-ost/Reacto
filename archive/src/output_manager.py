from device_manager import Device
from screens import VerticalMenu, HorizontalMenu
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
        self.BUZZER_NOTES = Device.Buzzer.NOTES
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
            note = Device.Buzzer.NOTES[note_name]
            Device.Buzzer.tone(note, duration, blocking=True)
            sleep(0.01)
        Device.Buzzer.no_tone()

    def buzzer_play_tone(self, note, duration):
        Device.Buzzer.tone(note, duration, blocking=True)
        Device.Buzzer.no_tone()

    def display_show_message(self, message, location=(0, 0)):
        Device.Display.set_cursor(*location)
        Device.Display.print(message)


# unique instance for use in other classes
Output = OutputManager()
