import random,enum
class Suit(enum.Enum):
  DIAMONDS = ('D','Diamonds')
  HEARTS = ('H','Hearts')
  SPADES = ('S','Spades')
  CLUBS = ('C','Clubs')
  SUIT_RED_JOKER = ('R', 'Red')
  SUIT_BLACK_JOKER = ('B', 'Black')
class Rank(enum.Enum):
  ACE_HIGH = (14,'Ace')
  KING = (13,'King')
  QUEEN = (12,'Queen')
  JACK = (11, 'Jack')
  TEN = (10, 'Ten')
  NINE = (9, 'Nine')
  EIGHT = (8, 'Eight')
  SEVEN = (7, 'Seven')
  SIX = (6, 'Six')
  FIVE = (5, 'Five')
  FOUR = (4, 'Four')
  THREE = (3, 'Three')
  TWO = (2, 'Two')
  ACE_LOW = (1, 'Ace')
  RANK_RED_JOKER = (0, "Joker")
  RANK_BLACK_JOKER = (0, "Joker")
class Card:
  def __init__(self,suit,rank):
    self.suit = suit
    self.rank = rank
    self.create_cardname()
  def create_cardname(self):
    rank = self.rank.value[1]
    suit = self.suit.value[1]
    if self.rank != Rank.RANK_RED_JOKER and self.rank != Rank.RANK_BLACK_JOKER:
      self.cardname = '{rank} of {suit}'.format(rank=rank,suit=suit)
    else:
      self.cardname = '{suit} {rank}'.format(suit=suit,rank=rank)
class Deck:
  def __init__(self,ace_low=False,jokers=False):
    self.piles = {}
    self.maindeck = []
    if jokers is True:
      RJ = Card(Suit.SUIT_RED_JOKER,Rank.RANK_RED_JOKER)
      self.maindeck.append(RJ)
      BJ = Card(Suit.SUIT_BLACK_JOKER,Rank.RANK_BLACK_JOKER)
      self.maindeck.append(BJ)
    if ace_low is False:
      AoD = Card(Suit.DIAMONDS,Rank.ACE_HIGH)
      self.maindeck.append(AoD)
      AoH = Card(Suit.HEARTS,Rank.ACE_HIGH)
      self.maindeck.append(AoH)      
      AoS = Card(Suit.SPADES,Rank.ACE_HIGH)
      self.maindeck.append(AoS)
      AoC = Card(Suit.CLUBS,Rank.ACE_HIGH)
      self.maindeck.append(AoC)
    else:
      AoD = Card(Suit.DIAMONDS,Rank.ACE_LOW)
      self.maindeck.append(AoD)
      AoH = Card(Suit.HEARTS,Rank.ACE_LOW)
      self.maindeck.append(AoH)
      AoS = Card(Suit.SPADES,Rank.ACE_LOW)
      self.maindeck.append(AoS)
      AoC = Card(Suit.CLUBS,Rank.ACE_LOW)
      self.maindeck.append(AoC)
    ToD = Card(Suit.DIAMONDS,Rank.TWO)
    self.maindeck.append(ToD)
    ToH = Card(Suit.HEARTS,Rank.TWO)
    self.maindeck.append(ToH)
    ToS = Card(Suit.SPADES,Rank.TWO)
    self.maindeck.append(ToS)
    ToC = Card(Suit.CLUBS,Rank.TWO)
    self.maindeck.append(ToC)
    ThoD = Card(Suit.DIAMONDS,Rank.THREE)
    self.maindeck.append(ThoD)
    ThoH = Card(Suit.HEARTS,Rank.THREE)
    self.maindeck.append(ThoH)
    ThoS = Card(Suit.SPADES,Rank.THREE)
    self.maindeck.append(ThoS)
    ThoC = Card(Suit.CLUBS,Rank.THREE)
    self.maindeck.append(ThoC)
    FoD = Card(Suit.DIAMONDS,Rank.FOUR)
    self.maindeck.append(FoD)
    FoH = Card(Suit.HEARTS,Rank.FOUR)
    self.maindeck.append(FoH)
    FoS = Card(Suit.SPADES,Rank.FOUR)
    self.maindeck.append(FoS)
    FoC = Card(Suit.CLUBS,Rank.FOUR)
    self.maindeck.append(FoC)
    FioD = Card(Suit.DIAMONDS,Rank.FIVE)
    self.maindeck.append(FioD)
    FioH = Card(Suit.HEARTS,Rank.FIVE)
    self.maindeck.append(FioH)
    FioS = Card(Suit.SPADES,Rank.FIVE)
    self.maindeck.append(FioS)
    FioC = Card(Suit.CLUBS,Rank.FIVE)
    self.maindeck.append(FioC)
    SoD = Card(Suit.DIAMONDS,Rank.SIX)
    self.maindeck.append(SoD)
    SoH = Card(Suit.HEARTS,Rank.SIX)
    self.maindeck.append(SoH)
    SoS = Card(Suit.SPADES,Rank.SIX)
    self.maindeck.append(SoS)
    SoC = Card(Suit.CLUBS,Rank.SIX)
    self.maindeck.append(SoC)
    SeoD = Card(Suit.DIAMONDS,Rank.SEVEN)
    self.maindeck.append(SeoD)
    SeoH = Card(Suit.HEARTS,Rank.SEVEN)
    self.maindeck.append(SeoH)
    SeoS = Card(Suit.SPADES,Rank.SEVEN)
    self.maindeck.append(SeoS)
    SeoC = Card(Suit.CLUBS,Rank.SEVEN)
    self.maindeck.append(SeoC)
    EoD = Card(Suit.DIAMONDS,Rank.EIGHT)
    self.maindeck.append(EoD)
    EoH = Card(Suit.HEARTS,Rank.EIGHT)
    self.maindeck.append(EoH)
    EoS = Card(Suit.SPADES,Rank.EIGHT)
    self.maindeck.append(EoS)
    EoC = Card(Suit.CLUBS,Rank.EIGHT)
    self.maindeck.append(EoC)
    NoD = Card(Suit.DIAMONDS,Rank.NINE)
    self.maindeck.append(NoD)
    NoH = Card(Suit.HEARTS,Rank.NINE)
    self.maindeck.append(NoH)
    NoS = Card(Suit.SPADES,Rank.NINE)
    self.maindeck.append(NoS)
    NoC = Card(Suit.CLUBS,Rank.NINE)
    self.maindeck.append(NoC)
    TeoD = Card(Suit.DIAMONDS,Rank.TEN)
    self.maindeck.append(TeoD)
    TeoH = Card(Suit.HEARTS,Rank.TEN)
    self.maindeck.append(TeoH)
    TeoS = Card(Suit.SPADES,Rank.TEN)
    self.maindeck.append(TeoS)
    TeoC = Card(Suit.CLUBS,Rank.TEN)
    self.maindeck.append(TeoC)
    JoD = Card(Suit.DIAMONDS,Rank.JACK)
    self.maindeck.append(JoD)
    JoH = Card(Suit.HEARTS,Rank.JACK)
    self.maindeck.append(JoH)
    JoS = Card(Suit.SPADES,Rank.JACK)
    self.maindeck.append(JoS)
    JoC = Card(Suit.CLUBS,Rank.JACK)
    self.maindeck.append(JoC)
    QoD = Card(Suit.DIAMONDS,Rank.QUEEN)
    self.maindeck.append(QoD)
    QoH = Card(Suit.HEARTS,Rank.QUEEN)
    self.maindeck.append(QoH)
    QoS = Card(Suit.SPADES,Rank.QUEEN)
    self.maindeck.append(QoS)
    QoC = Card(Suit.CLUBS,Rank.QUEEN)
    self.maindeck.append(QoC)
    KoD = Card(Suit.DIAMONDS,Rank.KING)
    self.maindeck.append(KoD)
    KoH = Card(Suit.HEARTS,Rank.KING)
    self.maindeck.append(KoH)
    KoS = Card(Suit.SPADES,Rank.KING)
    self.maindeck.append(KoS)
    KoC = Card(Suit.CLUBS,Rank.KING)
    self.maindeck.append(KoC)
  def create_pile(self,pilename,num_of_cards):
    pile = []
    for _ in range(num_of_cards):
      card = random.choice(self.maindeck)
      self.maindeck.remove(card)
      pile.append(card)
    self.piles[pilename] = pile
  def add_random_to_pile(self,pilename):
    card = random.choice(self.maindeck)
    self.maindeck.remove(card)
    self.piles[pilename].append(card)
  def print_pile(self,pilename): #prints
    print('[',end='')
    for card in self.piles[pilename]:
      try:
        index = self.piles[pilename].index(card) + 1
        _ = self.piles[pilename][index]
      except:
        end = ''
      else:
        end = ', '
      print(card.cardname,end=end)
    print(']',end='\n')
  def pile_string(self,pilename):
    string = '['
    for card in self.piles[pilename]:
      try:
        index = self.piles[pilename].index(card) + 1
        _ = self.piles[pilename][index]
      except:
        end = ''
      else:
        end = ', '
      string = string+card.cardname+end
    string = string+']\n'
    return string
