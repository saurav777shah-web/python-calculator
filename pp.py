import tkinter as tk
import math

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

color_light_gray = "#F5F5F5"
color_light_black = "#333333"
color_orange = "#FF9500"
color_white = "white"

# window
window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tk.Frame(window)

expression = ""

# display
label = tk.Label(frame, text="0", font=("Arial", 45),
                 background=color_light_black,
                 foreground=color_white,
                 anchor="e",
                 width=12)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

# function
def button_click(value):
    global expression

    if value == "AC":
        expression = ""
        label["text"] = "0"

    elif value == "=":
        try:
            expression = expression.replace("×", "*").replace("÷", "/")
            result = str(eval(expression))
            label["text"] = result
            expression = result
        except:
            label["text"] = "Error"
            expression = ""

    elif value == "√":
        try:
            result = str(math.sqrt(float(label["text"])))
            label["text"] = result
            expression = result
        except:
            label["text"] = "Error"

    elif value == "%":
        try:
            result = str(float(label["text"]) / 100)
            label["text"] = result
            expression = result
        except:
            label["text"] = "Error"

    elif value == "+/-":
        try:
            result = str(-float(label["text"]))
            label["text"] = result
            expression = result
        except:
            label["text"] = "Error"

    else:
        if label["text"] == "0":
            label["text"] = value
        else:
            label["text"] += value

        expression += value


# buttons
for row in range(row_count):
    for column in range(column_count):

        value = button_values[row][column]

        button = tk.Button(frame,
                           text=value,
                           font=("Arial", 30),
                           width=4,
                           height=1,
                           command=lambda value=value: button_click(value))

        button.grid(row=row+1, column=column, padx=3, pady=3)

frame.pack()

window.mainloop()