import random
from collections import Counter
class Card:
    # Generate 52 card decks
    def GenerateDeckAndShuffle(self):
        suits = ['diamonds', 'hearts', 'clubs', 'spades'];
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];
        # Initialize empty lists to store cards
        deck = [];
        # To generate 52 card deck
        for suit in suits:
            for rank in ranks:
                card = (rank, suit)    ;   
                deck.append(card);
        # To shuffle the deck randomly
        random.shuffle(deck);
        return deck;
    
    def DivideCards(self,deck):
        # Divide the deck into 4 parts with 13 cards each.
        deck1, deck2, deck3, deck4 = [], [], [], [];

        for i, card in enumerate(deck):
            if i < 13:
                deck1.append(card);
            elif i >= 13 and i < 26:
                deck2.append(card);
            elif i >= 26 and i < 39:
                deck3.append(card);
            else:
                deck4.append(card);
        return deck1, deck2, deck3, deck4;