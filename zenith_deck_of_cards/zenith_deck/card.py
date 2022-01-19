import random
class Card: #class for cards, obviously
    def __init__(self,suit,rank):
        self.suit = suit 
        self.rank = rank
        self.create_cardname()
    def create_cardname(self): #creates a name to be printed out, e.g "King of Clubs" and stores it in the attribute cardname
        self.cardname = '{rank} of {suit}'
        if self.suit == 'D':
            suit = 'Diamonds'
        elif self.suit == 'S':
            suit = 'Spades'
        elif self.suit == 'H':
            suit = 'Hearts'
        elif self.suit == 'C':
            suit = 'Clubs'
        if self.rank == 14:
            val = 'Ace'
        if self.rank == 13:
            val = 'King'
        elif self.rank == 12:
            val = 'Queen'
        elif self.rank == 11:
            val =  'Jack'
        elif self.rank == 10:
            val = 'Ten'
        elif self.rank == 9:
            val = 'Nine'
        elif self.rank == 8:
            val = 'Eight'
        elif self.rank == 7:
            val = 'Seven'
        elif self.rank == 6:
            val = 'Six'
        elif self.rank == 5:
            val = 'Five'
        elif self.rank == 4:
            val = 'Four'
        elif self.rank == 3:
            val = 'Three'
        elif self.rank == 2:
            val = 'Two'
        elif self.rank == 1:
            val = 'Ace'
        self.cardname = self.cardname.format(rank = val,suit = suit)
