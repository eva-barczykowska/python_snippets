suits = ["♦", "♥", "♠", "♣"]
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
#
# all_cards = []
# for suit in suits:
#     for card in cards:
#         all_cards.append(f'{suit}{card}')
#
# print(all_cards)
#
# # write Medium article why this does not work
# all_cards = {}
# for suit in suits:
#     for card in cards:
#         if suit not in all_cards:
#             all_cards[suit] = []  # Initialize list for new suit
#         else:
#             all_cards[suit].append(card) # missing the first card of each suit
#
# print(all_cards)

#Medium
suits = ["♦", "♥", "♠", "♣"]
cards = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

all_cards = {}
for suit in suits:
    for card in cards:
        if suit not in all_cards:
            all_cards[suit] = []
        else:
            all_cards[suit].append(f'{suit}{card}')

print(all_cards)

# all_cards = {}
# for suit in suits:
#     for card in cards:
#         if suit not in all_cards:
#             all_cards[suit] = [f'{suit}{card}'] # Initialize list for new suit plus add the first card
#         else:
#             all_cards[suit].append(f'{suit}{card}') # I LOST '♦1' and every other 1 of each suit!!!
#
# print(all_cards)