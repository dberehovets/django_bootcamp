#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    MY_DECK = []

    def __init__(self):
        for i in SUITE:
            for j in RANKS:
                self.MY_DECK.append(j+i)

    def split_deck(self):
        return self.MY_DECK[:26], self.MY_DECK[26:]

    def shuffle_deck(self):
        shuffle(self.MY_DECK)
        return self.MY_DECK


class Player:
    name = "user"
    hand = []

######################
#### GAME PLAY #######
######################

deck = Deck()
deck.shuffle_deck()

half1, half2 = deck.split_deck()

player = Player()
player.name = input("Please enter name of Player1\n")

computer = Player()
computer.name = "Computer"

print("OK. The cards are dealt! Let's play!")
while(half1 and half2):
    input("Please press Enter to draw a card\n")

    pl_card = half1.pop(0)
    cm_card = half2.pop(0)

    print("Your're holding card " + pl_card)
    print("Computer is holding card " + cm_card)

    if RANKS.index(pl_card[:-1]) > RANKS.index(cm_card[:-1]):
        print("Your card is higher. You take 2 cards!")
        half1 = half1 + [pl_card, cm_card]
    elif RANKS.index(pl_card[0]) < RANKS.index(cm_card[0]):
        print("Computer's card is higher. You lose 1 card.")
        half2 = half2 + [cm_card, pl_card]
    else:
        print("Oh no...")
        break


# Use the 3 classes along with some logic to play a game of war!
