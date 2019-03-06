def select_cards(possible_cards, hand):
    for current_card in possible_cards:
        print("Do you want to pick up {}?".format(current_card))
        answer = input()
        if answer.lower() == 'y':
            if len(hand) >= 3:
                print("Sorry, you can only pick up 3 cards.")
            else:
                hand.append(current_card)
    return hand


available_cards = ['queen of spades', '2 of clubs', '3 of diamonds', 'jack of spades', 'queen of hearts']

new_hand = select_cards(available_cards, [])

while len(new_hand) < 3:
    print("You have only picked up {} cards.\nYou are required to have 3 cards.\nPlease choose again.".format(len(new_hand)))
    new_hand = select_cards(available_cards, [])

display_hand = "\n".join(new_hand)

print("Your new hand is: \n{}".format(display_hand))
