# # from tkinter import *
# # from tkinter.ttk import *
   
# # # create root window
# # root = Tk()                          
 
# # # frame inside root window
# # frame = Frame(root)                 
 
# # # geometry method
# # frame.pack()                         
 
# # # button inside frame which is
# # # inside root
# # button = Button(frame, text ='Geek') 
# # button.pack()                        
 
# # # Tkinter event loop
# # root.mainloop()   
# # import tkinter as tk
# # from PIL import ImageTk, Image

# # card_images = {
# #     ('2', 'spades'): 'cards/2S.png',
# #     ('3', 'spades'): 'cards/3S.png',
# #     ('3', 'hearts'): 'cards/3H.png',
# #     ('5', 'diamonds'): 'cards/5D.png',
# #     ('k', 'spades'):'cards/KS.png'
# #     # Add more cards here...
# # }

# # card_images_tk = {}

# # def get_card_image(card):
# #     """Return a tkinter PhotoImage object for the given card."""
# #     if card not in card_images_tk:
# #         filename = card_images[card]
# #         image = Image.open(filename)
# #         card_images_tk[card] = ImageTk.PhotoImage(image)
# #     return card_images_tk[card]


# # root = tk.Tk()
# # root.title("Card Images")

# # cards = [('2', 'spades'),('3', 'spades'),('5', 'diamonds'),('3', 'hearts'),('k', 'spades')]

# # for i, card in enumerate(cards):
# #     image = get_card_image(card) # Width: 100, Height: 150

# #     label = tk.Label(root, image=image)
# #     label.grid(row=i, column=0)

# # root.mainloop()

# #Simport tkinter as tk

# root = tk.Tk()
# root.title("Select a Card")

# # Define a list of image file names
# card_images = [
#     "cards/AS.png",
#     "cards/2S.png",
#     "cards/3S.png",
#     "cards/4S.png",
#     "cards/5S.png",
#     "cards/6S.png",
#     "cards/7S.png",
#     "cards/8S.png",
#     "cards/9S.png",
#     "cards/10S.png",
#     "cards/JS.png",
#     "cards/QS.png",
#     "cards/KS.png"
# ]

# # Create a list to hold the images
# card_imgs = []

# # Load the images and append them to the card_imgs list
# for img_file in card_images:
#     img = tk.PhotoImage(file=img_file)
#     card_imgs.append(img)

# # Create a IntVar to hold the selected card
# selected_card = tk.IntVar()

# # Create a frame to hold the radio buttons
# frame = tk.Frame(root)
# frame.pack()

# # Create a radio button for each card image
# for i in range(13):
#     rb = tk.Radiobutton(frame, image=card_imgs[i], variable=selected_card, value=i)
#     rb.pack(side=tk.LEFT)

# root.mainloop()
