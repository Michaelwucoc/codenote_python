def find_card_to_play(lead_card, dealer_cards):
    lead_value, lead_suit = lead_card[0], lead_card[1]

    if same_suit_cards := [
        card for card in dealer_cards if card[1] == lead_suit
    ]:
        if higher_rank_cards := [
            card for card in same_suit_cards if card[0] > lead_value
        ]:
            return min(higher_rank_cards)

        return min(same_suit_cards)


    return min(dealer_cards)

# Process each input line
for _ in range(5):
    input_line = input().split()
    lead_card = input_line[0]
    dealer_cards = input_line[1:]
        

    # Find the card to play and print the result
    result = find_card_to_play(lead_card, dealer_cards)
    print(result)
