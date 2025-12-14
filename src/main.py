from lcd_i2c import LCD
from machine import I2C, Pin
from modulino import (
    ModulinoButtons,
    ModulinoBuzzer,
    ModulinoKnob,
    ModulinoMovement,
    ModulinoPixels,
)
from neopixel import NeoPixel
from time import sleep


class DeviceManager:
    def __init__(self):
        ##### INSTANTIATE DEVICES #####
        # self.Button = Pin("A0", Pin.IN)
        # self.Buttons = ModulinoButtons()
        self.Buzzer = ModulinoBuzzer()
        self.Display = LCD(0x27, 16, 2, i2c=I2C(1))
        self.Knob = ModulinoKnob()
        self.Movement = ModulinoMovement()
        # self.Pixels = ModulinoPixels()
        # self.Ring = NeoPixel(Pin("A2"), 16)

        ##### SETUP DEVICES #####
        self.Display.begin()
        self.Display.cursor_off()
        self.Knob.range = (0, 30)


Device = DeviceManager()


class InputManager:
    def __init__(self):

        ##### VARIABLES #####
        self.acceleration_back_front = 0
        self.acceleration_down_up = 0
        self.acceleration_left_right = 0
        self.button_center = False
        self.button_knob = False
        self.button_left = False
        self.button_right = False
        self.button_side = False
        self.gyro_nod = 0
        self.gyro_shake = 0
        self.gyro_tilt = 0
        self.knob_rotation = 0

    def update(self):
        # update states
        # Device.Buttons.update()
        Device.Knob.update()

        # assign values
        self.acceleration_back_front = Device.Movement.accelerometer.y
        self.acceleration_down_up = Device.Movement.accelerometer.z
        self.acceleration_left_right = Device.Movement.accelerometer.x
        # self.button_center = bool(Device.Buttons.button_b_pressed)
        self.button_knob = bool(Device.Knob.pressed)
        # self.button_left = bool(Device.Buttons.button_a_pressed)
        # self.button_right = bool(Device.Buttons.button_c_pressed)
        # self.button_side = bool(Device.Button.value())
        self.gyro_nod = Device.Movement.gyro.x
        self.gyro_shake = Device.Movement.gyro.z
        self.gyro_tilt = Device.Movement.gyro.y
        self.knob_rotation = Device.Knob.value

    def wait_for_continue(self):
        while True:
            Device.Knob.update()
            if Device.Knob.pressed:
                break
            sleep(0.1)


Input = InputManager()


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
    
    def display_clear():
        Device.Display.clear()


Output = OutputManager()


class Player:
    def __init__(self, id: int):
        self.id = id
        self.score = 0

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

class Game:
    def __init__(self, players: list[Player]):
        self.players = players
        self.results = []
        for _ in range(len(self.players)):
            self.results.append(0)

class GameHideAndSeek(Game):
    def __init__(self, players: list[Player]):
        super(players)
    
    def start(self):
        Output.display_show_message("Hide and Seek", (0, 0))
        Output.display_show_message("Press to proceed", (0, 1))
        Input.wait_for_continue()
        for player in self.players:
            Output.display_show_message(f"Player {player.id} hide", (0, 0))
            Output.display_show_message("Press to proceed", (0, 1))
            Input.wait_for_continue()
            



class GameSpeedItUp:
    def __init__(self, players):
        self.players = players


class GameTimeGuess:
    def __init__(self, players):
        self.players = players


class GameHotPotato:
    def __init__(self, players):
        self.players = players


class GameManager:
    def __init__(self, player_count):
        self.HotPotato = GameHotPotato()
        self.TimeGuess = GameTimeGuess()
        self.SpeedItUp = GameSpeedItUp()
        self.HideAndSeek = GameHideAndSeek()
        self.players = []
        for player_number in range(player_count):
            self.players.append(Player(player_number))