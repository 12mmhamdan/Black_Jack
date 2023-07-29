import random
import os

def clear_output():
    os.system("cls" if os.name == "nt" else "clear")

# ----------------------------------------------------------
# Create a deck of 52 cards 
# Shuffle the deck
# Ask the Player for their bet
# Make sure that the Player’s bet does not exceed their available chips
# Deal two cards to the Dealer and two cards to the Player
# Show only one of the Dealer’s cards, the other remains hidden
# Show both of the Player’s cards
# Ask the Player if they wish to Hit, and take another card
# If the Player’s hand doesn’t Bust (go over 21) , ask if they’d like to Hit again
# If a Player Stands, play the Dealer’s hand. The dealer will always Hit until the Dealer’s value meets or exceeds 17
# Determine the winner and adjust the Player’s chips accordingly
# Ask the Player if they’d like to play again
# ----------------------------------------------------------
# determine suits or just numbers?

# Create a card Class    

suits = ("♥", "♦", "♣", "♠")
card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'K': 10, 'Q': 10, 'A': 11}

class Card:
    def __init__(self, suit, card_title):
        self.suit = suit
        self.card_title = card_title
        self.card_value = card_values[card_title]

    def __repr__(self):
        return f"<{self.card_title} of {self.suit}"

    def show(self):
        print('┌───────┐')
        print(f'| {self.card_title:<2}    |')
        print('|       |')
        print(f'|   {self.suit}   |')
        print('|       |')
        print(f'|    {self.card_title:>2} |')
        print('└───────┘')

class Game:
    def __init__(self):
        self.deck = []
        self.shuffle()
        self.dealer = Player('bobert')
        self.player = Player('kevin')

    def shuffle(self):
        self.deck = []
        for suit in suits:
            for card_value in card_values:
                self.deck.append(Card(suit, card_value))
        random.shuffle(self.deck)

    def deal(self):
        for i in range(2):
            dealt_card = self.deck.pop()
            self.player.hand.append(dealt_card)
            self.player.value += dealt_card.card_value
            if dealt_card.card_title == 'A':
                self.player.aces += 1

            dealt_card = self.deck.pop()
            self.dealer.hand.append(dealt_card)
            self.dealer.value += dealt_card.card_value
            if dealt_card.card_title == 'A':
                self.dealer.aces += 1

# If the hand contains an ace, subtract 10 if the total is > 21

    def adjust_for_ace(self, player):
        while player.value > 21 and player.aces:
            player.value -= 10
            player.aces -= 1

    def hit(self, player):
        card = self.deck.pop()
        player.hand.append(card)
        player.value += card.card_value
        if card.card_title == 'A':
            player.aces += 1
        self.adjust_for_ace(player)

    def stand(self):
        while self.dealer.value < 17:
            self.hit(self.dealer)

    def display(self):
        for card in self.player.hand:
            card.show()
        print(f"Player has: {self.player.value}\n\n")
        for card in self.dealer.hand:
            card.show()
        print(f"Dealer has: {self.dealer.value}\n")

# find value of each player's 2 cards
# If dealer hand <= 17 must hit
# if player < 21 provide hit, stand options
# check if player OR dealer = 21, blackjack winner
# check if player OR dealer > 21, game over
# if hit, append value of new card to hand
# if stand, pass until dealer over 17
# compare sum of card value - highest not over 21 wins
# input would you like to play again?
    clear_output()
    def action(self):
        print("\nHi friend! It's time to play blackjack!!\n")
        while True:
            response = input("Would you like to: 1. Hit, or 2. Stand? ").lower()
            if response == 'hit' or response == '1' or response == 'h':
                clear_output()
                self.hit(self.player)
                self.display()
                if self.player.value > 21:
                    print("Bust! You lose.")
                    break
            elif response == 'stand' or response == '2' or response == 's':
                clear_output()
                self.stand()
                self.display()
                if self.dealer.value > 21 or self.player.value > self.dealer.value:
                    print("You win!")
                elif self.dealer.value == self.player.value:
                    print("You lose!")
                else:
                    print("You lose!")
                break
            else:
                print(f"'{response.title()}' is not one of the available options. Please select 'hit' or 'stand'.")

# Create a deck
# Create 'shuffle' which would be a random from import
# Create a hand for dealer and for player
# Betting option, $$ or chips, (I like chips if we can)
# Take a bet
# Hit, stand, bust

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.value = 0
        self.aces = 0

game = Game()
game.shuffle()
game.deal()
game.display()
game.action()
