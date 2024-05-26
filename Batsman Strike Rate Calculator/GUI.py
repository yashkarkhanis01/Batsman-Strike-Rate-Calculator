import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def calculate_strike_rate():
    try:
        name = name_var.get()
        runs = int(runs_var.get())
        balls = int(balls_var.get())
        avg = runs / balls
        strike_rate = avg * 100
        result_var.set(f"The strike rate of {name} is {strike_rate:.2f}")
    except ValueError:
        result_var.set("Please enter valid numbers for runs and balls")

# Create the main window
root = tk.Tk()
root.title("Batsman Strike Rate Calculator")

# Load and set the background image
bg_image = Image.open("background.jpeg")  # Replace with your background image path
bg_image = bg_image.resize((800, 600), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

# Create StringVar for input and output
name_var = tk.StringVar()
runs_var = tk.StringVar()
balls_var = tk.StringVar()
result_var = tk.StringVar()

# Create and place widgets on top of the background
input_frame = tk.Frame(root, bg='lightgrey', padx=10, pady=10)
input_frame.place(relx=0.5, rely=0.5, anchor='center')

tk.Label(input_frame, text="Enter the name of batsman:", font=('Arial', 14)).grid(row=0, column=0, pady=5)
name_entry = tk.Entry(input_frame, textvariable=name_var, font=('Arial', 14))
name_entry.grid(row=0, column=1, pady=5)

tk.Label(input_frame, text="Enter the runs scored by batsman:", font=('Arial', 14)).grid(row=1, column=0, pady=5)
runs_entry = tk.Entry(input_frame, textvariable=runs_var, font=('Arial', 14))
runs_entry.grid(row=1, column=1, pady=5)

tk.Label(input_frame, text="Enter the number of balls faced by batsman:", font=('Arial', 14)).grid(row=2, column=0, pady=5)
balls_entry = tk.Entry(input_frame, textvariable=balls_var, font=('Arial', 14))
balls_entry.grid(row=2, column=1, pady=5)

calculate_button = tk.Button(input_frame, text="Calculate Strike Rate", command=calculate_strike_rate, font=('Arial', 14))
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(input_frame, textvariable=result_var, font=('Arial', 14), bg="lightyellow", fg="black")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Set the size of the main window
root.geometry("800x600")

# Run the application
root.mainloop()
