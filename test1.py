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
# import tkinter as tk

# def create_gui():
#     root = tk.Tk()
#     root.title("My GUI")

#     button = tk.Button(root, text="Click me", command=do_something)
#     button.pack()

#     root.mainloop()

# def do_something():
#     print("Button clicked")
    
# import tkinter as tk
# from gui import create_gui, do_something

# def add_widgets():
#     root = tk.Tk()

#     create_gui()  # create the original GUI

#     label = tk.Label(root, text="Enter your name:")
#     label.pack()

#     entry = tk.Entry(root)
#     entry.pack()

#     root.mainloop()

# add_widgets()




import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from Game import Game
class MyGUI:
    CardPlayed = ();
    MovesSelected = "";
    def __init__(self, root):
        #setting title
        root.title("Concerto")
        #setting window size
        width1=1005
        height1=665
        dealer = tk.IntVar()  
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width1, height1, (screenwidth - width1) / 2, (screenheight - height1) / 2)
        root.geometry(alignstr)
        # root.resizable(width=False, height=False)
        #     
        #Add frame to display played cards -1
        self.DisplayCards=tk.LabelFrame(root)
        self.DisplayCards["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        self.DisplayCards["font"] = ft
        self.DisplayCards["fg"] = "#333333"
        self.DisplayCards["text"] = "Cards played"
        self.DisplayCards["height"] = 350
        self.DisplayCards["width"] = 300
        self.DisplayCards.grid(row=0,column=0,sticky="W")
        #Add frame to display played cards -2
        self.DisplayCards1=tk.LabelFrame(root)
        self.DisplayCards1["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        self.DisplayCards1["font"] = ft
        self.DisplayCards1["fg"] = "#333333"
        self.DisplayCards1["text"] = "Cards played"
        self.DisplayCards1["height"] = 350
        self.DisplayCards1["width"] = 300
        self.DisplayCards1.grid(row=0,column=1,sticky="W")
        #Add frame to display moves
        self.DisplayMoves=tk.LabelFrame(root);
        self.DisplayMoves["bg"] = "black"
        ft = tkFont.Font(family='Times',size=10)
        self.DisplayMoves["font"] = ft
        self.DisplayMoves["fg"] = "#fff"
        self.DisplayMoves["text"] = "Select a move"
        self.DisplayMoves["height"] = 145
        self.DisplayMoves["width"] = 780
        self.DisplayMoves.grid(row=2,column=0,sticky="NW",padx=2, pady=2,columnspan=3);

        #Add frame to display deck of the player
        self.DisplayDeck=tk.LabelFrame(root)
        self.DisplayDeck["bg"] = "green"
        ft = tkFont.Font(family='Times',size=10)
        self.DisplayDeck["font"] = ft
        self.DisplayDeck["fg"] = "#333333"
        self.DisplayDeck["text"] = "Your cards"
        self.DisplayDeck["height"] = 250
        self.DisplayDeck["width"] = 780
        self.DisplayDeck.grid(row=1,column=0,sticky="NW",columnspan=3);
    @staticmethod
    def StartBtn_command(gui):
        gui = gui;
        game = Game();
        game.StartGame(gui);
    
    def DisplayDeckAndMoves(self, cards, State):
        # Create variable to hold selected card
        selected_card = tk.StringVar()
        # Function to update selected card variable
        def select_card(card):
            #in card variable selected cards are stored
            #selected_card.set(card)
            pass;

        def submit_cards():
            self.CardPlayed = selected_card.get();
            input_list = self.CardPlayed.split()  # Split the string into a list of words
            input_tuple = (input_list[0], input_list[1])  # Create a tuple from the first two words
            self.CardPlayed = input_tuple;    

        def submit_moves():
            self.MovesSelected = self.move_var.get();

        self.radiobuttons = []
        # Create radio buttons for each card to display
        for i, card in enumerate(cards):
            image_path = f"cards/{card[0]}{card[1].upper()}.png"  # Convert suit to uppercase letter
            image = Image.open(image_path)
            image = image.resize((75, 100), Image.ANTIALIAS)  # Resize to fit frame
            card_image = ImageTk.PhotoImage(image)
            self.rb = tk.Radiobutton(self.DisplayDeck, image=card_image, variable=selected_card, value=card, command=lambda card=card: select_card(card))
            self.rb.image = card_image
            self.rb.grid(row=i//7, column=i%7, padx=5, pady=5)
            self.radiobuttons.append(self.rb)
            self.SubmitCard = tk.Button(
                self.DisplayDeck,
                text="Submit",
                command=submit_cards
            )
            self.SubmitCard.grid(row=1, column=6)
        # Pack label frame
        # self.DisplayDeck.grid(row=1,column=0,sticky="NW",columnspan=3);

        #To add options to pass, play or force
        self.move_var = tk.StringVar()
        # self.move_var.set("play")
        play_radio = tk.Radiobutton(self.DisplayMoves, text="Play", variable=self.move_var, value="Play")
        pass_radio = tk.Radiobutton(self.DisplayMoves, text="Pass", variable=self.move_var, value="Pass")
        force_radio = tk.Radiobutton(self.DisplayMoves, text="Force", variable=self.move_var, value="Force")
        SubmitMove = tk.Button(self.DisplayMoves, text="Submit", command=submit_moves)
        play_radio.grid(row=0,column=0, padx=5, pady=5)
        pass_radio.grid(row=0,column=1, padx=5, pady=5)
        force_radio.grid(row=0,column=2, padx=5, pady=5)
        SubmitMove.grid(row=0, column=3, padx=5, pady=5,columnspan=2,sticky="E")
        self.DisplayMoves.grid(row=2,column=0,sticky="NW",padx=2, pady=2,columnspan=3);
        self.DisplayMoves.grid_propagate(0)
       
       # To validate if the moves options should be displayed or not
        if(State == False):
            # Disable radio button and submit button
            play_radio["state"] = tk.DISABLED;
            pass_radio["state"] = tk.DISABLED;
            force_radio["state"] = tk.DISABLED;
            SubmitMove["state"] = tk.DISABLED;
            for rb in self.radiobuttons:
                rb.config(state=tk.NORMAL)
            self.SubmitCard["state"] = tk.NORMAL;

        elif(State == True):
            # Enable radio button and submit button
            play_radio["state"] = tk.NORMAL;
            pass_radio["state"] = tk.NORMAL;
            force_radio["state"] = tk.NORMAL;
            SubmitMove["state"] = tk.NORMAL;
            for rb in self.radiobuttons:
                rb["state"] = tk.DISABLED
            self.SubmitCard["state"] = tk.DISABLED;
        self.DisplayDeck.wait_visibility()
        self.DisplayDeck.grab_set()
        self.DisplayDeck.mainloop()
        return self.CardPlayed,self.MovesSelected

    def GetTheCard(self):
         return self.CardPlayed,self.MovesSelected;

    #Function to display the cards
    def DisplayCardsPlayed(self,CardsToDisplay):
        pass;


if __name__ == "__main__":
    root = tk.Tk()
    gui = MyGUI(root)
    MyGUI.StartBtn_command(gui)
    root.mainloop()


