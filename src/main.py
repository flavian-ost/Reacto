from input import Input
from output import Output


def none():
    pass

def main():
    Input.start()
    # Output.buzzer_play_melody(Output.BUZZER_MELODIES["Dixie"])
    Menu = Output.create_menu_horizontal("Test", "Yes", "No")
    Menu.show()
    while True:
        pass

main()