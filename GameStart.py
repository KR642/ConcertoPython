import random
class Card:
    # Generate 52 card decks
    def GenerateDeckAndShuffle(self):
        suits = ['\u2666', '\u2665', '\u2663', '\u2660'];
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];
        # Initialize empty lists to store cards
        deck = []
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

class Team:
    TeamScore = "";
    TeamName = "";
    PlayersInTeam = [];
    
    # Constructor to initialize team name and players in team
    def __init__(self, TeamName, PlayersInTeam):
        self.TeamName = TeamName;
        self.PlayersInTeam = PlayersInTeam;

    # Function to add players to team
    def add_player(self, player):
        self.PlayersInTeam.append(player);

    # Function to identify leading and non leading players
    def IdentifyLeadAndNonLead(PlayersInTeam):
        #Returns leading and non leading players
        pass

class Player:
    name = "";
    id = "";
    CardsReceived = [];
    CardsPlayed = []; #Need a fn to store this cards played

    # Constructor to intialize player properties
    def __init__(self,name,id):
        self.name = name;
        self.id = id;
    
    # Receive respective cards
    def ReceiveCards(self,MyDeck):
        self.CardsReceived = MyDeck;

    # Show all cards except played cards
    def ShowCards(self):
        for i, card in enumerate(self.CardsReceived):
            # if(i == 1):
            #    print(f"{i}: {card}");
            # elif(i > 1):
            #     self.CardsPlayed[i] in self.CardsReceived
            #     continue;
            # else:
                print(f"{i}: {card}");

    # To play one card from the options
    def PlayCards(self):
        ChosenCard = input("\nEnter your card: ");
        for i, card in enumerate(self.CardsReceived):
            if str(i) == ChosenCard:
                ChosenCard = card;
                break
        self.CardsPlayed.append(ChosenCard);

    # To make a choice of pass/play/force
    def MakeAMove(self):
        move = input("\nEnter your choice of move - \n1: Play the card\n2: Pass the card\n3: Force the partner\n");
        if(move == "1"):
            move = "Play";
        elif(move == "2"):
            move = "Pass";
        elif(move == "3"):
            move = "Force";
        return move
    

class Deal:
    DealScores = "";
    DealLead = "";
    BonusPoints = "";
    # Bonus calculations and leftover processing happens here
    pass

class Hand:
    HandScore = "";
    TotalCards = 5;
    NoOfHands = 8;
    OnlyPlay = 0;
    TrackMoves = ["","","","",""];
    TrackCards = [];

    def PlayHands(self, LeadingPlayerObj, NonLeadingPlayerObj):
        self.ConsecutivePass = False;
        self.NextTurn = "";
        self.x = 1;
        while(self.x<=5):
            if(self.x == 1):
                print("\nLeading player is playing now:\n");
                LeadingPlayerObj.ShowCards();
                LeadingPlayerObj.PlayCards();
                self.TrackMoves[0]="Play";
                self.TrackCards.append("LeadingPlayer");
                self.NextTurn = "NonLeadingPlayer";
                self.x+=1;
            else:
                if(self.NextTurn == "NonLeadingPlayer"):
                    print("\nNonLeading player making a move now:\n")
                    move = NonLeadingPlayerObj.MakeAMove();
                    self.TrackMoves[self.x] = move;
                    self.ConsecutivePass = self.TrackMoves[self.x-2] == "Pass" and self.TrackMoves[self.x+1] == "Pass";
                    if(move == "Play"):
                            print("\nNonLeading player playing now:\n")
                            NonLeadingPlayerObj.ShowCards();
                            NonLeadingPlayerObj.PlayCards();
                            self.TrackCards.append("NonLeadingPlayer");
                            self.NextTurn = "LeadingPlayer";
                            self.x+=1;   
                    elif((move == "Pass") and self.ConsecutivePass != True):
                            print("\nLeading player making a move now:\n")
                            move = LeadingPlayerObj.MakeAMove();
                            self.TrackMoves[self.x] = move;
                            self.ConsecutivePass = self.TrackMoves[self.x] == "Pass" and self.TrackMoves[self.x+1] == "Pass";
                            if(move == "Pass" and self.ConsecutivePass != True):
                                print("\nNonLeading player is playing now:\n");
                                NonLeadingPlayerObj.ShowCards();
                                NonLeadingPlayerObj.PlayCards();
                                self.TrackCards.append("NonLeadingPlayer");
                                self.NextTurn = "LeadingPlayer";
                                self.x+=1;
                            elif(move == "Play"):
                                print("\nLeading player is playing now:\n");
                                LeadingPlayerObj.ShowCards();
                                LeadingPlayerObj.PlayCards();
                                self.TrackCards.append("LeadingPlayer");
                                self.NextTurn = "NonLeadingPlayer";
                                self.x+=1;
                            elif(move == "Force"):
                                pass;
                                # write a loop to play rest of the cards of non leading player
                                # NonLeadingPlayerObj.ShowCards();
                                # NonLeadingPlayerObj.CardsPlayed.extend(NonLeadingPlayerObj.CardsReceived);
                                # write a loop to play rest of the cards of non leading player
                elif(self.NextTurn == "LeadingPlayer"):
                    print("\nLeading player is making a move now:\n");
                    move = LeadingPlayerObj.MakeAMove();
                    self.TrackMoves[self.x] = move;
                    self.ConsecutivePass = self.TrackMoves[self.x] == "Pass" and self.TrackMoves[self.x+1] == "Pass";
                    if(move == "Play"):
                            print("\nLeading player is playing now:\n");
                            LeadingPlayerObj.ShowCards();
                            LeadingPlayerObj.PlayCards();
                            self.TrackCards.append("NonLeadingPlayer");
                            self.NextTurn = "NonLeadingPlayer";
                            self.x+=1;   
                    elif((move == "Pass") and self.ConsecutivePass != True):
                            print("\nNonLeading player is making a move now:\n");
                            move = NonLeadingPlayerObj.MakeAMove();
                            self.TrackMoves[self.x] = move;
                            self.ConsecutivePass = self.TrackMoves[self.x] == "Pass" and self.TrackMoves[self.x+1] == "Pass";
                            if(move == "Pass" and self.ConsecutivePass != True):
                                print("\nLeading player is playing now:\n");
                                LeadingPlayerObj.ShowCards();
                                LeadingPlayerObj.PlayCards();
                                self.TrackCards.append("NonLeadingPlayer");
                                self.NextTurn = "NonLeadingPlayer";
                                self.x+=1;
                            elif(move == "Play"):
                                print("\nNonLeading player is playing now:\n");
                                NonLeadingPlayerObj.ShowCards();
                                NonLeadingPlayerObj.PlayCards();
                                self.TrackCards.append("LeadingPlayer");
                                self.NextTurn = "LeadingPlayer";
                                self.x+=1;
                            elif(move == "Force"):
                                pass;
                                # write a loop to play rest of the cards of non leading player
                                # NonLeadingPlayerObj.ShowCards();
                                # NonLeadingPlayerObj.CardsPlayed.extend(NonLeadingPlayerObj.CardsReceived);
                                # write a loop to play rest of the cards of non leading player
                    

        #Get choice from the player 1
        #Store the choice of first card
        #Give options of pass,play,force
        pass
    pass
    
class Game:
    def StartGame(self):
        print("Concerto game starts: \n");
        # 4 Player object created
        player1 = Player("North","1");
        player2 = Player("East","2");
        player3 = Player("South","3");
        player4 = Player("West","4");

        # Assign players to different teams
        NS = Team("NS",[]);
        EW = Team("EW",[]);
        NS.add_player(player1);
        NS.add_player(player3);
        EW.add_player(player2);
        EW.add_player(player4);
        

        card = Card();
        cards = [];
        cards = card.GenerateDeckAndShuffle();

            #Divide and allocate cards to 4 players
        deck1,deck2,deck3,deck4 = [],[],[],[];
        deck1,deck2,deck3,deck4 = card.DivideCards(cards);

            #Allocate cards to players after shuffling
        player1.ReceiveCards(deck1);
        player2.ReceiveCards(deck2);
        player3.ReceiveCards(deck3);
        player4.ReceiveCards(deck4);

        hand = Hand();
        hand.PlayHands(player1,player3);


game = Game();
game.StartGame();