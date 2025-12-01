from machine import Timer


class Timer:
    def __init__(self, Display, message, time, callback):
        self.Display = Display
        self.message = message
        self.time = time
        self.callback = callback
        self.Timer = Timer(1)
    
    def on_timer_end(self, timer):
        self.callback

    def show(self):
        self.Display.clear()
        self.Display.set_cursor(0, 0)
        self.Display.print(self.message)
        self.Display.set_cursor(0, 0)
        self.Display.print(f"{self.time}s")

    def update(self, timer):
        self.time -= 1
        self.show()
        if self.time is 0:
            self.Timer.deinit()
            self.on_timer_end()

    def start(self):
        self.Timer.init(mode=Timer.PERIODIC, period=1000, callback=self.update)
