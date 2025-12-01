from io.devices import Display


class horizontalMenu:
    def __init__(self, message, option_left, option_right):
        self.message = message
        self.option_left = option_left
        self.option_right = option_right
        self.state = option_left

    def show_left_selected(self):
        Display.clear()
        Display.set_cursor(0, 0)
        Display.print(self.message)
        Display.set_cursor(0, 1)
        Display.print(f">{self.option_left}")
        Display.set_cursor(8, 1)
        Display.print(f" {self.option_right}")

    def show_right_selected(self):
        Display.clear()
        Display.set_cursor(0, 0)
        Display.print(self.message)
        Display.set_cursor(0, 1)
        Display.print(f" {self.option_left}")
        Display.set_cursor(8, 1)
        Display.print(f">{self.option_right}")

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
