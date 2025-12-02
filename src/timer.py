from machine import Timer


class Timer:
    def __init__(self, Display, message, time, callback):
        self.Display = Display
        self.message = message
        self.time = time
        self.callback = callback
        self.Timer = Timer(1)
    
    def on_timer_end(self):
        self.callback
    
    def interrupt(self):
        self.Timer.deinit()
        return self.time

    def show(self):
        self.Display.clear()
        self.Display.move(0, 0)
        self.Display.write(self.message)
        self.Display.move(0, 1)
        self.Display.write(f"{self.time}s")

    def update(self, timer):
        self.time -= 1
        self.show()
        if self.time is 0:
            self.Timer.deinit()
            self.on_timer_end()

    def start(self):
        self.Timer.init(mode=Timer.PERIODIC, period=1000, callback=self.update)
