# import tkinter as tk

# class App:
#     def __init__(self, master):
#         self.master = master
#         master.title("Select a Color")

#         self.color = tk.StringVar()

#         self.rb_red = tk.Radiobutton(master, text="Red", variable=self.color, value="red", command=self.update_color)
#         self.rb_red.pack()

#         self.rb_green = tk.Radiobutton(master, text="Green", variable=self.color, value="green", command=self.update_color)
#         self.rb_green.pack()

#         self.rb_blue = tk.Radiobutton(master, text="Blue", variable=self.color, value="blue", command=self.update_color)
#         self.rb_blue.pack()

#         self.label = tk.Label(master, text="Selected color: ")
#         self.label.pack()

#         self.label_2 = tk.Label(master, text="")
#         self.label_2.pack()

#         self.func_obj = Functionality()

#     def update_color(self):
#         self.label.config(text="Selected color: " + self.color.get())
#         result = self.func_obj.do_something(self.color.get())
#         self.label_2.config(text=result)

# class Functionality:
#     def do_something(self, color):
#         if color == "red":
#             result = "The color red signifies passion and energy."
#         elif color == "green":
#             result = "The color green is associated with nature and growth."
#         elif color == "blue":
#             result = "The color blue is often used to represent calmness and stability."
#         else:
#             result = "Please select a color."
#         return result

# root = tk.Tk()
# app = App(root)
# root.mainloop()

