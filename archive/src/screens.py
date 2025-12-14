from output_manager import Output


class PlayerSelection:
    def __init__(self, message="Player count:", min_players=1, max_players=6):
        self.min_players = min_players
        self.max_players = max_players
        self.message = message
        self.player_count = 1

    def show(self):
        Output.display_show_message(self.message, (0, 0))
        Output.display_show_message(str(self.player_count), (0, 1))

    def decrease(self):
        self.player_count -= 1
        if self.player_count < self.min_players:
            self.player_count = self.min_players
        self.show()

    def increase(self):
        self.player_count += 1
        if self.player_count > self.max_players:
            self.player_count = self.max_players
        self.show()

    def value(self):
        return self.player_count


class HorizontalMenu:
    def __init__(self, Display, message, option_left, option_right):
        self.Display = Display
        self.message = message
        self.option_left = option_left
        self.option_right = option_right
        self.state = option_left

    def show_left_selected(self):
        self.Display.clear()
        self.Display.set_cursor(0, 0)
        self.Display.print(self.message)
        self.Display.set_cursor(0, 1)
        self.Display.print(f">{self.option_left}")
        self.Display.set_cursor(8, 1)
        self.Display.print(f" {self.option_right}")

    def show_right_selected(self):
        self.Display.clear()
        self.Display.set_cursor(0, 0)
        self.Display.print(self.message)
        self.Display.set_cursor(0, 1)
        self.Display.print(f" {self.option_left}")
        self.Display.set_cursor(8, 1)
        self.Display.print(f">{self.option_right}")

    def show(self):
        self.show_left_selected

    def change_selection(self):
        if self.state is self.option_left:
            self.show_right_selected
            self.state = self.option_right
        else:
            self.show_left_selected
            self.state = self.option_left

    def get_current_selection(self):
        return self.state


class VerticalMenu:
    def __init__(self, Display, message, options):
        self.Display = Display
        self.message = message
        self.options = options
        self.state = 0

    def show(self):
        self.Display.clear()
        self.Display.set_cursor(0, 0)
        self.Display.print(self.message)
        self.Display.set_cursor(0, 1)
        self.Display.print(f">{self.options[self.state]}")

    def change_selection_up(self):
        self.state -= 1
        if self.state < 0:
            self.state = self.options.length()
        self.show()

    def change_selection_down(self):
        self.state += 1
        if self.state > self.options.length():
            self.state = 0
        self.show()

    def get_current_selection(self):
        return self.state


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
        self.Display.set_cursor(0, 0)
        self.Display.print(self.message)
        self.Display.set_cursor(0, 1)
        self.Display.print(f"{self.time}s")

    def update(self, timer):
        self.time -= 1
        self.show()
        if self.time is 0:
            self.Timer.deinit()
            self.on_timer_end()

    def start(self):
        self.Timer.init(mode=Timer.PERIODIC, period=1000, callback=self.update)


class Stopwatch:
    def __init__(self):
        self.time = 0
        self.Timer = Timer(2)

    def update(self, timer):
        self.time += 1

    def start(self):
        self.Timer.init(mode=Timer.PERIODIC, period=1, callback=self.update)

    def stop(self):
        self.Timer.deinit()
        return self.time
