import tkinter as tk

def create_gui():
    root = tk.Tk()
    root.title("My GUI")

    button = tk.Button(root, text="Click me", command=do_something)
    button.pack()

    root.mainloop()

def do_something():
    print("Button clicked")
    


def add_widgets():
    root = tk.Tk()

    create_gui()  # create the original GUI

    label = tk.Label(root, text="Enter your name:")
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    root.mainloop()

add_widgets()