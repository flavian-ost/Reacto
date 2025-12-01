from io.devices import Display
from machine import Timer


class Timer:
    def __init__(self, message, time):
        self.message = message
        self.time = time
        self.Timer = Timer()

    def on_timer_end(self, callback):
        callback

    def show(self):
        Display.clear()
        Display.set_cursor(0, 0)
        Display.print(self.message)
        Display.set_cursor(0, 0)
        Display.print(f"{self.time}s")

    def update(self, timer):
        self.time -=1
        self.show()
        if self.time is 0:
            self.Timer.deinit()
            self.on_timer_end()

    def start(self):
        self.Timer.init(
            mode=Timer.PERIODIC, period=1000, callback=self.update
        )
