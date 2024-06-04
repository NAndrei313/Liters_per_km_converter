# Import TK module as *
from tkinter import *


# Def a function to calculate input MPG to l/100KM.
def converted():
    miles_per_gallon = float(input_miles_per_gallon.get())
    result = round(235.21 / miles_per_gallon)
    calcul_result["text"] = result


# Create a window and give it a name.
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Create an entry box and set the position.
input_miles_per_gallon = Entry(width=7)
input_miles_per_gallon.get()
input_miles_per_gallon.grid(column=1, row=0)

# Create a label for text and set the position.
miles_per_gallon_label = Label(text="Miles per Gallon (US)", font=("Arial", 12,))
miles_per_gallon_label.config(padx=15, pady=15)
miles_per_gallon_label.grid(column=2, row=0)

# Create a label for text and set the position.
is_equal = Label(text="is equal to", font=("Arial", 12,))
is_equal.config(padx=15, pady=15)
is_equal.grid(column=0, row=1)

# Create a label for text and set the position.
calcul_result = Label(text="0", font=("Arial", 12,))
calcul_result.config(padx=15, pady=15)
calcul_result.grid(column=1, row=1)

# Create a label for text and set the position.
liter_km_label = Label(text="Liter per Km", font=("Arial", 12,))
liter_km_label.config(padx=15, pady=15)
liter_km_label.grid(column=2, row=1)

# Create a button and add a command.
calcul_button = Button(text="Calculate", command=converted, font=("Arial", 12,))
calcul_button.grid(column=1, row=2)

window.mainloop()
