
# Highest and Lowest Ranking Cards
# Update this class so you can use it to determine the lowest ranking and highest ranking cards in a list of Card objects:

class Card:
    def __init__(self, rank, suit):
        self.name = Card.__name__
        self.rank = rank
        self.suit = suit
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack' ,'Queen', 'King', 'Ace']

    def min(self, lst):
        minimum = 0
        for card1 in lst:
            for card2 in self.ranks:
                if self.ranks.index(card2) < minimum:
                    minimum = card1
        return minimum

    def max(self ,lst):
        maximum = 0
        for card1 in lst:
            for card2 in self.ranks:
                if self.ranks.index(card2) > maximum:
                    maximum = card1
        return maximum


    def __str__(self):
        retur n(f"{(self.name)}({self.rank}, {self.suit})")

    def __lt__(self, other):
        return self.ranks.index(self.rank) < other.ranks.index(other.rank)

    def __gt__(self ,other):
        return self.ranks.index(self.rank) > other.ranks.index(other.rank)


# cards = [Card(2, 'Hearts'),
#          Card(10, 'Diamonds'),
#          Card('Ace', 'Clubs')]

# print(max(cards))

# For this exercise, numeric cards are low cards, ordered from 2 through 10. Jacks are higher than 10s, Queens are higher than Jacks, Kings are higher than Queens, and Aces are higher than Kings. The suit plays no part in the relative ranking of cards.

# If you have two or more cards of the same rank in your list, your min and max methods should return one of the matching cards; it doesn't matter which one.

# Besides any methods needed to determine the lowest and highest cards, create a __str__ method that returns a string representation of the card, e.g., "Jack of Diamonds", "4 of Clubs", etc.

cards = [Card(2, 'Hearts'),
         Card(10, 'Diamonds'),
         Card('Ace', 'Clubs')]
print(min(cards) == Card(2, 'Hearts'))             # True
print(max(cards) == Card('Ace', 'Clubs'))          # True
# print(str(min(cards)) == "2 of Hearts")            # True
# print(str(max(cards)) == "Ace of Clubs")           # True

# cards = [Card(5, 'Hearts')]
# print(min(cards) == Card(5, 'Hearts'))             # True
# print(max(cards) == Card(5, 'Hearts'))             # True
# print(str(Card(5, 'Hearts')) == "5 of Hearts")     # True

# cards = [Card(4, 'Hearts'),
#          Card(4, 'Diamonds'),
#          Card(10, 'Clubs')]
# print(min(cards).rank == 4)                        # True
# print(max(cards) == Card(10, 'Clubs'))             # True
# print(str(Card(10, 'Clubs')) == "10 of Clubs")     # True

# cards = [Card(7, 'Diamonds'),
#          Card('Jack', 'Diamonds'),
#          Card('Jack', 'Spades')]
# print(min(cards) == Card(7, 'Diamonds'))           # True
# print(max(cards).rank == 'Jack')                   # True
# print(str(Card(7, 'Diamonds')) == "7 of Diamonds") # True

# cards = [Card(8, 'Diamonds'),
#          Card(8, 'Clubs'),
#          Card(8, 'Spades')]
# print(min(cards).rank == 8)                        # True
# print(max(cards).rank == 8)                        # True

