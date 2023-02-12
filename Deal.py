from Hand import Hand
class Deal:
    TotalHands = 8;
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
