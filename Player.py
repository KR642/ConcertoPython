class Player:
    name = "";
    id = "";
    CardsReceived = CardsReceivedOrg = [];
    CardsPlayed = []; #Need a fn to store this cards played
    RemainingOriginal = [];
    # Constructor to intialize player properties
    def __init__(self,name,id):
        self.name = name;
        self.id = id;
    
    # Receive respective cards
    def ReceiveCards(self,MyDeck):
        self.CardsReceived = MyDeck;
        self.CardsReceivedOrg = MyDeck;

    # Show all cards except played cards
    def ShowCards(self):
        self.RemainingOriginal = remaining_cards = [card for card in self.CardsReceived if card not in self.CardsPlayed];
        for i, (rank, suit) in enumerate(remaining_cards):
            if suit == 'spades':
                symbol = '♠'
            elif suit == 'diamonds':
                symbol = '♦'
            elif suit == 'hearts':
                symbol = '♥'
            elif suit == 'clubs':
                symbol = '♣'
            else:
                symbol = suit
            remaining_cards[i] = (rank, symbol)
        for i, card in enumerate(remaining_cards):
            print(f"{card}");

    # To play one card from the options
    def PlayCards(self):
        print("\nChoose your card:\n\nEnter rank and the suit");
        print("\nA K Q J 10 9 8 7 6 5 2");
        print("\nC = Clubs, D = Diamonds, H = Hearts, S = Spades");
        ChosenCardRank = input("\nEnter the rank: ").upper();
        ChosenCardSuit = input("\nEnter suit: ").upper();
        if(ChosenCardSuit == 'C'):
            ChosenCardSuit = "clubs";
        elif(ChosenCardSuit == 'D'):
            ChosenCardSuit = "diamonds";
        elif(ChosenCardSuit == 'H'):
            ChosenCardSuit = "hearts";
        elif(ChosenCardSuit == "S"):
            ChosenCardSuit = "spades";
        else:
            print("Error in selecting input, please try again");
        if ChosenCardRank not in ['A','K','J','10','9','8','7','6','5','4','3','2']:
            print("\nError in selecting input, please try again");
        card = (ChosenCardRank,ChosenCardSuit);
        if card in self.CardsReceived:
            self.CardsPlayed.append(card);
            self.CardsReceived.remove(card);
        else:
            print("\n You've entered a card that is not in your deck, please try again");
            exit;
        # for i, card in enumerate(self.CardsReceived):
        #     if str(i) == ChosenCard:
        #         ChosenCard = card;
        #         break
        # self.CardsPlayed.append(ChosenCard);
        return self.CardsPlayed;

    # To make a choice of pass/play/force
    def MakeAMove(self):
        move = input("\nEnter your choice of move : \n1: Play the card\n2: Pass the card\n3: Force the partner\n");
        if(move == "1"):
            move = "Play";
        elif(move == "2"):
            move = "Pass";
        elif(move == "3"):
            move = "Force";
        else:
            move = "Error";
        return move
    



  