from tkinter import *

# Font
small_font = ("arial", 16)
large_font = ("arial", 40)
digit_font = ("arial", 24)
default_font = ("arial", 20)

# Color
light_grey = "#F5F5F5"
lb_color = "#D4D4D2"
off_white = "#F5F5F5"  # Updated color name
operator_color = "#FF9500"
sp_black = "#1C1C1C"

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("300x600")
        self.window.resizable(0, 0)
        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()

        self.create_special_buttons()

        self.bind_keys()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_display_labels(self):
        total_label = Label(self.display_frame, text=self.total_expression, anchor=E, bg=off_white, fg=light_grey, padx=24, font=small_font)  # Updated color name
        total_label.pack(expand=True, fill="both")
        label = Label(self.display_frame, text=self.current_expression, anchor=E, bg=off_white, fg=light_grey, padx=24, font=large_font)  # Updated color name
        label.pack(expand=True, fill="both")
        return total_label, label

    def create_display_frame(self):
        frame = Frame(self.window, height=221, bg=off_white)  # Updated color name
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = Button(self.button_frame, text=str(digit), bg=off_white, fg=lb_color, font=digit_font, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))  # Updated color name
            button.grid(row=grid_value[0], column=grid_value[1], sticky=NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = Button(self.button_frame, text=symbol, bg=operator_color, fg=lb_color, font=default_font, borderwidth=0, command=lambda x=operator: self.append_operator(x))  # Updated color name
            button.grid(row=i, column=4, sticky=NSEW)
            i += 1

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_label()

    def create_clear_button(self):
        button = Button(self.button_frame, text="C", bg=sp_black, fg=lb_color, font=default_font, borderwidth=0, command=self.clear)  # Updated color name
        button.grid(row=0, column=1, sticky=NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = Button(self.button_frame, text="x²", bg=sp_black, fg=lb_color, font=default_font, borderwidth=0, command=self.square)  # Updated color name
        button.grid(row=0, column=2, sticky=NSEW)

    def sqrt(self):
        try:
            self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        except:
            self.current_expression = "Error"
        finally:
            self.update_label()

    def create_sqrt_button(self):
        button = Button(self.button_frame, text="√x", bg=sp_black, fg=lb_color, font=default_font, borderwidth=0, command=self.sqrt)  # Updated color name
        button.grid(row=0, column=3, sticky=NSEW)

    def evaluate(self):
        try:
            self.current_expression = str(eval(self.total_expression + self.current_expression))
        except:
            self.current_expression = "Error"
        finally:
            self.total_expression = ""
            self.update_total_label()
            self.update_label()

    def create_equals_button(self):
        button = Button(self.button_frame, text="=", bg=operator_color, fg=lb_color, font=default_font, borderwidth=0, command=self.evaluate)  # Updated color name
        button.grid(row=4, column=3, columnspan=2, sticky=NSEW)

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def build(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.build()
