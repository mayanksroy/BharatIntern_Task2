import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature():
    try:
        value = float(entry_temperature.get())
        if radio_var.get() == 1:
            result = celsius_to_fahrenheit(value)
            result_label.config(text=f"{value:.2f}°C is equal to {result:.2f}°F")
        elif radio_var.get() == 2:
            result = fahrenheit_to_celsius(value)
            result_label.config(text=f"{value:.2f}°F is equal to {result:.2f}°C")
        else:
            result_label.config(text="Invalid choice. Please select a conversion type.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid temperature.")

app = tk.Tk()

app.title("Temperature Converter App")
app.geometry("500x400")
app.resizable(False, False)

header_label = tk.Label(app, text="Temperature Converter App", font=("Helvetica", 20, "bold"))
header_label.pack(pady=10)

entry_label = tk.Label(app, text="Enter temperature: ", font=("Helvetica", 14))
entry_label.pack()

entry_temperature = tk.Entry(app, font=("Helvetica", 14))
entry_temperature.pack()

radio_var = tk.IntVar()
radio_var.set(1)

radio_celsius_to_fahrenheit = ttk.Radiobutton(app, text="Celsius to Fahrenheit", variable=radio_var, value=1)
radio_celsius_to_fahrenheit.pack()

radio_fahrenheit_to_celsius = ttk.Radiobutton(app, text="Fahrenheit to Celsius", variable=radio_var, value=2)
radio_fahrenheit_to_celsius.pack()

convert_button = tk.Button(app, text="Convert", font=("Helvetica", 14), command=convert_temperature)
convert_button.pack(pady=10)

result_label = tk.Label(app, text="", font=("Helvetica", 14, "bold"))
result_label.pack()

app.mainloop()