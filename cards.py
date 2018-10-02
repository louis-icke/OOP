from random import shuffle, randint

class Card():
    def __init__(self, value, suit):
        self.__value = value
        if value > 10:
            self.__type = 'picture'
        else:
            self.__type = 'number'
        if value == 11:
            self.__picture = 'J'
        elif value == 12:
            self.__picture = 'Q'
        elif value == 13:
            self.__picture = 'K'
        else:
            self.__picture = None
        self.__suit = suit

    def show(self):
        if self.__type == 'picture':
            out = self.__picture
        else:
            out = str(self.__value)
        out += self.__suit
        return out

class Deck():
    def __init__(self, size=52):
        self.__cards = self.build()
        self.__size = size

    def build(self):
        cards = []
        cards += self.buildSuit('♠')
        cards += self.buildSuit('♥')
        cards += self.buildSuit('♣')
        cards += self.buildSuit('♦')
        return cards

    def buildSuit(self,suit):
        cards = []
        for i in range(1,14):
            cards.append(Card(i,suit))
        return cards

    def show(self):
        out = []
        for i in range(self.__size):
            out.append(self.__cards[i].show())
        return out

    def showTop(self):
        return self.__cards[0].show()

    def deal(self,size):
        out = []
        for i in range(size):
            out.append(self.__cards[0])
            del self.__cards[0]
        return out

    def shuffle(self):
        for i in range(self.__size-1, -1, -1):
            j = randint(0,i)
            self.__cards[i], self.__cards[j] = self.__cards[j], self.__cards[i]

class Player():
    def __init__(self, deck, size):
        self.__hand = deck.deal(size)

    def show(self):
        out = []
        for i in range(len(self.__hand)):
            out.append(self.__hand[i].show())
        return out
        
    
x = Deck()
x.shuffle()
one = Player(x,5)
two = Player(x,5)
print(one.show())
print(two.show())
