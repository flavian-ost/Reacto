from modulino import ModulinoKnob, ModulinoMovement, ModulinoButtons

class Input:
    button = []
    knob = 0
    acceleration = []
    rotation = []

    def get_input():
        print("reading input...")

    def get_button(which):
        match which:
            case "side":
                return button[0]
            case "left":
                return button[1]
            case "center":
                return button[2]
            case "right":
                return button[3]
    
    def get_acceleration(which):
        match which:
            case "x":
                return acceleration[0]
            case "y":
                return acceleration[1]
            case "z":
                return acceleration[2]
    
    def get_rotation(which):
        match which:
            case "x":
                return rotation[0]
            case "y":
                return rotation[1]
            case "z":
                return rotation[2]
