def find_best_hand(cards):
    sorted_ranks = sorted([card[0] for card in cards], reverse=True)
    rank_counts = {rank: sorted_ranks.count(rank) for rank in set(sorted_ranks)}
    suits = [card[1] for card in cards]

    # Check for a straight flush
    if sorted_ranks == list(range(int(sorted_ranks[0]), int(sorted_ranks[0]) - 5, -1)) and len(set(suits)) == 1:
        return cards

    # Check for four of a kind
    for rank, count in rank_counts.items():
        if count == 4:
            return [card for card in cards if card[0] == rank] + [card for card in cards if card[0] != rank][:1]

    # Check for a full house
    if sorted_ranks[0] == sorted_ranks[2] and sorted_ranks[3] == sorted_ranks[4]:
        return [card for card in cards if card[0] == sorted_ranks[0]] + [card for card in cards if card[0] == sorted_ranks[3]]

    # Check for a flush
    if len(set(suits)) == 1:
        return cards

    # Check for a straight
    if sorted_ranks == list(range(int(sorted_ranks[0]), int(sorted_ranks[0]) - 5, -1)):
        return cards

    # Check for three of a kind
    for rank, count in rank_counts.items():
        if count == 3:
            return [card for card in cards if card[0] == rank] + [card for card in cards if card[0] != rank][:2]

    # Check for two pairs
    if len(rank_counts) == 3 and sorted(rank_counts.values()) == [1, 2, 2]:
        second_pair_rank = [rank for rank, count in rank_counts.items() if count == 2 and rank != sorted_ranks[0]][0]
        return [card for card in cards if card[0] == sorted_ranks[0]] + [card for card in cards if card[0] == second_pair_rank][:2] + [card for card in cards if card[0] != sorted_ranks[0] and card[0] != second_pair_rank][:1]

    # Check for a pair
    if len(rank_counts) >= 2 and 2 in rank_counts.values():
        pair_rank = [rank for rank, count in rank_counts.items() if count == 2][0]
        return [card for card in cards if card[0] == pair_rank][:2] + [card for card in cards if card[0] != pair_rank][:3]

    # Return the highest cards
    return cards[:5]


cards = [('2', 'hearts'), ('3', 'hearts'), ('4', 'hearts'), ('5', 'hearts'),('2','diamonds'),('6','hearts')];
list = find_best_hand(cards);
print(list);

TrackCards = ['LeadingPlayer','NonLeadingPlayer','NonLeadingPlayer','LeadingPlayer','LeadingPlayer']
