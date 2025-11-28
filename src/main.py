# from Output import output
from Input import input
from timer import Timer

##### CONSTANTS #####
FREQUENCY = 60

def main():
    input.get_input()
    output.set_output()

execution_timer = Timer(1000/FREQUENCY, False)
execution_timer.on_timer_end = main()

while True:
    execution_timer.update()