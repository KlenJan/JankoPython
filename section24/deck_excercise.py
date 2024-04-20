import random as r


class Card:
    suites = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, suit, value) -> None:
        self.suit = suit
        self.value = value

    def __repr__(self) -> str:
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self) -> None:
        self.cards = [Card(x, y) for x in Card.suites for y in Card.values]

    def __repr__(self) -> str:
        return f"Deck of {self.count()} cards"

    def _deal(self, number):
        if self.count() <= 0:
            raise ValueError('All cards have been dealt')
        if self.count() < number:
            number = self.count()
        removedcards = [self.cards.pop(-1) for x in range(number)]
        return removedcards

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError('Only full decks can be shuffled')
        r.shuffle(self.cards)

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, number):
        return self._deal(number)


d = Deck()
# print(d.count())
# print(d)
print(d.cards)
d._deal(53)
print(d.cards)
# print(d.count())
# print(len(d.cards))
# d.shuffle()
# print(d.cards)
# print(d.deal_card())
# print(d.cards)
# print(d.deal_hand(3))
# print(d.count())
# print(d.deal_hand(3))
