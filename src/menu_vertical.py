from io.devices import Display


class verticalMenu:
    def __init__(self, message, options):
        self.message = message
        self.options = options
        self.state = 0

    def show(self):
        Display.clear()
        Display.set_cursor(0, 0)
        Display.print(self.message)
        Display.set_cursor(0, 1)
        Display.print(f">{self.options[self.state]}")

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
