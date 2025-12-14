from device_manager import Device
from machine import Timer


class InputManager:
    def __init__(self): 
        ##### CONSTANTS #####
        # self.FREQUENCY = 60

        ##### OBJECTS #####
        # self.Timer = Timer(0)

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
        Device.Buttons.update()
        Device.Knob.update()

        # assign values
        self.acceleration_back_front = Device.Movement.accelerometer.y
        self.acceleration_down_up = Device.Movement.accelerometer.z
        self.acceleration_left_right = Device.Movement.accelerometer.x
        self.button_center = bool(Device.Buttons.button_b_pressed)
        self.button_knob = bool(Device.Knob.pressed)
        self.button_left = bool(Device.Buttons.button_a_pressed)
        self.button_right = bool(Device.Buttons.button_c_pressed)
        self.button_side = bool(Device.Button.value())
        self.gyro_nod = Device.Movement.gyro.x
        self.gyro_shake = Device.Movement.gyro.z
        self.gyro_tilt = Device.Movement.gyro.y
        self.knob_rotation = Device.Knob.value

    # def start(self):
    #     self.Timer.init(
    #         mode=Timer.PERIODIC, freq=self.FREQUENCY, callback=self.get_input
    #     )


# unique instance for use in other classes
Input = InputManager()
