# 0 - import and global variables
import random
suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':11}

game_on = True

# 1 - creating cards
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + ' of ' + self.suit

# 2 - creating deck
class Deck:
    def __init__(self):
        self.cards_deck = []
        for suit in suits:
            for rank in ranks:
                self.cards_deck.append(Card(suit, rank))
    def shuffle(self):
        random.shuffle(self.cards_deck)
    def deal_one(self):
        dealt_card =  self.cards_deck.pop()
        return dealt_card

# 3 - welcome/greeting
def game_welcome():
    print('Welcome to BlackJack! Are you ready to lose?')
    

# 4 - creating hand - values / ace values
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        
    def adjust_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# 5 - hit or stand functions

def hit(deck,hand):
    hand.add_card(deck.deal_one())
    hand.adjust_ace()

def hit_or_stand(deck,hand):
    global game_on
    
    while True:
        ask_hit = input('Hit or stand? H for hit, S for stand.: ')

        if ask_hit == 'H':
            hit(deck,hand)
        elif ask_hit == 'S':
            print(f'Player stands. Dealer is playing.')
            game_on = False
        else:
            print('Wrong answer, please try again!')
            continue
        break

# 6 - show cards function (in this case, i did not wanted to hide the dealer first card, as it's just a simple code)
def show_cards(player,dealer):
    print("\nDealer's hand:", *dealer.cards, sep= '\n')
    print("\nDealer's sum =", dealer.value)
    print("\nPlayer's hand:", *player.cards, sep= '\n')
    print("\nPlayer's sum =", player.value)

# 7 - endgame printing functions
def player_bust(player,dealer):
    print('Player busts! Dealer wins!')
def player_win(player,dealer):
    print('Player wins!')
def dealer_bust(player,dealer):
    print('Dealer busts! Player wins!')
def dealer_win(player,dealer):
    print('Dealer wins!')
def draw(player,dealer):
    print("Player and dealer tie! It's a draw!")

# 8 - game logic

while True:
    # greeting
    game_welcome()
    # create deck and shuffle
    deck = Deck()
    deck.shuffle()

    # deal 2 cards for player and dealer
    player_hand = Hand()
    player_hand.add_card(deck.deal_one())
    player_hand.add_card(deck.deal_one())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal_one())
    dealer_hand.add_card(deck.deal_one())

    # show each cards
    show_cards(player_hand,dealer_hand)
    
    # game ready to begin
    while game_on: 
        # run a check to see if hands bustes at first 2 deals
        if player_hand.value > 21 and dealer_hand.value <= 21:
            player_bust(player_hand, dealer_hand)

            break
        # repeat check for dealer
        elif dealer_hand.value > 21 and player_hand.value <= 21:
            dealer_bust(player_hand, dealer_hand)

            break
        else:
            pass
        # hit or stand - player
        hit_or_stand(deck, player_hand)
        # show cards after hit or stand
        show_cards(player_hand,dealer_hand)

    # condition - if player hasnt busted, dealer has to hit until 17
    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        # show cards after hits
        show_cards(player_hand,dealer_hand)

        # win conditions - printing who wins
        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand)
        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand, dealer_hand)
        elif player_hand.value > dealer_hand.value:
            player_win(player_hand, dealer_hand)
        else:
            draw(player_hand, dealer_hand)
    # replay
    new_game = input('Would you like to play again? Y for Yes, N for no!' )
    if new_game == 'Y':
        game_on = True
        continue
    else:
        print('Thank you for playing with us!')
        break

