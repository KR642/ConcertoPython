from Hand import Hand
class Deal:
    TotalHands = 1;
    BonusPoints = "";
    TotalHandsPlayed = [];
    def StartDeal(self,NS,EW):
        i = 1;
        HandScore = 0;
        while(i <= self.TotalHands):
            self.TotalHandsPlayed.append(Hand());
            if(i % 2 != 0):
                #call function identifying leading and non leading players
                self.LeadingPlayer,self.NonLeadingPlayer = NS.IdentifyLeadAndNonLead(i);
                CardsPlayed, CardTrack = self.TotalHandsPlayed[i-1].PlayHands(self.LeadingPlayer,self.NonLeadingPlayer);
                HandScore = self.TotalHandsPlayed[i-1].CheckCombination(CardsPlayed);
                NS.TeamScore.append(HandScore);
                print(HandScore);
                print("\nEast-West team will be playing next:\n");
                i+=1;
            elif(i % 2 == 0):
                #call function identifying leading and non leading players
                self.LeadingPlayer,self.NonLeadingPlayer = EW.IdentifyLeadAndNonLead(i);
                CardsPlayed, CardTrack = self.TotalHandsPlayed[i-1].PlayHands(self.LeadingPlayer,self.NonLeadingPlayer);
                HandScore = self.TotalHandsPlayed[i-1].CheckCombination(CardsPlayed);
                EW.TeamScore.append(HandScore);
                if(i!=8):
                    print("\nNorth-South team will be playing next:\n");
                else:
                    print("\nA deal is completed\n");
                i+=1;