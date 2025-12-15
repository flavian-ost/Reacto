from math import sqrt
from random import randint
from time import sleep
from modulino import (
    ModulinoButtons,
    ModulinoBuzzer,
    ModulinoKnob,
    ModulinoMovement,
    ModulinoPixels,
)
from lcd_i2c import LCD
from neopixel import NeoPixel
from machine import I2C, Pin

##### INSTANTIATE DEVICES #####
Buzzer = ModulinoBuzzer()
Display = LCD(0x27, 16, 2, i2c=I2C(1))
Knob = ModulinoKnob()
Movement = ModulinoMovement()

##### SETUP DEVICES #####
Display.begin()
Knob.range = (0, 30)

##### GLOBAL VARIABLES #####
player1_score = 0
player2_score = 0


def wait_for_continue():
    while True:
        Knob.update()
        if Knob.pressed:
            break
        sleep(0.1)


def display_message(top, bottom):
    Display.clear()
    Display.set_cursor(0, 0)
    Display.print(top)
    Display.set_cursor(0, 1)
    Display.print(bottom)


def buzzer_play_melody():
    melody = [
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
    for note_name, duration in melody:
        note = Buzzer.NOTES[note_name]
        Buzzer.tone(note, duration, blocking=True)
        sleep(0.01)
    Buzzer.no_tone()


def welcome():
    display_message("  Welcome to   ", "==== REACTO ====")
    buzzer_play_melody()


def player_selection():
    global player_scores
    global player_count
    knob_value = 0

    def increase():
        global player_count
        player_count += 1
        if player_count > 6:
            player_count = 6

    def decrease():
        global player_count
        player_count -= 1
        if player_count < 1:
            player_count = 1

    Display.clear()
    Display.set_cursor(0, 0)
    Display.print("Player count:")
    while True:
        Knob.update()
        if Knob.value > knob_value:
            increase()
        elif Knob.value < knob_value:
            decrease()
        Display.set_cursor(0, 1)
        Display.print(str(player_count))
        knob_value = Knob.value
        if Knob.pressed:
            break
        sleep(0.1)


def hide_and_seek():
    global player1_score
    global player2_score
    display_message("Hide and Seek", "Press to start")
    wait_for_continue()
    display_message("Player 1 ready?", "Press to proceed")
    wait_for_continue()
    for time in range(10):
        display_message("Hide REACTO!", f"Time left: {str(9-time)}")
        sleep(1)
    buzzer_play_melody()
    display_message("Waiting...", "Press when found")
    wait_for_continue()
    display_message("Player 2 ready?", "Press to proceed")
    wait_for_continue()
    for time in range(10):
        display_message("Hide REACTO!", f"Time left: {str(9-time)}")
        sleep(1)
    buzzer_play_melody()
    display_message("Waiting...", "Press when found")
    wait_for_continue()
    display_message("Game finished!", "Press to proceed")
    wait_for_continue()


def speed_it_up():
    global player1_score
    global player2_score
    values1 = []
    values2 = []
    display_message("Speed it up", "Press to start")
    wait_for_continue()
    display_message("Player 1 ready?", "Press to proceed")
    wait_for_continue()
    display_message("Shake as hard", "as you can!")
    for _ in range(1000):
        values1.append(
            sqrt(
                Movement.accelerometer.x**2
                + Movement.accelerometer.y**2
                + Movement.accelerometer.z**2
            )
        )
        player1_score += max(values1)
        sleep(0.01)
    display_message("Player 2 ready?", "Press to proceed")
    wait_for_continue()
    display_message("Shake as hard", "as you can!")
    for _ in range(1000):
        values2.append(
            sqrt(
                Movement.accelerometer.x**2
                + Movement.accelerometer.y**2
                + Movement.accelerometer.z**2
            )
        )
        player2_score += max(values2)
        sleep(0.01)
    display_message("Game finished!", "Press to proceed")
    wait_for_continue()


def time_guess():
    global player1_score
    global player2_score
    display_message("Time guess", "Press to start")
    wait_for_continue()
    display_message("Player 1 ready?", "Press to proceed")
    wait_for_continue()
    time1 = randint(1, 9)
    display_message(f"Press in {str(time1)}s", "Press to proceed")
    guess1 = 0
    while True:
        Knob.update()
        guess1 += 0.01
        if Knob.pressed():
            break
        sleep(0.01)
    player1_score += abs(guess1 - time1)
    display_message("Player 2 ready?", "Press to proceed")
    wait_for_continue()
    time2 = randint(1, 9)
    display_message(f"Press in {str(time1)}s", "Press to proceed")
    guess2 = 0
    while True:
        Knob.update()
        guess2 += 0.01
        if Knob.pressed():
            break
        sleep(0.01)
    player2_score += abs(guess2 - time2)
    display_message("Game finished!", "Press to proceed")
    wait_for_continue()


def hot_potato():
    global player1_score
    global player2_score


def results():
    global player1_score
    global player2_score
    if player1_score > player2_score:
        display_message("Player 1 won!", f"Score: {str(player1_score)}")
    elif player1_score < player2_score:
        display_message("Player 2 won!", f"Score: {str(player2_score)}")
    else:
        display_message("Draw!", "")


def main():
    welcome()
    sleep(5)
    # player_selection()
    hide_and_seek()
    speed_it_up()
    time_guess()
    # hot_potato()
    results()


main()
