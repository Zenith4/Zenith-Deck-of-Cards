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

class Deck:
    def __init__(self,ace_low=False): #creates all cards and appends them to cardslist
        self.player_hands = {}
        self.cardslist = []
        if ace_low is False:
            self.AoD = Card('D',14)
            self.cardslist.append(self.AoD)
            self.AoH = Card('H',14)
            self.cardslist.append(self.AoH)
            self.AoS = Card('S',14)
            self.cardslist.append(self.AoS)
            self.AoC = Card('C',14)
            self.cardslist.append(self.AoC)
        else:
            self.AoD = Card('D',1)
            self.cardslist.append(self.AoD)
            self.AoH = Card('H',1)
            self.cardslist.append(self.AoH)
            self.AoS = Card('S',1)
            self.cardslist.append(self.AoS)
            self.AoC = Card('C',1)
            self.cardslist.append(self.AoC)            
        self.KoD = Card('D',13)
        self.cardslist.append(self.KoD)
        self.KoH = Card('H',13)
        self.cardslist.append(self.KoH)
        self.KoS = Card('S',13)
        self.cardslist.append(self.KoS)
        self.KoC = Card('C',13)
        self.cardslist.append(self.KoC)
        self.QoD = Card('D',12)
        self.cardslist.append(self.QoD)
        self.QoH = Card('H',12)
        self.cardslist.append(self.QoH)
        self.QoS = Card('S',12)
        self.cardslist.append(self.QoS)
        self.QoC = Card('C',12)
        self.cardslist.append(self.QoC)
        self.JoD = Card('D',11)
        self.cardslist.append(self.JoD)
        self.JoH = Card('H',11)
        self.cardslist.append(self.JoH)
        self.JoS = Card('S',11)
        self.cardslist.append(self.JoS)
        self.JoC = Card('C',11)
        self.cardslist.append(self.JoC)
        self.ToD = Card('D',10)
        self.cardslist.append(self.ToD)
        self.ToH = Card('H',10)
        self.cardslist.append(self.ToH)
        self.ToS = Card('S',10)
        self.cardslist.append(self.ToS)
        self.ToC = Card('C',10)
        self.cardslist.append(self.ToC)
        self.NoD = Card('D',9)
        self.cardslist.append(self.NoD)
        self.NoH = Card('H',9)
        self.cardslist.append(self.NoH)
        self.NoS = Card('S',9)
        self.cardslist.append(self.NoS)
        self.NoC = Card('C',9)
        self.cardslist.append(self.NoC)
        self.EoD = Card('D',8)
        self.cardslist.append(self.EoD)
        self.EoH = Card('H',8)
        self.cardslist.append(self.EoH)
        self.EoS = Card('S',8)
        self.cardslist.append(self.EoS)
        self.EoC = Card('C',8)
        self.cardslist.append(self.EoC)
        self.SeoD = Card('D',7)
        self.cardslist.append(self.SeoD)
        self.SeoH = Card('H',7)
        self.cardslist.append(self.SeoH)
        self.SeoS = Card('S',7)
        self.cardslist.append(self.SeoS)
        self.SeoC = Card('C',7)
        self.cardslist.append(self.SeoC)
        self.SoD = Card('D',6)
        self.cardslist.append(self.SoD)
        self.SoH = Card('H',6)
        self.cardslist.append(self.SoH)
        self.SoS = Card('S',6)
        self.cardslist.append(self.SoS)
        self.SoC = Card('C',6)
        self.cardslist.append(self.SoC)
        self.FioD = Card('D',5)
        self.cardslist.append(self.FioD)
        self.FioH = Card('H',5)
        self.cardslist.append(self.FioH)
        self.FioS = Card('S',5)
        self.cardslist.append(self.FioS)
        self.FioC = Card('C',5)
        self.cardslist.append(self.FioC)
        self.FoD = Card('D',4)
        self.cardslist.append(self.FoD)
        self.FoH = Card('H',4)
        self.cardslist.append(self.FoH)
        self.FoS = Card('S',4)
        self.cardslist.append(self.FoS)
        self.FoC = Card('C',4)
        self.cardslist.append(self.FoC)
        self.ThoD = Card('D',3)
        self.cardslist.append(self.ThoD)
        self.ThoH = Card('H',3)
        self.cardslist.append(self.ThoH)
        self.ThoS = Card('S',3)
        self.cardslist.append(self.ThoS)
        self.ThoC = Card('C',3)
        self.cardslist.append(self.ThoC)
        self.TwoD = Card('D',2)
        self.cardslist.append(self.TwoD)
        self.TwoH = Card('H',2)
        self.cardslist.append(self.TwoH)
        self.TwoS = Card('S',2)
        self.cardslist.append(self.TwoS)
        self.TwoC = Card('C',2)
        self.cardslist.append(self.TwoC)
    def remove(self,card): # removes card from cardslist
        self.cardslist.remove(card)
    def add(self,card): # adds card to cardslist
        self.cardslist.append(card)
    def reset(self): # doesn't work
        self = Deck()
    def deal_player_hands(self,num_of_players,num_of_cards): # deals out player hands
        for player in range(1,num_of_players+1):
            hand = []
            for _ in range(num_of_cards):
                randcard = random.choice(self.cardslist)
                hand.append(randcard)
                self.remove(randcard)
            self.player_hands['p%i' % player] = hand
    def print_player_hand(self,player_number): #prints a player's hand
        for card in self.player_hands['p%i' % player_number]:
            try: # this try sequence makes sure the last item doesn't have a comma
                tempindex = self.player_hands['p%i' % player_number].index(card) + 1
                _ = self.player_hands['p%i' % player_number][tempindex]
            except:
                end = '\n'
            else:
                end = ', '
            print(card.cardname,end=end)
