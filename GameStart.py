import random
from collections import Counter
class Card:
    # Generate 52 card decks
    def GenerateDeckAndShuffle(self):
        suits = ['diamonds', 'hearts', 'clubs', 'spades'];
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"];
        # Initialize empty CardsPlayings to store cards
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

class Team:
    TeamScore = [];
    TeamName = "";
    PlayersInTeam = [];
    
    # Constructor to initialize team name and players in team
    def __init__(self, TeamName, PlayersInTeam,TeamScore):
        self.TeamName = TeamName;
        self.PlayersInTeam = PlayersInTeam;
        self.TeamScore = TeamScore;
    # Function to add players to team
    def add_player(self, player):
        self.PlayersInTeam.append(player);

    # Function to identify leading and non leading players
    def IdentifyLeadAndNonLead(self,HandNo):
        self.HandNo = HandNo;
        #Returns leading and non leading players
        if (self.TeamName == "NS"):
            if (self.HandNo == 1):
                return self.PlayersInTeam[0],self.PlayersInTeam[1];
            elif (self.HandNo == 3):
                return self.PlayersInTeam[1],self.PlayersInTeam[0];
            elif (self.HandNo == 5):
                return self.PlayersInTeam[0],self.PlayersInTeam[1];
            elif (self.HandNo == 7):
                return self.PlayersInTeam[1],self.PlayersInTeam[0];
        elif (self.TeamName == "EW"):
            if (self.HandNo == 2):
                return self.PlayersInTeam[0],self.PlayersInTeam[1];
            elif (self.HandNo == 4):
                return self.PlayersInTeam[1],self.PlayersInTeam[0];
            elif (self.HandNo == 6):
                return self.PlayersInTeam[0],self.PlayersInTeam[1];
            elif (self.HandNo == 8):
                return self.PlayersInTeam[1],self.PlayersInTeam[0];

class Player:
    name = "";
    id = "";
    CardsReceived = CardsReceivedOrg = [];
    CardsPlayed = []; #Need a fn to store this cards played
    RemainingOriginal = [];
    # Constructor to intialize player properties
    def __init__(self,name,id,CardsPlayed):
        self.name = name;
        self.id = id;
        self.CardsPlayed = CardsPlayed;
    
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
        ChosenCardSuit = input("Enter suit: ").upper();
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
        if ChosenCardRank not in ['A','K','Q','J','10','9','8','7','6','5','4','3','2']:
            print("\nError in selecting input, please try again");
        card = (ChosenCardRank,ChosenCardSuit);
        if card in self.CardsReceived:
            self.CardsPlayed.append(card);
            self.CardsReceived.remove(card);
        else:
            print("\n You've entered a card that is not in your deck, please try again");
            exit;
        return self.CardsPlayed;
    
    # To show played cards
    def ShowCardPlaying(self):
        for i, (rank, suit) in enumerate(self.CardsPlayed):
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
            self.CardsPlayed[i] = (rank, symbol)
        print("\nCards Played:");
        for item in self.CardsPlayed:
            print(item[0], item[1], end="  ")
        print()
      

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
    

class Deal:
    TotalHands = 2;
    BonusPoints = "";
    TotalHandsPlayed = [];
    def StartDeal(self,NS,EW):
        i = 1;
        HandScore = 0;
        while(i <= self.TotalHands):
            self.TotalHandsPlayed.append(Hand([],[]));
            if(i % 2 != 0):
                #call function identifying leading and non leading players
                self.LeadingPlayer,self.NonLeadingPlayer = NS.IdentifyLeadAndNonLead(i);
                CardsPlayed, CardTrack = self.TotalHandsPlayed[i-1].PlayHands(self.LeadingPlayer,self.NonLeadingPlayer);
                HandScore = self.TotalHandsPlayed[i-1].CheckCombination(CardsPlayed,CardTrack);
                NS.TeamScore.append(HandScore);
                print("Scores of North-South");
                print(HandScore);
                print("\nEast-West team will be playing next:\n");
                i+=1;
            elif(i % 2 == 0):
                #call function identifying leading and non leading players
                self.LeadingPlayer,self.NonLeadingPlayer = EW.IdentifyLeadAndNonLead(i);
                CardsPlayed, CardTrack = self.TotalHandsPlayed[i-1].PlayHands(self.LeadingPlayer,self.NonLeadingPlayer);
                HandScore = self.TotalHandsPlayed[i-1].CheckCombination(CardsPlayed,CardTrack);
                EW.TeamScore.append(HandScore);
                print("Scores of East-West");
                print(HandScore);
                if(i!=8):
                    print("\nNorth-South team will be playing next:\n");
                else:
                    print("\nA deal is completed\n");
                i+=1;
    #To find best 5 cards from the leftover cards
    @staticmethod
    def BestFiveCard(CardsLeft):
        RankCounts = {}
        Suits = {}
        for card in CardsLeft:
            rank, suit = card
            RankCounts[rank] = RankCounts.get(rank, 0) + 1
            Suits[suit] = Suits.get(suit, 0) + 1
            
        SortedRanks = sorted(RankCounts.keys(), key=lambda x: RankCounts[x], reverse=True)

        # Check for a straight
        for i in range(len(SortedRanks) - 4):
            if int(SortedRanks[i]) - int(SortedRanks[i + 4]) == 4:
                StraightRank = SortedRanks[i:i + 5]
                return [card for card in CardsLeft if card[0] in StraightRank][:5]
        
        # Check for flush
        for suit, count in Suits.items():
            if count >= 5:
                FlushCardsLeft = [card for card in CardsLeft if card[1] == suit]
                FlushRanks = [card[0] for card in FlushCardsLeft]
                return [card for card in FlushCardsLeft if card[0] in sorted(FlushRanks, reverse=True)][:5]
        
        # Check for four of a kind
        if len(SortedRanks) >= 4 and RankCounts[SortedRanks[0]] == 4:
            FourRank = SortedRanks[0]
            return [card for card in CardsLeft if card[0] == FourRank][:4] + [card for card in CardsLeft if card[0] == SortedRanks[-1]][:1]

        # Check for a full house
        if len(SortedRanks) >= 3 and RankCounts[SortedRanks[0]] == 3 and RankCounts[SortedRanks[1]] == 2:
            ThreeRank = SortedRanks[0]
            TwoRank = SortedRanks[1]
            return [card for card in CardsLeft if card[0] == ThreeRank][:3] + [card for card in CardsLeft if card[0] == TwoRank][:2]
        
        # Check for three of a kind
        if len(SortedRanks) >= 3 and RankCounts[SortedRanks[0]] == 3:
            ThreeRank = SortedRanks[0]
            return [card for card in CardsLeft if card[0] == ThreeRank][:3] + [card for card in CardsLeft if card[0] == SortedRanks[-2]][:1] + [card for card in CardsLeft if card[0] == SortedRanks[-1]][:1]

        # Check for two pair
        if len(SortedRanks) >= 2 and RankCounts[SortedRanks[0]] == 2 and RankCounts[SortedRanks[1]] == 2:
            FirstPairRank = SortedRanks[0]
            SecondPairRank = SortedRanks[1]
            return [card for card in CardsLeft if card[0] == FirstPairRank][:2] + [card for card in CardsLeft if card[0] == SecondPairRank][:2] + [card for card in CardsLeft if card[0] == SortedRanks[-1]][:1]

        # Check for a pair
        if len(SortedRanks) >= 2 and RankCounts[SortedRanks[0]] == 2:
            PairRank = SortedRanks[0]
            return [card for card in CardsLeft if card[0] == PairRank][:2] + [card for card in CardsLeft if card[0] != PairRank][:3]

        # Return the highest CardsLeft
        return [card for card in CardsLeft if card[0] == SortedRanks[0]][:1] + [card for card in CardsLeft if card[0] == SortedRanks[1]][:1] + [card for card in CardsLeft if card[0] == SortedRanks[2]][:1] + [card for card in CardsLeft if card[0] == SortedRanks[3]][:1] + [card for card in CardsLeft if card[0] == SortedRanks[4]][:1]

    
    # Bonus calculations and leftover processing happens here
    def CalculateBonus(self,NS,EW):
        NSSumOfScores = EWSumOfScores = 0;
        # Find the total scores of teams
        NSSumOfScores = sum(NS.TeamScore);
        EWSumOfScores = sum(EW.TeamScore);
        cardsOrgEW = self.EWCardsLeft = EW.PlayersInTeam[0].CardsReceived + EW.PlayersInTeam[1].CardsReceived;
        cardsOrgNS = self.NSCardsLeft = NS.PlayersInTeam[0].CardsReceived + NS.PlayersInTeam[1].CardsReceived;
        print("\nBonus calculating..");
        # Find the leading team and getting the leftover cards accordingly
        TempHandObj = Hand([],[]);
        if(NSSumOfScores > EWSumOfScores):   
            # Display leftover cards
            print("North-South is leading with "+NSSumOfScores);
            print("Leftover cards of East-West");
            TempHandObj.DisplayCards(self.EWCardsLeft);

            #Find the best 5 cards among the leftover cards
            CardsPlaying = Deal.BestFiveCard(self.EWCardsLeft);
            t1Length = len(EW.PlayersInTeam[0].CardsReceived);
            t1 = ['LeadingPlayer']*t1Length;
            t2Length = len(EW.PlayersInTeam[1].CardsReceived);
            t2 = ['NonLeadingPlayer']*t2Length;
            TrackCards1 = t1+t2;
            indexes = []
            for i, item in enumerate(cardsOrgEW):
                if item in CardsPlaying:
                    indexes.append(i);
            TrackCards = [TrackCards1[i] for i in indexes];
            self.LeftoverScore =TempHandObj.CheckCombination(CardsPlaying,TrackCards);

            self.LeftoverScore = self.LeftoverScore * 10;
            EW.TeamScore.append(self.LeftoverScore);
            print("Bonus earned by North-South : "+self.LeftoverScore);
        elif(NSSumOfScores == EWSumOfScores):
            print("North-South is leading with "+NSSumOfScores);
            print("Leftover cards of East-West");
            # Display leftover cards
            TempHandObj.DisplayCards(self.EWCardsLeft);

            #Find the best 5 cards among the leftover cards
            CardsPlaying = Deal.BestFiveCard(self.EWCardsLeft);
            t1Length = len(EW.PlayersInTeam[0].CardsReceived);
            t1 = ['LeadingPlayer']*t1Length;
            t2Length = len(EW.PlayersInTeam[1].CardsReceived);
            t2 = ['NonLeadingPlayer']*t2Length;
            TrackCards1 = t1+t2;
            indexes = []
            for i, item in enumerate(cardsOrgEW):
                if item in CardsPlaying:
                    indexes.append(i);
            TrackCards = [TrackCards1[i] for i in indexes];
            self.LeftoverScore = TempHandObj.CheckCombination(CardsPlaying,TrackCards);
            self.LeftoverScore = self.LeftoverScore * 10;
            print("Bonus earned by North-South : "+self.LeftoverScore);
            EW.TeamScore.append(self.LeftoverScore);
        elif(EWSumOfScores > NSSumOfScores):
            print("East-West is leading with "+EWSumOfScores);
            print("Leftover cards of North-South");
            # Display leftover cards
            TempHandObj.DisplayCards(self.NSCardsLeft);

            #Find the best 5 cards among the leftover cards
            CardsPlaying = Deal.BestFiveCard(self.NSCardsLeft);
            t1Length = len(NS.PlayersInTeam[0].CardsReceived);
            t1 = ['LeadingPlayer']*t1Length;
            t2Length = len(NS.PlayersInTeam[1].CardsReceived);
            t2 = ['NonLeadingPlayer']*t2Length;
            TrackCards1 = t1+t2;
            indexes = []
            for i, item in enumerate(cardsOrgNS):
                if item in CardsPlaying:
                    indexes.append(i);
            TrackCards = [TrackCards1[i] for i in indexes];

            self.LeftoverScore = TempHandObj.CheckCombination(CardsPlaying,TrackCards);
            self.LeftoverScore = self.LeftoverScore * 10;
            print("Bonus earned by East-West : "+self.LeftoverScore);
            NS.TeamScore.append(self.LeftoverScore);
            


class Hand:
    HandScore = "";
    TotalCards = 5;
    TrackMoves = ["","","","","","","","","","","","",""];
    TrackCards = [];
    CardsPlaying = [];
    ScoreofHand = 0;

    def __init__(self,CardsPlaying,TrackCards):
        self.CardsPlaying = CardsPlaying;
        self.TrackCards = TrackCards;
        self.TrackMoves = ["","","","","","","","","","","","",""];
    
    @staticmethod
    def DisplayCards(CardsPlaying):
        print("\nCards played: \n")
        for i, (rank, suit) in enumerate(CardsPlaying):
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
            CardsPlaying[i] = (rank, symbol)
        for item in CardsPlaying:
            print(item[0], item[1], end="  ")
        print()
    
    # To play a hand with leading player and non leading player 
    def PlayHands(self, LeadingPlayerObj, NonLeadingPlayerObj):
        self.ConsecutivePass = False;
        self.NextTurn = "";
        self.x = 1; # The number of cards
        self.CardsPlaying = [];
        self.LeadingPlayerCards = [];
        self.NonLeadingPlayerCards = [];
        while(self.x<=self.TotalCards):
            if(self.x == 1):
                print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                LeadingPlayerObj.ShowCards();
                LeadingPlayerObj.PlayCards();
                self.CardsPlaying.append(LeadingPlayerObj.CardsPlayed[-1]);
                Hand.DisplayCards(self.CardsPlaying);
                self.TrackMoves[0]="Play";
                self.TrackCards.append("LeadingPlayer");
                self.NextTurn = "NonLeadingPlayer";
                self.x+=1;
            else:
                if(self.NextTurn == "NonLeadingPlayer"):
                    print("\nNon-Leading player "+NonLeadingPlayerObj.name+" making a move now:\n");
                    NonLeadingPlayerObj.ShowCards();
                    move = NonLeadingPlayerObj.MakeAMove();
                    self.TrackMoves[self.x] = move;
                    self.ConsecutivePass = self.TrackMoves[self.x-2] == "Pass" and self.TrackMoves[self.x+1] == "Pass";
                    if(move == "Play"):
                            print("\nNon-Leading player "+NonLeadingPlayerObj.name+" playing now:\n")
                            NonLeadingPlayerObj.PlayCards();
                            self.CardsPlaying.append(NonLeadingPlayerObj.CardsPlayed[-1]);
                            Hand.DisplayCards(self.CardsPlaying);
                            self.TrackCards.append("NonLeadingPlayer");
                            self.NextTurn = "LeadingPlayer";
                            self.x+=1;   
                    elif((move == "Pass") and self.ConsecutivePass != True):
                            print("\nLeading player "+LeadingPlayerObj.name+" making a move now:\n");
                            LeadingPlayerObj.ShowCards();
                            move = LeadingPlayerObj.MakeAMove();
                            self.TrackMoves[self.x] = move;
                            self.ConsecutivePass = self.TrackMoves[self.x] == "Pass" and self.TrackMoves[self.x+1] == "Pass";
                            if(move == "Pass" and self.ConsecutivePass != True):
                                print("\nNon-Leading player "+NonLeadingPlayerObj.name+" is playing now:\n");
                                NonLeadingPlayerObj.ShowCards();
                                NonLeadingPlayerObj.PlayCards();
                                self.CardsPlaying.append(NonLeadingPlayerObj.CardsPlayed[-1]);
                                Hand.DisplayCards(self.CardsPlaying);
                                self.TrackCards.append("NonLeadingPlayer");
                                self.NextTurn = "LeadingPlayer";
                                self.x+=1;
                            elif(move == "Play"):
                                print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                                LeadingPlayerObj.PlayCards();
                                self.CardsPlaying.append(LeadingPlayerObj.CardsPlayed[-1]);
                                Hand.DisplayCards(self.CardsPlaying);
                                self.TrackCards.append("LeadingPlayer");
                                self.NextTurn = "NonLeadingPlayer";
                                self.x+=1;
                            elif(move == "Force"):
                                print("\nNon-Leading player "+NonLeadingPlayerObj.name+" is playing now:\n");
                                self.CardsLeft = 5 - (self.x-1); #To find rest of the cards to be played
                                self.i = 1;
                                while(self.i<=self.CardsLeft):
                                    NonLeadingPlayerObj.ShowCards();
                                    NonLeadingPlayerObj.PlayCards();
                                    self.CardsPlaying.append(NonLeadingPlayerObj.CardsPlayed[-1]);
                                    Hand.DisplayCards(self.CardsPlaying);
                                    self.TrackCards.append("NonLeadingPlayer");
                                    self.i+=1;
                                break;
                    elif(move == "Force"):
                        print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                        self.CardsLeft = 5 - (self.x-1); #To find rest of the cards to be played
                        self.i = 1;
                        LeadingPlayerObj.ShowCards();
                        while(self.i<=self.CardsLeft):
                            LeadingPlayerObj.PlayCards();
                            self.CardsPlaying.append(LeadingPlayerObj.CardsPlayed[-1]);
                            Hand.DisplayCards(self.CardsPlaying);
                            self.TrackCards.append("LeadingPlayer");
                            self.i+=1;
                        break;
                    elif(move == "Error"):
                        print("Error in selecting option, please try again");

                elif(self.NextTurn == "LeadingPlayer"):
                    print("\nLeading player "+LeadingPlayerObj.name+" is making a move now:\n");
                    LeadingPlayerObj.ShowCards();
                    move = LeadingPlayerObj.MakeAMove();
                    self.TrackMoves[self.x] = move;
                    self.ConsecutivePass = self.TrackMoves[self.x] == "Pass" and self.TrackMoves[self.x+1] == "Pass";
                    if(move == "Play"):
                            print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                            LeadingPlayerObj.PlayCards();
                            self.CardsPlaying.append(LeadingPlayerObj.CardsPlayed[-1]);
                            Hand.DisplayCards(self.CardsPlaying);
                            self.TrackCards.append("LeadingPlayer");
                            self.NextTurn = "NonLeadingPlayer";
                            self.x+=1;   
                    elif((move == "Pass") and self.ConsecutivePass != True):
                            print("\nNon-Leading player "+NonLeadingPlayerObj.name+" is making a move now:\n");
                            NonLeadingPlayerObj.ShowCards();
                            move = NonLeadingPlayerObj.MakeAMove();
                            self.TrackMoves[self.x] = move;
                            self.ConsecutivePass = self.TrackMoves[self.x] == "Pass" and self.TrackMoves[self.x+1] == "Pass";
                            if(move == "Pass" and self.ConsecutivePass != True):
                                print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                                LeadingPlayerObj.ShowCards();
                                LeadingPlayerObj.PlayCards();
                                self.CardsPlaying.append(LeadingPlayerObj.CardsPlayed[-1]);
                                Hand.DisplayCards(self.CardsPlaying);
                                self.TrackCards.append("LeadingPlayer");
                                self.NextTurn = "NonLeadingPlayer";
                                self.x+=1;
                            elif(move == "Play"):
                                print("\nNon-Leading "+NonLeadingPlayerObj.name+" player is playing now:\n");
                                NonLeadingPlayerObj.PlayCards();
                                self.CardsPlaying.append(NonLeadingPlayerObj.CardsPlayed[-1]);
                                Hand.DisplayCards(self.CardsPlaying);
                                self.TrackCards.append("NonLeadingPlayer");
                                self.NextTurn = "LeadingPlayer";
                                self.x+=1;
                            elif(move == "Force"):
                                print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                                self.CardsLeft = 5 - (self.x-1); #To find rest of the cards to be played
                                self.i = 1;
                                while(self.i<=self.CardsLeft):
                                    LeadingPlayerObj.ShowCards();
                                    LeadingPlayerObj.PlayCards();
                                    self.CardsPlaying.append(LeadingPlayerObj.CardsPlayed[-1]);
                                    Hand.DisplayCards(self.CardsPlaying);
                                    self.TrackCards.append("LeadingPlayer");
                                    self.i+=1;
                                break;
                    elif(move == "Force"):
                        print("\nNon-Leading player "+NonLeadingPlayerObj.name+" is playing now:\n");
                        self.CardsLeft = 5 - (self.x-1); #To find rest of the cards to be played
                        self.i = 1;
                        while(self.i<=self.CardsLeft):
                            NonLeadingPlayerObj.ShowCards();
                            NonLeadingPlayerObj.PlayCards();
                            self.CardsPlaying.append(NonLeadingPlayerObj.CardsPlayed[-1]);
                            Hand.DisplayCards(self.CardsPlaying);
                            self.TrackCards.append("NonLeadingPlayer");
                            self.i+=1;
                        break;
                    elif(move == "Error"):
                        print("Error in selecting option, please try again");
        return self.CardsPlaying,self.TrackCards;

    def CheckCombination(self,CardsPlaying,TrackCards):
        ScoreofHand = 0;
        #Check for poker combination code and returns scores
        values = [card[0] for card in CardsPlaying]
        suits = [h[1] for h in CardsPlaying]
        value_counts = Counter(values)
        # convert face cards to their integer values for comparison
        for i in range(len(values)) :
            if values[i] == "T":
                values[i] = 10
            elif values[i] == "J":
                values[i] = 11
            elif values[i] == "Q":
                values[i] = 12
            elif values[i] == "K":
                values[i] = 13
            elif values[i] == "A":
                values[i] = 14
        values = [int(value) for value in values]
        values.sort()
        #for straight
        is_straight = False
        for i in range(len(values) - 4):
            if values[i + 4] == values[i + 3] + 1 and values[i + 3] == values[i + 2] + 1 and values[i + 2] == values[i + 1] + 1 and values[i + 1] == values[i] + 1:
                is_straight = True
                break
        if not is_straight:
            if values == [2, 3, 4, 5, 14]:
                is_straight = True
        #for  straight_flush
        is_flush = len(set(suits)) == 1
        #for full house
        three_of_a_kind = False
        two_of_a_kind = False
        for count in value_counts.values():
            if count == 3:
                three_of_a_kind = True
            elif count == 2:
                two_of_a_kind = True  
        #check full house
        if three_of_a_kind and two_of_a_kind:
            print("\nFull House combination found!");
            ScoreofHand = 8;
            return ScoreofHand;
        # check for straight flush
        if is_straight and is_flush:
            print("\nStraight Flush combination found!");
            player_counts = {'LeadingPlayer': 0, 'NonLeadingPlayer': 0}
            for player in TrackCards:
                player_counts[player] += 1
                
                leading_player_count = player_counts['LeadingPlayer']
                non_leading_player_count = player_counts['NonLeadingPlayer']
                
                if leading_player_count == 5 or non_leading_player_count == 5:
                    ScoreofHand = 10;
                elif leading_player_count == 4 or non_leading_player_count == 4:
                    ScoreofHand = 15;
                elif leading_player_count == 3 or non_leading_player_count == 3:
                    ScoreofHand = 20;
                else:
                    ScoreofHand = 0;
            return ScoreofHand;
        #check for flush
        elif len(set(suits)) == 1:
            print("\nFlush combination found!");
            ScoreofHand = 6;
            return ScoreofHand;
        # Check for fours
        if max(value_counts.values()) == 4:
            print("\nFours combination found!");
            #To find card contribution of players and assign correct scores
            leading_player_count = 0
            non_leading_player_count = 0
            for i in range(len(CardsPlaying)):
                if CardsPlaying[i][0] == CardsPlaying[0][0]:
                    if TrackCards[i] == 'LeadingPlayer':
                        leading_player_count += 1
                    else:
                        non_leading_player_count += 1
                if leading_player_count == 4:
                    ScoreofHand = 8
                elif non_leading_player_count == 4:
                    ScoreofHand =  8
                elif leading_player_count == 3 or non_leading_player_count == 3:
                    ScoreofHand = 12
                else:
                    ScoreofHand = 16
            ScoreofHand = 8;
            return ScoreofHand; 
        # Check for one pair
        elif len([x for x in value_counts.values() if x == 2]) == 1:
            print("\nOne pair combination found!");
            ScoreofHand = 1;
            return ScoreofHand;
        # Check for two pair
        elif len([x for x in value_counts.values() if x == 2]) == 2:
            print("\nTwo pair combination found!");
            ScoreofHand = 2;
            return ScoreofHand; 
        # Check for three of a kind
        elif len([x for x in value_counts.values() if x == 3]) == 1:
            print("\nThrees combination found!");
            ScoreofHand = 3;
            return ScoreofHand;
        #Check for straight
        elif is_straight:
            print("\nStraight combination found!");
            ScoreofHand = 5; 
            return ScoreofHand;  
        else:
            ScoreofHand = 0;
            print("\nNo combination found!");
            return ScoreofHand;
          
class Game:
    def StartGame(self):
        print("Concerto game starts: \n");

        # 4 Player object created
        player1 = Player("North","1",[]); 
        player2 = Player("East","2",[]);
        player3 = Player("South","3",[]);
        player4 = Player("West","4",[]);

        # Assign players to different teams
        NS = Team("NS",[],[]);
        EW = Team("EW",[],[]);
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

        #Deal object creation
        deal = Deal();
        deal.StartDeal(NS,EW);
        deal.CalculateBonus(NS,EW);

        # Check game score

        DealLeft = 3; #Will be dynamically fetched when written in a loop
        Bonus = 100+100*DealLeft; #Bonus to be added
        SetUpNextDeal = False;
        if sum(NS.TeamScore) > 100:
            print("North-South is the winner of the game");
            print(sum(NS.TeamScore)+Bonus);
        elif sum(EW.TeamScore) > 100:
            print("East-West is the winner of the game");
            print(sum(EW.TeamScore)+Bonus);
        #If 4 deals are completed
        elif len(deal) == 4:
            if sum(NS.TeamScore) > sum(EW.TeamScore):
                print("North-South is the winner of the game");
                print(sum(NS.TeamScore)+Bonus);
            elif sum(NS.TeamScore) == sum(EW.TeamScore):
                print("Both teams have tied for the game");
            else:
                print("East-West is the winner of the game");
                print(sum(EW.TeamScore)+Bonus);
        else:
            SetUpNextDeal = True;
        
        if(SetUpNextDeal == True):
            print("Next deal begins");

        

game = Game();
game.StartGame();


