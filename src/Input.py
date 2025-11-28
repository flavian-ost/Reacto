from modulino import ModulinoKnob, ModulinoMovement, ModulinoButtons, map_value_int
from machine import Pin, Timer


class InputManager:
    def __init__(self):
        ##### CONSTANTS #####
        self.FREQUENCY = int(1000 / 60)

        ##### DEVICES #####
        self.Button = Pin("D2", Pin.IN)
        self.Buttons = ModulinoButtons()
        self.Knob = ModulinoKnob()
        self.Movement = ModulinoMovement()

        ##### SETUP #####
        self.Knob.range = (0, 30)
        self.Timer = Timer(0)

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

    def get_input(self, timer):
        # update states
        self.Buttons.update()
        self.Knob.update()

        # assign values
        self.acceleration_back_front = self.Movement.accelerometer.y
        self.acceleration_down_up = self.Movement.accelerometer.z
        self.acceleration_left_right = self.Movement.accelerometer.x
        self.button_center = self.Buttons.button_b_pressed
        self.button_knob = self.Knob.pressed
        self.button_left = self.Buttons.button_a_pressed
        self.button_right = self.Buttons.button_c_pressed
        self.button_side = bool(self.Button.value())
        self.gyro_nod = self.Movement.gyro.x
        self.gyro_shake = self.Movement.gyro.z
        self.gyro_tilt = self.Movement.gyro.y
        self.knob_rotation = self.Knob.value

    def start(self):
        self.Timer.init(
            mode=Timer.PERIODIC, period=self.FREQUENCY, callback=self.get_input
        )


# singular instance for use in other classes
Input = InputManager()
