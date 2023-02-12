from collections import Counter
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
          