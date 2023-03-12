# def find_best_hand(cards):
#     sorted_ranks = sorted([card[0] for card in cards], reverse=True)
#     rank_counts = {rank: sorted_ranks.count(rank) for rank in set(sorted_ranks)}
#     suits = [card[1] for card in cards]

#     # Check for a straight flush
#     if sorted_ranks == list(range(int(sorted_ranks[0]), int(sorted_ranks[0]) - 5, -1)) and len(set(suits)) == 1:
#         return cards

#     # Check for four of a kind
#     for rank, count in rank_counts.items():
#         if count == 4:
#             return [card for card in cards if card[0] == rank] + [card for card in cards if card[0] != rank][:1]

#     # Check for a full house
#     if sorted_ranks[0] == sorted_ranks[2] and sorted_ranks[3] == sorted_ranks[4]:
#         return [card for card in cards if card[0] == sorted_ranks[0]] + [card for card in cards if card[0] == sorted_ranks[3]]

#     # Check for a flush
#     if len(set(suits)) == 1:
#         return cards

#     # Check for a straight
#     if sorted_ranks == list(range(int(sorted_ranks[0]), int(sorted_ranks[0]) - 5, -1)):
#         return cards

#     # Check for three of a kind
#     for rank, count in rank_counts.items():
#         if count == 3:
#             return [card for card in cards if card[0] == rank] + [card for card in cards if card[0] != rank][:2]

#     # Check for two pairs
#     if len(rank_counts) == 3 and sorted(rank_counts.values()) == [1, 2, 2]:
#         second_pair_rank = [rank for rank, count in rank_counts.items() if count == 2 and rank != sorted_ranks[0]][0]
#         return [card for card in cards if card[0] == sorted_ranks[0]] + [card for card in cards if card[0] == second_pair_rank][:2] + [card for card in cards if card[0] != sorted_ranks[0] and card[0] != second_pair_rank][:1]

#     # Check for a pair
#     if len(rank_counts) >= 2 and 2 in rank_counts.values():
#         pair_rank = [rank for rank, count in rank_counts.items() if count == 2][0]
#         return [card for card in cards if card[0] == pair_rank][:2] + [card for card in cards if card[0] != pair_rank][:3]

#     # Return the highest cards
#     return cards[:5]


# cards = [('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'),('2','diamonds'),('6','hearts')];
# list = find_best_hand(cards);
# print(list);

# TrackCards = ['LeadingPlayer','NonLeadingPlayer','NonLeadingPlayer','LeadingPlayer','LeadingPlayer']




# import tkinter as tk

# def display_choice():
#     selection = v.get()
#     if selection == 1:
#         choice_label.config(text="You chose rock.")
#     elif selection == 2:
#         choice_label.config(text="You chose paper.")
#     elif selection == 3:
#         choice_label.config(text="You chose scissors.")

# root = tk.Tk()
# root.title("Rock Paper Scissors")

# # create radio buttons
# v = tk.IntVar()
# rock_button = tk.Radiobutton(root, text="Rock", variable=v, value=1)
# paper_button = tk.Radiobutton(root, text="Paper", variable=v, value=2)
# scissors_button = tk.Radiobutton(root, text="Scissors", variable=v, value=3)

# # create submit button
# submit_button = tk.Button(root, text="Submit", command=display_choice)

# # create label to display user's choice
# choice_label = tk.Label(root, text="")

# # pack widgets onto the screen
# rock_button.pack()
# paper_button.pack()
# scissors_button.pack()
# submit_button.pack()
# choice_label.pack()

# root.mainloop()





def Play():
    n = [];
    i = 1;
    while(i<=5):
        num = input("\nEnter a num\n");
        n.append(num);
        i+=1;
    return n
all_sets = []  # Define a global variable to store all sets

# def Show(n):
#     global all_sets  # Use the global variable

#     CardsToDisplay = n
#     n1 = []
#     for x in n:
#         if x not in n1:
#             n1.append(x)
#     CardsToDisplay = n1

#     # Divide the CardsToDisplay list into sets of 5 numbers
#     sets_of_5 = [CardsToDisplay[i:i+5] for i in range(0, len(CardsToDisplay), 5)]

#     # Combine the previous sets with the current set of 5 numbers
#     all_sets += sets_of_5

#     # Determine which sets of 5 numbers to display based on the iteration number
#     if i == 1:
#         CardsToShow = all_sets[0]
#     elif i == 2:
#         CardsToShow = all_sets[1]
#     elif i == 3:
#         CardsToShow = all_sets[0] + all_sets[2]
#     elif i == 4:
#         CardsToShow = all_sets[1] + all_sets[3]
#     elif i == 5:
#         CardsToShow = all_sets[0] + all_sets[2] + all_sets[4]
#     elif i == 6:
#         CardsToShow = all_sets[1] + all_sets[3] + all_sets[5]
#     elif i == 7:
#         CardsToShow = all_sets[0] + all_sets[2] + all_sets[4] + all_sets[6]
#     elif i == 8:
#         CardsToShow = all_sets[1] + all_sets[3] + all_sets[5] + all_sets[7]

#     length = len(CardsToDisplay)

#     print(CardsToShow)
#     print(length)

# # Call the Show function in a loop
# if __name__ == "__main__":
#     i = 1
#     while i <= 8:
#         n = Play()
#         Show(n)
#         i += 1



# def DisplayCardsPlayed(self, CardsToDisplay, HandNo):
#     # Add new cards to the list of cards to show
#     for x in CardsToDisplay:
#         if x not in self.CardToShow1:
#             self.CardToShow1.append(x)
#     CardsToDisplay = self.CardToShow1
#     length = len(CardsToDisplay)

#     # Divide the cards into sets of 5 cards each
#     sets_of_5 = [CardsToDisplay[i:i+5] for i in range(0, len(CardsToDisplay), 5)]

#     # Combine the previous sets with the current set of 5 cards
#     self.all_sets += sets_of_5

#     # Determine which sets of 5 cards to display based on the iteration number
#     set_index = (HandNo - 1) % 2
#     start_index = set_index * 5
#     end_index = (set_index + 1) * 5
#     CardsToShow2 = []
#     for i in range(start_index, end_index):
#         CardsToShow2 += self.all_sets[i]

#     # Create a new frame to display the cards in, alternating between two frames
#     if HandNo % 2 == 0:
#         if HandNo // 2 > len(self.display_frames):
#             # Create a new frame if this is the first time displaying cards for this set
#             new_frame = tk.LabelFrame(root, bg="#90ee90", font=("Times", 10), fg="#333333", text="Cards played",
#                                       height=350, width=300)
#             new_frame.grid(row=0, column=0, sticky="W")
#             new_frame.grid_propagate(0)
#             self.display_frames.append(new_frame)
#         frame_index = HandNo // 2 - 1
#         self.current_display_frame = self.display_frames[frame_index]
#     else:
#         if HandNo // 2 > len(self.display_frames):
#             # Create a new frame if this is the first time displaying cards for this set
#             new_frame = tk.LabelFrame(root, bg="#90ee90", font=("Times", 10), fg="#333333", text="Cards played",
#                                       height=350, width=300)
#             new_frame.grid(row=0, column=1, sticky="W")
#             new_frame.grid_propagate(0)
#             self.display_frames.append(new_frame)
#         frame_index = HandNo // 2
#         self.current_display_frame = self.display_frames[frame_index]

#     # Clear the previous cards from the display frame
#     for widget in self.current_display_frame.winfo_children():
#         widget.destroy()

#     # Display the new cards in the display frame
#     for i, card in enumerate(CardsToShow2):
#         image_path = f"cards/{card[0]}{card[1].upper()}.png"
#         image = Image.open(image_path)
#         image = image.resize((50, 75), Image.ANTIALIAS)
#         card_image = ImageTk.PhotoImage(image)
#         label = tk.Label(self.current_display_frame, image=card_image)
#         label.image = card_image
#         label.grid(row=i // 5, column=i % 5, padx=2, pady=2)


def Show(n, previous_sets):
    CardsToDisplay = n
    n1 = []
    for x in n:
        if x not in n1:
            n1.append(x)
    CardsToDisplay = n1

    # Divide the CardsToDisplay list into sets of 5 numbers
    sets_of_5 = [CardsToDisplay[i:i+5] for i in range(0, len(CardsToDisplay), 5)]

    # Combine the previous sets with the current set of 5 numbers
    all_sets = previous_sets + sets_of_5

    # Determine which sets of 5 numbers to display based on the iteration number
    if i == 1:
        CardsToShow = all_sets[0]
    elif i == 2:
        CardsToShow = all_sets[1]
    elif i == 3:
        CardsToShow = all_sets[0] + all_sets[2]
    elif i == 4:
        CardsToShow = all_sets[1] + all_sets[3]
    elif i == 5:
        CardsToShow = all_sets[0] + all_sets[2] + all_sets[4]
    elif i == 6:
        CardsToShow = all_sets[1] + all_sets[3] + all_sets[5]
    elif i == 7:
        CardsToShow = all_sets[0] + all_sets[2] + all_sets[4] + all_sets[6]
    elif i == 8:
        CardsToShow = all_sets[1] + all_sets[3] + all_sets[5] + all_sets[7]

    length = len(CardsToDisplay)

    print(CardsToShow)
    print(length)

    return all_sets


if __name__ == "__main__":
    all_sets = []
    i = 1
    while i <= 8:
        n = Play()
        all_sets = Show(n, all_sets)
        i += 1

