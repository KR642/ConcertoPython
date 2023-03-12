# import tkinter as tk
# class people:
#     CardsReceived=[];
#     def __init__(self,CardsReceived):
#         self.CardsReceived = CardsReceived;
#     def enter(self):
#         ip = input("\npress enter");
#         return ip;

# class numbers:
#     c1 = ["12","13","12","14","15"];
#     c2 = ["1","2","3","4","5"];

# class deal:
#     def dealstart(self,p1,p2,gui):
#         i = 1;
#         while(i<=4):
#             hands = hand();
#             hands.play(p1,p2,gui);
#             i+=1;

# class hand:
    
#    def play(self, p1, p2, gui):
#         i = 1
#         while i <= 10:
#             if i % 2 == 0:
#                 p1.enter();
#                 gui.update_list_widget(p1.CardsReceived)
#             else:
#                 p2.enter();
#                 gui.update_list_widget(p2.CardsReceived)
#             i += 1
# class game:
#     def start(self):
#         c = numbers();
#         p1 = people(c.c1);
#         p2 = people(c.c2);
#         deals = deal();
#         gui = GUI();
#         deals.dealstart(p1,p2,gui);
#         gui.mainloop()

        

# class GUI:
    
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.title("My GUI")

#         self.list_widget = tk.Text(self.root, state=tk.DISABLED)
#         self.list_widget.pack()

#     def update_list_widget(self, values):
#         self.list_widget.config(state=tk.NORMAL)
#         self.list_widget.delete('1.0', tk.END)
#         for value in values:
#             self.list_widget.insert(tk.END, value + '\n')
#         self.list_widget.config(state=tk.DISABLED)

#     def mainloop(self):
#         self.root.mainloop()

    

# st = game();
# st.start();




# class MyGUI:
#     def __init__(self, master):
#         # Set up the main window
#         self.master = master
#         master.title("Card Game")
#         dealer_var = 1
#         # Create the frames
#         frame1 = tk.Frame(master)
#         frame2 = tk.Frame(master)
#         frame3 = tk.Frame(master)
#         frame4 = tk.Frame(master)
#         frame5 = tk.Frame(master)

#         # Place the frames using grid
#         frame1.grid(row=0, column=0)
#         frame2.grid(row=1, column=0)
#         frame3.grid(row=2, column=0)
#         frame4.grid(row=3, column=0)
#         frame5.grid(row=4, column=0)

#         # Create the widgets for each frame
#         played_cards_label = tk.Label(frame1, text="Played Cards", font=("Arial", 14))
#         played_cards_label.pack(padx=10, pady=10)

#         player_cards_label = tk.Label(frame2, text="Player Cards", font=("Arial", 14))
#         player_cards_label.pack(padx=10, pady=10)

#         player1_radiobutton = tk.Radiobutton(frame3, text="Player 1", variable=dealer_var, value="Player 1")
#         player2_radiobutton = tk.Radiobutton(frame3, text="Player 2", variable=dealer_var, value="Player 2")
#         player3_radiobutton = tk.Radiobutton(frame3, text="Player 3", variable=dealer_var, value="Player 3")
#         player4_radiobutton = tk.Radiobutton(frame3, text="Player 4", variable=dealer_var, value="Player 4")

#         player1_radiobutton.pack(padx=10, pady=5, anchor="w")
#         player2_radiobutton.pack(padx=10, pady=5, anchor="w")
#         player3_radiobutton.pack(padx=10, pady=5, anchor="w")
#         player4_radiobutton.pack(padx=10, pady=5, anchor="w")

#         player_name_label = tk.Label(frame4, text="Enter player names:", font=("Arial", 14))
#         player_name_label.pack(padx=10, pady=10)

#         player1_name_entry = tk.Entry(frame4)
#         player2_name_entry = tk.Entry(frame4)
#         player3_name_entry = tk.Entry(frame4)
#         player4_name_entry = tk.Entry(frame4)

#         player1_name_entry.pack(padx=10, pady=5)
#         player2_name_entry.pack(padx=10, pady=5)
#         player3_name_entry.pack(padx=10, pady=5)
#         player4_name_entry.pack(padx=10, pady=5)

#         start_button = tk.Button(frame5, text="Start Game", font=("Arial", 14))
#         start_button.pack(padx=10, pady=10)

#         message_label = tk.Label(frame5, text="Messages", font=("Arial", 14))
#         message_label.pack(padx=10, pady=10)

#         # Initialize the dealer variable
#         #dealer_var.set("Player 1")

#         # Pack the frames
#         frame1.pack(fill="both", expand=True)
#         frame2.pack(fill="both", expand=True)
#         frame3.pack(fill="both", expand=True)
#         frame4.pack(fill="both", expand=True)
#         frame5.pack(fill="both", expand=True)



# root = tk.Tk()
# my_gui = MyGUI(root)


# root.mainloop()

        #Add radio button to the code

        self.RadioBtn1=tk.Radiobutton(root,variable=dealer,value=1)
        ft = tkFont.Font(family='Times',size=10)
        self.RadioBtn1["font"] = ft
        self.RadioBtn1["fg"] = "#333333"
        self.RadioBtn1["justify"] = "center"
        self.RadioBtn1["text"] = "Player 1"
        # self.RadioBtn1.place()
        #self.RadioBtn1.place(x=480,y=30,width=85,height=25)
        #self.RadioBtn1["command"] = self.GRadio_197_command

        self.RadioBtn2=tk.Radiobutton(root,variable=dealer,value=2)
        ft = tkFont.Font(family='Times',size=10)
        self.RadioBtn2["font"] = ft
        self.RadioBtn2["fg"] = "#333333"
        self.RadioBtn2["justify"] = "center"
        self.RadioBtn2["text"] = "Player 2"
        # self.RadioBtn2.place()
        # self.RadioBtn2.place(x=480,y=60,width=85,height=25)
        #self.RadioBtn2["command"] = self.RadioBtn2_command

        self.RadioBtn3=tk.Radiobutton(root,variable=dealer,value=3)
        ft = tkFont.Font(family='Times',size=10)
        self.RadioBtn3["font"] = ft
        self.RadioBtn3["fg"] = "#333333"
        self.RadioBtn3["justify"] = "center"
        self.RadioBtn3["text"] = "Player 3"
        # self.RadioBtn3.place()
        #self.RadioBtn3.place(x=480,y=90,width=85,height=25)
        #self.RadioBtn3["command"] = self.RadioBtn3_command

        self.RadioBtn4=tk.Radiobutton(root,variable=dealer,value=4)
        ft = tkFont.Font(family='Times',size=10)
        self.RadioBtn4["font"] = ft
        self.RadioBtn4["fg"] = "#333333"
        self.RadioBtn4["justify"] = "center"
        self.RadioBtn4["text"] = "Player 4"
        # self.RadioBtn4.place()
        #self.RadioBtn4.place(x=480,y=120,width=85,height=25)
        #self.RadioBtn4["command"] = self.RadioBtn4_command

        #Add text inputs to the code

        self.Name1=tk.Entry(root)
        self.Name1["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.Name1["font"] = ft
        self.Name1["fg"] = "#333333"
        self.Name1["justify"] = "left"
        self.Name1["text"] = "Entry"
        #self.Name1.place(x=590,y=30,width=116,height=30)
        # self.Name1.place()

        self.Name2=tk.Entry(root)
        self.Name2["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.Name2["font"] = ft
        self.Name2["fg"] = "#333333"
        self.Name2["justify"] = "left"
        self.Name2["text"] = "Entry"
        #self.Name2.place(x=590,y=60,width=115,height=30)
        # self.Name2.place()

        self.Name3=tk.Entry(root)
        self.Name3["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.Name3["font"] = ft
        self.Name3["fg"] = "#333333"
        self.Name3["justify"] = "left"
        self.Name3["text"] = "Entry"
        # self.Name3.place(x=590,y=90,width=115,height=30)
        # self.Name3.place()

        self.Name4=tk.Entry(root)
        self.Name4["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.Name4["font"] = ft
        self.Name4["fg"] = "#333333"
        self.Name4["justify"] = "left"
        self.Name4["text"] = "Entry"
        # self.Name4.place(x=590,y=120,width=116,height=30)
        # self.Name4.place()