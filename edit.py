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
