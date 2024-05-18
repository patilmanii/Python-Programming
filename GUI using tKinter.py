import tkinter as tk
from tkinter import messagebox

# Function to display a message box
def show_message():
    messagebox.showinfo("Message", "Hello, Tkinter!")

# Create the main window
root = tk.Tk()
root.title("Tkinter Demo")

# Create a button widget
button = tk.Button(root, text="Click Me", command=show_message)
button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
