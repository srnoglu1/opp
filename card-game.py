from random import shuffle
class card:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __repr__(self):
        return f"{self.type} {self.value}"


class deck:
    types = ["Hearts","Diamonds","Clubs","Spades"]
    values = ["A","2","3","4","4","6","7","8","8","10","J","Q","K"]

    def __init__(self):
        self.cards = [card(type,value) for type in deck.types for value in deck.values ]

    def cardNumber(self):
        return self.cards

    def shuffleTheCard(self):
        if self.cardNumber()<52:
            raise ValueError ("you can shuffle cards before the deck is destroyed.")
        shuffle (self.cards)
    
    def giveCards(self,piece):
        cardNumber = self.cardNumber()
        if cardNumber == 0:
            raise ValueError ("the cards distributed to everyone.")
        adet = min([cardNumber,piece])
        _cards = self.cards[-piece:]
        self.cards = self.cards[:-piece]
        return _cards


deck1 = deck()

deck1.shuffleTheCard()
print(deck1.giveCards(5))
print(deck1.cardNumber())

print(deck1.cards)
