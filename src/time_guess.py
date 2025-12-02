import random
from time import sleep

# -------------------------------------------------------------
# HIER DEINE INPUT/OUTPUT-KLASSEN EINBINDEN
# Beispiel:
# from my_io import Input, Output
# input_dev = Input()
# output_dev = Output()
# -------------------------------------------------------------

# -------------------------------------------------------------
# HIER ZEITFUNKTION EINBINDEN (von dir bereitgestellt)
# from your_time_module import current_time
#
# Erwartet wird: current_time() liefert Tuple (Y,M,D,h,m,s)
# -------------------------------------------------------------

def get_timestamp_ms():
    t = current_time(1)
    # Format: (year, month, day, hour, minute, second, weekday, yearday)
    millis = (t[3] * 3600 + t[4] * 60 + t[5]) * 1000
    return millis

def calculate_points(target, actual):
    diff = abs(actual - target)
    if diff >= 1.0:
        return 0
    score = 100 * (1 - diff)
    return round(score)

def time_guess_round():
    target_time = random.uniform(3, 10)
    target_time = round(target_time, 2)

    # -------------------------------------------------------------
    # OUTPUT: Zeige Zielzeit
    # output_dev.show_text(f"Ziel: {target_time:.2f} s")
    # -------------------------------------------------------------
    print(f"Zielzeit: {target_time:.2f} s")   # Fallback falls kein Output-System

    # -------------------------------------------------------------
    # INPUT: Warte auf START-Knopf
    # input_dev.wait_for_start()
    # -------------------------------------------------------------
    input("Press ENTER for START")           # Platzhalter

    start_ms = get_timestamp_ms()

    # -------------------------------------------------------------
    # INPUT: Warte auf STOP-Knopf
    # input_dev.wait_for_stop()
    # -------------------------------------------------------------
    input("Press ENTER for STOP")            # Platzhalter

    stop_ms = get_timestamp_ms()

    measured = (stop_ms - start_ms) / 1000.0
    measured_rounded = round(measured / 0.05) * 0.05
    points = calculate_points(target_time, measured_rounded)

    # -------------------------------------------------------------
    # OUTPUT: Ergebnis anzeigen
    # output_dev.show_result(target_time, measured_rounded, points)
    # -------------------------------------------------------------
    print("---------------------------")
    print(f"Zielzeit:     {target_time:.2f} s")
    print(f"Gemessen:     {measured_rounded:.2f} s")
    print(f"Punkte:       {points}")
    print("---------------------------")

    return target_time, measured_rounded, points

# -------------------------------------------------------------
# HAUPTSCHLEIFE DES SPIELS
# -------------------------------------------------------------
def main():
    print("Time Guess Game startet...")

    while True:
        time_guess_round()
        sleep(1)

# -------------------------------------------------------------
# START
# -------------------------------------------------------------
if __name__ == "__main__":
    main()