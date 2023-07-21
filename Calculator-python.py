import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def on_button_click(button_text):
    if button_text == "=":
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif button_text == "C":
        display_var.set("")
    else:
        display_var.set(display_var.get() + button_text)

# Create the main application window
app = tk.Tk()
app.title("Realistic Calculator")
app.geometry("300x400")

# Display area
display_var = tk.StringVar()
display_var.set("")
display = tk.Label(app, textvariable=display_var, font=("Helvetica", 20), anchor="e", relief="groove", width=15, height=2)
display.grid(row=0, column=0, columnspan=4, pady=10)

# Buttons
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

button_colors = {
    "/": "orange",
    "*": "orange",
    "-": "orange",
    "+": "orange",
    ".": "yellow",
    "=": "green",
    "C": "red"
}

for i in range(5):
    for j in range(4):
        index = i * 4 + j
        if index < len(button_texts):
            button_text = button_texts[index]
            bg_color = button_colors.get(button_text, "white")
            button = tk.Button(app, text=button_text, font=("Helvetica", 16), width=5, height=2, bg=bg_color,
                               command=lambda text=button_text: on_button_click(text))
            button.grid(row=i+1, column=j, padx=5, pady=5)

# Run the application
app.mainloop()
