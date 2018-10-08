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

    def value(self):
        return self.__value

    def suit(self):
        return self.__suit

    def isPicture(self):
        if self.__picture != None:
            return True
        else:
            return False

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

class Player(object):
    def __init__(self, deck, size, bet):
        self.hand = deck.deal(size)
        #self.hand2 = None
        self.__bet = bet
        self.__insurance = 0

    def show(self):
        out = ''
        for i in range(len(self.hand)):
            out += ', ' + self.hand[i].show()
        out = out[2:]
        return out

    def draw(self, deck, size=1):
        self.hand += deck.deal(size)

    def total(self):
        total = 0
        for i in range(len(self.hand)):
            if self.hand[i].isPicture() == True:
                total += 10
            else:
                total += self.hand[i].value()
        return total

    def insure(self,value):
        self.__insurance = value

    def getInsurance(self):
        return self.__insurance

    def getBet(self):
        return self.__bet

    def canSplit(self):
        c1 = self.hand[0].value()
        c2 = self.hand[1].value()
        if c1 == c2:
            return True
        else:
            return False

    '''def split(self):
        self.hand2 = self.hand
        print('A bet of £'+str(self.__bet)+' has been placed on the second hand.')'''
        
    def isBlackjack(self):
        if self.total() == 21:
            return True
        else:
            return False

    def isBust(self):
        if self.total() > 21:
            return True

class Dealer(Player):      
        
    def initShow(self):
        return self.hand[0].show()

    def firstVal(self):
        return self.hand[0].value()

    def play(self,deck):
        print('\nDealer:')
        play = True
        while play == True:
            print('    '+self.show())
            if self.total() < 16:
                self.draw(deck)
            elif self.total() <= 21:
                print()
                return self.total()
            else:
                print('Dealer is bust/\n')
                return None

def numIn(message,top=None,bottom=0):
    valid = False
    while valid == False: 
        try:
            number = abs(int(input(message)))
            if top != None:
                if number > top or number <= bottom:
                    print('That is not a valid number.')
                else:
                    valid = True
                    return number
            else:
                valid = True
                return number
        except:
            print('That is not a valid number.')
        

def twoIn(message,one,two):
    valid = False
    while valid == False:
        pIn = input(message).upper()
        if pIn == one or pIn == two:
            valid = True
            return pIn
        else:
             print('That is not a valid option.')
        

def playHand(player,handNum,deck):
    print('    Your cards are: '+player.show())
    playing = True
    while playing == True:
        #Hit / stand
        pIn = twoIn('    Do you want to hit or stand? [H/S] ','H','S')
        if pIn == 'H':
            player.draw(deck)
        else:
            playing = False
        print('    Your cards are: '+player.show())
        #check for bust
        if player.isBust() == True:
            print('    You are bust.')
            playing = False

def main():
    #Creation of variables
    x = Deck()
    x.shuffle()
    dealer = Dealer(x,2,None)
    players = []
    playerNum = numIn('Please input the number of players [MAX 7]: ',7)
    for i in range(playerNum):
        players.append(Player(x,2,numIn(('Please input the bet for player '+str(i+1)+': £'))))

    #Initial showing of cards
    print()
    print('The dealer\'s face up card is a: '+dealer.initShow())
    for i in range(playerNum):
        print('Player '+str(i+1)+'\'s cards are: '+players[i].show())

    #Insurance    
    print()
    if dealer.firstVal() == 1:
        for i in range(playerNum):
            players[i].insure(numIn('The dealer\'s first card is an ace, please place an insurance bet for player '+str(i+1)+': £'))
    elif dealer.firstVal() == 10:
        for i in range(playerNum):
            players[i].insure(numIn('The dealer\'s first card is a 10, please place an insurance bet for player '+str(i+1)+': £'))

    #Check for dealer blackjack
    if dealer.isBlackjack() == True:
        print('\nThe dealer has a blackjack!\n')
        for i in range(playerNum):
            total = 0
            player = players[i]
            if player.isBlackjack() == True:
                total += player.getBet()
            total += player.getInsurance() * 2
            print('Player '+str(i+1)+' wins £'+str(total))

    #Check for player blackjack
    for i in range(playerNum):
        player = players[i]
        if player.isBlackjack == True:
            print('\nPlayer '+str(i+1)+' has a blackjack!')
            total = player.getBet() * 1.5
            print('Player '+str(i+1)+' wins £'+str(total))

    #Main play
    for i in range(playerNum):
        player = players[i]
        print('\nPlayer '+str(i+1)+':')
        '''#Checking if player can split
        if player.canSplit() == True:
            pIn = twoIn('    You can split your hand do you want to split? [Y/N] ','Y','N')
            if pIn == 'Y':
                player.split()'''
        playHand(player,0,x)
        '''if player.hand2 != None:
            playHand(player,1)'''

    dealTot = dealer.play(x)
    print('\nDealer total: '+str(dealer.total())+'\n')

    #Totaling
    for i in range(playerNum):
        player = players[i]
        total = 0
        if player.total() > 22: #If bust:
            print('Player '+str(i+1)+' is bust.')
            total = 0
        elif dealTot == None: #If dealer is bust
            total = player.getBet() * 2
        elif player.total() > dealer.total(): #If win
            total = player.getBet() * 2
            print('Player '+str(i+1)+' wins against dealer')
        else:
            print('Dealer wins against player '+str(i+1)+'.')
        print('Player '+str(i+1)+' wins £'+str(total))

main()
