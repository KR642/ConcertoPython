def best_poker_hand(cards):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    suits = set([card[1] for card in cards])

    # Check for straight flush
    flush_suits = [card[1] for card in cards]
    for suit in suits:
        suit_cards = [card for card in cards if card[1] == suit]
        if len(suit_cards) >= 5:
            suit_card_values = sorted([values[card[0]] for card in suit_cards], reverse=True)
            for i in range(len(suit_card_values) - 4):
                if suit_card_values[i] == suit_card_values[i+4] + 4:
                    straight_flush_cards = [(card[0], suit) for card in suit_cards if values[card[0]] in range(suit_card_values[i+4], suit_card_values[i]+1)]
                    return (straight_flush_cards)

    # Check for four of a kind
    values_count = {card[0]: 0 for card in cards}
    for card in cards:
        values_count[card[0]] += 1
    for value, count in values_count.items():
        if count == 4:
            four_of_a_kind_cards = [card for card in cards if card[0] == value]
            remaining_cards = [card for card in cards if card[0] != value]
            return (four_of_a_kind_cards + sorted(remaining_cards, key=lambda x: values[x[0]], reverse=True)[:1])

    # Check for full house
    three_of_a_kind_values = [value for value, count in values_count.items() if count == 3]
    pairs = [value for value, count in values_count.items() if count == 2]
    if len(three_of_a_kind_values) >= 1 and len(pairs) >= 1:
        three_of_a_kind_value = max(three_of_a_kind_values, key=lambda x: values[x])
        pair_value = max(pairs, key=lambda x: values[x])
        full_house_cards = [card for card in cards if card[0] == three_of_a_kind_value or card[0] == pair_value]
        return (full_house_cards)

    # Check for flush
    for suit in suits:
        suit_cards = [card for card in cards if card[1] == suit]
        if len(suit_cards) >= 5:
            flush_cards = sorted(suit_cards, key=lambda x: values[x[0]], reverse=True)[:5]
            return (flush_cards)

    # Check for straight
    unique_values = list(set([card[0] for card in cards]))
    unique_values.sort(key=lambda x: values[x], reverse=True)
    straight_values = []
    for i in range(len(unique_values)-4):
        if values[unique_values[i]] == values[unique_values[i+4]] + 4:
            straight_values = unique_values[i:i+5]
            break
    if straight_values:
        straight_cards = [(value, suit) for value in straight_values for suit in suits]
        return (straight_cards)

        # Check for three of a kind
    three_of_a_kind_values = [value for value, count in values_count.items() if count == 3]
    if len(three_of_a_kind_values) >= 1:
        three_of_a_kind_value = max(three_of_a_kind_values, key=lambda x: values[x])
        three_of_a_kind_cards = [card for card in cards if card[0] == three_of_a_kind_value]
        remaining_cards = [card for card in cards if card[0] != three_of_a_kind_value]
        return (three_of_a_kind_cards + sorted(remaining_cards, key=lambda x: values[x[0]], reverse=True)[:2])

    # Check for two pair
    pair_values = [value for value, count in values_count.items() if count == 2]
    if len(pair_values) >= 2:
        pair_values.sort(key=lambda x: values[x], reverse=True)
        pair_cards = []
        for value in pair_values[:2]:
            pair_cards += [card for card in cards if card[0] == value]
        remaining_cards = [card for card in cards if card[0] != pair_values[0] and card[0] != pair_values[1]]
        return (pair_cards + [max(remaining_cards, key=lambda x: values[x[0]])])

    # Check for one pair
    pair_values = [value for value, count in values_count.items() if count == 2]
    if len(pair_values) == 1:
        pair_cards = [card for card in cards if card[0] == pair_values[0]]
        remaining_cards = [card for card in cards if card[0] != pair_values[0]]
        return (pair_cards + sorted(remaining_cards, key=lambda x: values[x[0]], reverse=True)[:3])

    # High card
    return (sorted(cards, key=lambda x: values[x[0]], reverse=True)[:5])


       




CardsLeft = [('6', 'hearts'), ('7', 'hearts'), ('8', 'hearts'), ('9', 'spades'),('9','hearts'),('9','diamonds')];
list = best_poker_hand(CardsLeft)
print(list);
