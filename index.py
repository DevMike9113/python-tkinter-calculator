import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("320x400")
root.configure(bg="#333")

# Global variable to hold the display text
display_text = tk.StringVar()

# Update display function


def append(value):
    current_text = display_text.get()
    display_text.set(current_text + value)

# Clear display function


def clear_display():
    display_text.set("")

# Backspace function


def backspace():
    current_text = display_text.get()
    display_text.set(current_text[:-1])

# Calculate function


def calculate():
    try:
        # Evaluate the expression and update display
        result = eval(display_text.get())
        display_text.set(str(result))
    except:
        # Display 'Error' if calculation fails
        display_text.set("Error")


# Display field
display = tk.Entry(root, textvariable=display_text, font=(
    "Arial", 24), bg="#222", fg="white", borderwidth=0, relief="solid", justify="right")
display.grid(row=0, column=0, columnspan=4,
             padx=10, pady=20, ipadx=10, ipady=20)

# Button configurations
button_config = {
    "font": ("Arial", 18),
    "bg": "#444",
    "fg": "black",
    "activebackground": "#555",
    "width": 4,
    "height": 2,
    "borderwidth": 0,
    "relief": "solid"
}

# Create number and operator buttons
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0, 2), ("←", 5, 2, 2)
]

# Add buttons to the grid
for (text, row, col, *span) in buttons:
    action = (lambda value=text: append(value)) if text not in {
        "C", "=", "←"} else None
    cmd = clear_display if text == "C" else calculate if text == "=" else backspace if text == "←" else action
    width = 9 if text in {"C", "←"} else 4
    button = tk.Button(root, text=text, command=cmd, **button_config)
    button.config(width=width)
    button.grid(row=row, column=col,
                columnspan=span[0] if span else 1, padx=5, pady=5)

# Start the main loop
root.mainloop()
