import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

class MyGUI:
    CardPlayed = ();
    MovesSelected = "";
    CardToShow1 = [];
    CardToShow2 = [];
    all_sets = [];
    def __init__(self, root):
        #setting title
        root.title("Concerto")
        #setting window size
        width1=1055;
        height1=725;
        screenwidth = root.winfo_screenwidth();
        screenheight = root.winfo_screenheight();
        alignstr = '%dx%d+%d+%d' % (width1, height1, (screenwidth - width1) / 2, (screenheight - height1) / 2);
        root.geometry(alignstr);
        root.resizable(width=False, height=False)

        def GameStart():
            self.StartGameBtn["state"]=tk.DISABLED;
            root.quit()

        #Add frame to display name and dealer options
        self.GameOptions=tk.LabelFrame(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GameOptions["font"] = ft
        self.GameOptions["text"] = "Game options"
        self.GameOptions["height"] = 350
        self.GameOptions["width"] = 360
        self.StartGameBtn = tk.Button(
                self.GameOptions,
                text="Start game",
                background="#D6C2C2",
                command=GameStart
            )
        self.StartGameBtn.grid(row=6,column=2)
        
        #Add console message box
        #Add frame to display message box
        self.MessageBox=tk.LabelFrame(root)
        self.MessageBox["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        self.MessageBox["font"] = ft
        self.MessageBox["fg"] = "#333333"
        self.MessageBox["text"] = "Console box"
        self.MessageBox["height"] = 395
        self.MessageBox["width"] = 260

        self.ConsoleBox =tk.Text(self.MessageBox)
        ft = tkFont.Font(family='Times',size=10)
        self.ConsoleBox["font"] = ft
        self.ConsoleBox.grid(row=0,column=0)
        self.ConsoleBox["state"] = tk.NORMAL
        self.ConsoleBox["background"] = "#90ee90"
        self.ConsoleBox["wrap"] = "word"

        self.MessageBox.grid(row=1,column=3,rowspan=2,sticky="W")
        self.MessageBox.grid_propagate(0)
        v=tk.Scrollbar(root,background="black",orient="vertical", command=self.ConsoleBox.yview)
        v.grid(row=1,column=4,rowspan=2,sticky="E")
        self.ConsoleBox['yscrollcommand'] = v.set
        
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

        # Add frame to display moves
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

        #To add game options
        self.player_labels = []
        self.player_entries = []
        for i in range(4):
            player_label = tk.Label(self.GameOptions, text=f"Player {i+1}:")
            # player_label.grid(row=i, column=3, padx=35, pady=5)
            player_label.grid(row=i, column=1,sticky="SE")
            #player_label.config(background="green",fg="white",font=("Arial", 14))
            self.player_labels.append(player_label)
            player_entry = tk.Entry(self.GameOptions)
            player_entry.grid(row=i, column=2, padx=5, pady=5,sticky="E",columnspan="3")
            self.player_entries.append(player_entry)           
        # create a label for the radio buttons
        self.dealer_label = tk.Label(self.GameOptions, text="Select the dealer:")
        # self.dealer_label.grid(row=0, column=0, padx=25, pady=5)
        self.dealer_label.grid(row=0, column=0)

        self.dealer_var = tk.StringVar()
        self.dealer_radios = []
        for i in range(4):
            dealer_radio = tk.Radiobutton(self.GameOptions, text=f"Player {i+1}", variable=self.dealer_var, value=f"Player {i+1}", command=self.assign_teams)
            dealer_radio.grid(row=i+1, column=0, padx=5, pady=5)
            self.dealer_radios.append(dealer_radio)
            # create a label for the team assignments
        self.GameOptions.grid(row=0,column=2,sticky="W",columnspan=2)
        self.GameOptions.grid_propagate(0)
        # create a label for the team assignments
        self.team_label = tk.Label(self.GameOptions, text="")
        self.team_label.grid(row=5, column=0, columnspan=5, padx=5, pady=5)

    def assign_teams(self):
        # get the names of the players
        player_names = [entry.get() for entry in self.player_entries]
        # get the selected dealer
        dealer = self.dealer_var.get()
        # check if a dealer has been selected
        if dealer:
            # check if all player names have been entered
            if all(player_names):
                # assign teams based on the selected dealer
                dealer_position = int(dealer.split(" ")[1]) - 1
                dealer_name = dealer.split(" ")[0]
                non_dealer_positions = [(dealer_position + i) % 4 for i in [1, 3]]
                non_dealing_team = [player_names[i] for i in non_dealer_positions]
                dealing_team = [p for p in player_names if p not in non_dealing_team]
                dealing_team.append(dealer_name)
                # update the team label with the assigned teams
                message = f"Dealing Team: {dealing_team[0]} and {dealing_team[1]}\nNon-Dealing Team: {non_dealing_team[0]} and {non_dealing_team[1]}"
                self.team_label.config(text=message,bg="green",fg="white")
            else:
                # display an error message if not all player names have been entered
                self.team_label.config(text="Please enter names for all players.")
        else:
            # display an error message if no dealer has been selected
            self.team_label.config(text="Please select a dealer.")
 
    # @staticmethod
    # def StartBtn_command(gui):
    #     # if(StartGameBtn["state"] == "disabled"):
    #         # game = Game();
    #         # game.StartGame(gui);
    #         pass;
    
    def WriteToConsole(self,text):
        self.ConsoleBox.insert(tk.END, text)
        self.ConsoleBox.see(tk.END)
    
    def DisplayDeckAndMoves(self, cards, State,root):
        if self.DisplayMoves and self.DisplayDeck is not None:
            self.DisplayDeck.destroy();
            self.DisplayMoves.destroy();

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
        self.DisplayDeck.grid_propagate(0)

        # Create variable to hold selected card
        selected_card = tk.StringVar()
        move_var = tk.StringVar()
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
            root.quit()   

        def submit_moves():
            self.MovesSelected = move_var.get();
            root.quit()

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
                background="#D6C2C2",
                command=submit_cards
            )
            self.SubmitCard.grid(row=1, column=6)

        #To add options to pass, play or force
        self.move_var = tk.StringVar()
        # self.move_var.set("play")
        self.play_radio = tk.Radiobutton(self.DisplayMoves, text="Play", variable=move_var, value="Play")
        self.pass_radio = tk.Radiobutton(self.DisplayMoves, text="Pass", variable=move_var, value="Pass")
        self.force_radio = tk.Radiobutton(self.DisplayMoves, text="Force", variable=move_var, value="Force")
        self.SubmitMove = tk.Button(self.DisplayMoves, text="Submit", command=submit_moves,background="#D6C2C2")
        self.play_radio.grid(row=0,column=0, padx=5, pady=5)
        self.pass_radio.grid(row=0,column=1, padx=5, pady=5)
        self.force_radio.grid(row=0,column=2, padx=5, pady=5)
        self.SubmitMove.grid(row=0, column=3, padx=5, pady=5,columnspan=2,sticky="E")
        self.DisplayMoves.grid(row=2,column=0,sticky="NW",padx=2, pady=2,columnspan=3);
        self.DisplayMoves.grid_propagate(0)
       
       # To validate if the moves options should be displayed or not
        if(State == False):
            # Disable radio button and submit button
            self.play_radio["state"] = tk.DISABLED;
            self.pass_radio["state"] = tk.DISABLED;
            self.force_radio["state"] = tk.DISABLED;
            self.SubmitMove["state"] = tk.DISABLED;
            for rb in self.radiobuttons:
                rb.config(state=tk.NORMAL)
            self.SubmitCard["state"] = tk.NORMAL;
            self.DisplayDeck.wait_visibility()
            self.DisplayDeck.grab_set()
            self.DisplayDeck.mainloop()
        elif(State == True):
            # Enable radio button and submit button
            self.play_radio["state"] = tk.NORMAL;
            self.pass_radio["state"] = tk.NORMAL;
            self.force_radio["state"] = tk.NORMAL;
            self.SubmitMove["state"] = tk.NORMAL;
            for rb in self.radiobuttons:
                rb["state"] = tk.DISABLED
            self.SubmitCard["state"] = tk.DISABLED;
            self.DisplayMoves.wait_visibility()
            self.DisplayMoves.grab_set()
            self.DisplayMoves.mainloop()

        return self.CardPlayed,self.MovesSelected

    # Function to display the cards
    def DisplayCardsPlayed(self,CardsToDisplay,HandNo,root):
        if(HandNo%2 == 0):
            for x in CardsToDisplay:
                    if x not in self.CardToShow1:
                        self.CardToShow1.append(x);
            CardsToDisplay = self.CardToShow1;
        elif(HandNo%2!=0):
            for x in CardsToDisplay:
                    if x not in self.CardToShow2:
                        self.CardToShow2.append(x);
            CardsToDisplay = self.CardToShow2;
        if HandNo %2 == 0:
            self.DisplayCards=tk.LabelFrame(root)
            self.DisplayCards["bg"] = "#90ee90"
            ft = tkFont.Font(family='Times',size=10)
            self.DisplayCards["font"] = ft
            self.DisplayCards["fg"] = "#333333"
            self.DisplayCards["text"] = "Cards played"
            self.DisplayCards["height"] = 350
            self.DisplayCards["width"] = 300
            self.DisplayCards.grid(row=0,column=0,sticky="W")
            self.DisplayCards.grid_propagate(0)
            for i, card in enumerate(CardsToDisplay):
                image_path = f"cards/{card[0]}{card[1].upper()}.png"  # Convert suit to uppercase letter
                image = Image.open(image_path)
                image = image.resize((50, 75), Image.ANTIALIAS)  # Resize to fit frame
                card_image = ImageTk.PhotoImage(image)
                label = tk.Label(self.DisplayCards, image=card_image)
                label.image = card_image # save a reference to the image to avoid garbage collection
                label.grid(row=i//5, column=i%5, padx=2, pady=2)
        elif HandNo %2!= 0:
            self.DisplayCards1=tk.LabelFrame(root)
            self.DisplayCards1["bg"] = "#90ee90"
            ft = tkFont.Font(family='Times',size=10)
            self.DisplayCards1["font"] = ft
            self.DisplayCards1["fg"] = "#333333"
            self.DisplayCards1["text"] = "Cards played"
            self.DisplayCards1["height"] = 350
            self.DisplayCards1["width"] = 300
            self.DisplayCards1.grid(row=0,column=1,sticky="W")
            self.DisplayCards1.grid_propagate(0)
            for i, card in enumerate(CardsToDisplay):
                image_path = f"cards/{card[0]}{card[1].upper()}.png"  # Convert suit to uppercase letter
                print(image_path)
                image = Image.open(image_path)
                image = image.resize((50, 75), Image.ANTIALIAS)  # Resize to fit frame
                card_image = ImageTk.PhotoImage(image)
                label = tk.Label(self.DisplayCards1, image=card_image)
                label.image = card_image # save a reference to the image to avoid garbage collection
                label.grid(row=i//5, column=i%5, padx=2, pady=2)

# if __name__ == "__main__":
#     root = tk.Tk()
#     gui = MyGUI(root)
#     MyGUI.StartBtn_command(gui)
#     root.mainloop()


