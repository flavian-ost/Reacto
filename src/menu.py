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


class HorizontalMenu:
    def __init__(self, Display, message, option_left, option_right):
        self.Display = Display
        self.message = message
        self.option_left = option_left
        self.option_right = option_right
        self.state = option_left

    def show_left_selected(self):
        self.Display.clear()
        self.Display.move(0, 0)
        self.Display.write(self.message)
        self.Display.move(0, 1)
        self.Display.write(f">{self.option_left}")
        self.Display.move(8, 1)
        self.Display.write(f" {self.option_right}")

    def show_right_selected(self):
        self.Display.clear()
        self.Display.move(0, 0)
        self.Display.write(self.message)
        self.Display.move(0, 1)
        self.Display.write(f" {self.option_left}")
        self.Display.move(8, 1)
        self.Display.write(f">{self.option_right}")

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
