from collections import Counter
class Hand:
    HandScore = "";
    TotalCards = 5;
    TrackMoves = ["","","","","","","","","","","","",""];
    TrackCards = [];

    def PlayHands(self, LeadingPlayerObj, NonLeadingPlayerObj):
        self.ConsecutivePass = False;
        self.NextTurn = "";
        self.x = 1; # The number of cards
        self.CardsPlaying = [];
        while(self.x<=self.TotalCards):
            if(self.x == 1):
                print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                LeadingPlayerObj.ShowCards();
                self.CardsPlaying = LeadingPlayerObj.PlayCards();
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
                            self.CardsPlaying = NonLeadingPlayerObj.PlayCards();
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
                                print("\nNon-Leading player "+LeadingPlayerObj.name+" is playing now:\n");
                                NonLeadingPlayerObj.ShowCards();
                                self.CardsPlaying = NonLeadingPlayerObj.PlayCards();
                                self.TrackCards.append("NonLeadingPlayer");
                                self.NextTurn = "LeadingPlayer";
                                self.x+=1;
                            elif(move == "Play"):
                                print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                                self.CardsPlaying = LeadingPlayerObj.PlayCards();
                                self.TrackCards.append("LeadingPlayer");
                                self.NextTurn = "NonLeadingPlayer";
                                self.x+=1;
                            elif(move == "Force"):
                                print("\nNon-Leading player "+NonLeadingPlayerObj.name+" is playing now:\n");
                                self.CardsLeft = 5 - (self.x-1); #To find rest of the cards to be played
                                self.i = 1;
                                while(self.i<=self.CardsLeft):
                                    NonLeadingPlayerObj.ShowCards();
                                    self.CardsPlaying = NonLeadingPlayerObj.PlayCards();
                                    self.TrackCards.append("LeadingPlayer");
                                    self.i+=1;
                                break;
                    elif(move == "Force"):
                        print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                        self.CardsLeft = 5 - (self.x-1); #To find rest of the cards to be played
                        self.i = 1;
                        LeadingPlayerObj.ShowCards();
                        while(self.i<=self.CardsLeft):
                            
                            self.CardsPlaying = LeadingPlayerObj.PlayCards();
                            self.TrackCards.append("NonLeadingPlayer");
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
                            self.CardsPlaying = LeadingPlayerObj.PlayCards();
                            self.TrackCards.append("NonLeadingPlayer");
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
                                self.CardsPlaying = LeadingPlayerObj.PlayCards();
                                self.TrackCards.append("LeadingPlayer");
                                self.NextTurn = "NonLeadingPlayer";
                                self.x+=1;
                            elif(move == "Play"):
                                print("\nNon-Leading "+NonLeadingPlayerObj.name+" player is playing now:\n");
                                self.CardsPlaying = NonLeadingPlayerObj.PlayCards();
                                self.TrackCards.append("NonLeadingPlayer");
                                self.NextTurn = "LeadingPlayer";
                                self.x+=1;
                            elif(move == "Force"):
                                print("\nLeading player "+LeadingPlayerObj.name+" is playing now:\n");
                                self.CardsLeft = 5 - (self.x-1); #To find rest of the cards to be played
                                self.i = 1;
                                while(self.i<=self.CardsLeft):
                                    LeadingPlayerObj.ShowCards();
                                    self.CardsPlaying = LeadingPlayerObj.PlayCards();
                                    self.TrackCards.append("LeadingPlayer");
                                    self.i+=1;
                                break;
                    elif(move == "Force"):
                        print("\nNon-Leading player "+NonLeadingPlayerObj.name+" is playing now:\n");
                        self.CardsLeft = 5 - (self.x-1); #To find rest of the cards to be played
                        self.i = 1;
                        while(self.i<=self.CardsLeft):
                            NonLeadingPlayerObj.ShowCards();
                            self.CardsPlaying = NonLeadingPlayerObj.PlayCards();
                            self.TrackCards.append("NonLeadingPlayer");
                            self.i+=1;
                        break;
                    elif(move == "Error"):
                        print("Error in selecting option, please try again");
        # print(self.CardsPlaying);
        # print("leading left\n");
        # print(LeadingPlayerObj.CardsReceived);
        # print("nonleading left\n");
        # print(NonLeadingPlayerObj.CardsReceived);
        return self.CardsPlaying,self.TrackCards;

    def CheckCombination(self,CardsPlaying):
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
            ScoreofHand = 10;
            return ScoreofHand;
        #check for flush
        elif len(set(suits)) == 1:
            print("\nFlush combination found!");
            ScoreofHand = 6;
            return ScoreofHand; 
        # Check for fours
        if max(value_counts.values()) == 4:
            print("\nFours combination found!");
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
            print("\nNo combination found!");
        