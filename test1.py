# class Player:
#     Score = [];
#     def __init__(self):
#         self.Score = []

#     def AddScore(self):
#         score = input("\n enter score");
#         self.Score.append(score);
#         return self.Score;
# class Start:
#     def StartAll(self):
#         p1 = Player()
#         p2 = Player()
#         i = 1
#         all_scores = []
#         while i <= 5:
#             if (i % 2 == 0):
#                 p1.AddScore()
#                 all_scores.append(p1.Score[-1])
#                 i += 1
#             elif (i % 2 != 0):
#                 p2.AddScore()
#                 all_scores.append(p2.Score[-1])
#                 i += 1
#         print(all_scores)
#         print(p1.Score)
#         print(p2.Score)

# start = Start();

# i=1;
# start1=[];
# while i<=2:
#     start1.append(Start());
#     start1[i-1].StartAll();
#     i+=1;




from collections import Counter

def get_best_hand(cards):
    rank_counts = {}
    suits = {}
    for card in cards:
        rank, suit = card
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
        suits[suit] = suits.get(suit, 0) + 1
        
    sorted_ranks = sorted(rank_counts.keys(), key=lambda x: rank_counts[x], reverse=True)

    # Check for a straight
    for i in range(len(sorted_ranks) - 4):
        if int(sorted_ranks[i]) - int(sorted_ranks[i + 4]) == 4:
            straight_ranks = sorted_ranks[i:i + 5]
            return [card for card in cards if card[0] in straight_ranks][:5]
    
    # Check for flush
    for suit, count in suits.items():
        if count >= 5:
            flush_cards = [card for card in cards if card[1] == suit]
            flush_ranks = [card[0] for card in flush_cards]
            return [card for card in flush_cards if card[0] in sorted(flush_ranks, reverse=True)][:5]
    
    # Check for four of a kind
    if len(sorted_ranks) >= 4 and rank_counts[sorted_ranks[0]] == 4:
        four_rank = sorted_ranks[0]
        return [card for card in cards if card[0] == four_rank][:4] + [card for card in cards if card[0] == sorted_ranks[-1]][:1]

    # Check for a full house
    if len(sorted_ranks) >= 3 and rank_counts[sorted_ranks[0]] == 3 and rank_counts[sorted_ranks[1]] == 2:
        three_rank = sorted_ranks[0]
        two_rank = sorted_ranks[1]
        return [card for card in cards if card[0] == three_rank][:3] + [card for card in cards if card[0] == two_rank][:2]
    
    # Check for three of a kind
    if len(sorted_ranks) >= 3 and rank_counts[sorted_ranks[0]] == 3:
        three_rank = sorted_ranks[0]
        return [card for card in cards if card[0] == three_rank][:3] + [card for card in cards if card[0] == sorted_ranks[-2]][:1] + [card for card in cards if card[0] == sorted_ranks[-1]][:1]

    # Check for two pair
    if len(sorted_ranks) >= 2 and rank_counts[sorted_ranks[0]] == 2 and rank_counts[sorted_ranks[1]] == 2:
        first_pair_rank = sorted_ranks[0]
        second_pair_rank = sorted_ranks[1]
        return [card for card in cards if card[0] == first_pair_rank][:2] + [card for card in cards if card[0] == second_pair_rank][:2] + [card for card in cards if card[0] == sorted_ranks[-1]][:1]

    # Check for a pair
    if len(sorted_ranks) >= 2 and rank_counts[sorted_ranks[0]] == 2:
        pair_rank = sorted_ranks[0]
        return [card for card in cards if card[0] == pair_rank][:2] + [card for card in cards if card[0] != pair_rank][:3]

    # Return the highest cards
    return [card for card in cards if card[0] == sorted_ranks[0]][:1] + [card for card in cards if card[0] == sorted_ranks[1]][:1] + [card for card in cards if card[0] == sorted_ranks[2]][:1] + [card for card in cards if card[0] == sorted_ranks[3]][:1] + [card for card in cards if card[0] == sorted_ranks[4]][:1]



def CheckCombination(CardsPlaying,TrackCards):
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


# cards = [('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'),('2','spades'), ('5', 'hearts'),('6','hearts')];
cards1 = [('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts')];
cards2 = [('2','spades'), ('5', 'hearts'),('6','hearts')];
cardsOrg = cards = cards1 + cards2;

t1Length = len(cards1);
t1 = ['LeadingPlayer']*t1Length;

t2Length = len(cards2);
t2 = ['NonLeadingPlayer']*t2Length;

TrackCards1 = t1+t2;



list = get_best_hand(cards);
print("the best 5 ");
print(list);

indexes = []
for i, item in enumerate(cardsOrg):
    if item in list:
        indexes.append(i);


print(cardsOrg);
print(TrackCards1);
TrackCards = [TrackCards1[i] for i in indexes]


print(TrackCards);



# score = CheckCombination(list,TrackCards);

# print(score);