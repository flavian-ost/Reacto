from io.devices import Button, Buttons, Knob, Movement
from machine import Timer


class InputManager:
    def __init__(self): 
        ##### CONSTANTS #####
        self.FREQUENCY = 30

        ##### OBJECTS #####
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
        Buttons.update()
        Knob.update()

        # assign values
        self.acceleration_back_front = Movement.accelerometer.y
        self.acceleration_down_up = Movement.accelerometer.z
        self.acceleration_left_right = Movement.accelerometer.x
        self.button_center = Buttons.button_b_pressed
        self.button_knob = Knob.pressed
        self.button_left = Buttons.button_a_pressed
        self.button_right = Buttons.button_c_pressed
        self.button_side = bool(Button.value())
        self.gyro_nod = Movement.gyro.x
        self.gyro_shake = Movement.gyro.z
        self.gyro_tilt = Movement.gyro.y
        self.knob_rotation = Knob.value

    def start(self):
        self.Timer.init(
            mode=Timer.PERIODIC, freq=self.FREQUENCY, callback=self.get_input
        )


# singular instance for use in other classes
Input = InputManager()
