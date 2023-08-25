import tkinter as tk

# creating the main window
root = tk.Tk()
root.title("My first GUI")
root.geometry("260x160")

def on_click():
    print("The button was clicked")

# creating a label widget
label = tk.Label(root, text = "Hello, world")
label.pack()

# create a button widget
button = tk.Button(root, text = "Click me")
button.config(command = on_click)
button.pack()

root.mainloop()