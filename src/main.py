from io.input import Input
from io.output import Output

def main():
    Input.start()
    Output.buzzer_play_melody(Output.BUZZER_MELODIES["Dixie"])
    while True:
        pass

main()