from modulino import ModulinoKnob, ModulinoMovement, ModulinoButtons, map_value_int
from machine import Pin

class Input:
    ##### DEVICES #####
    Button = Pin("D2", Pin.IN)
    Buttons = ModulinoButtons()
    Knob = ModulinoKnob()
    Movement = ModulinoMovement()

    ##### SETUP #####
    Knob.range = (0, 30)

    ##### VRIABLES #####
    button_side = False
    button_left = False
    button_center = False
    button_right = False
    button_knob = False
    knob_rotation = 0
    acceleration_down_up = 0
    acceleration_left_right = 0
    acceleration_back_front = 0
    gyro_nod = 0
    gyro_tilt = 0
    gyro_shake = 0

    def get_input(self):
        # update states
        self.Buttons.update()
        self.Knob.update()

        # assign values
        self.button_side = bool(self.Button.value())
        self.button_left = self.Buttons.button_a_pressed
        self.button_center = self.Buttons.button_b_pressed
        self.button_right = self.Buttons.button_c_pressed
        self.button_knob = self.Knob.pressed
        self.knob_rotation = self.Knob.value
        self.acceleration_left_right = self.Movement.accelerometer.y
        self.acceleration_back_front = self.Movement.accelerometer.y
        self.acceleration_down_up = self.Movement.accelerometer.z
        self.gyro_nod = self.Movement.gyro.x
        self.gyro_tilt = self.Movement.gyro.y
        self.gyro_shake = self.Movement.gyro.z

input = Input()