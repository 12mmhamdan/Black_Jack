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

    
    def show_rows(self):
        return [
            '┌───────┐',
            f'| {self.card_title:<2}    |',
            '|       |',
            f'|   {self.suit}   |',
            '|       |',
            f'|    {self.card_title:>2} |',
            '└───────┘'
        ]
    
    def hidden_rows():
        return [
            '┌───────┐',
            '|░░░░░░░|',
            '|░░░░░░░|',
            '|░░░░░░░|',
            '|░░░░░░░|',
            '|░░░░░░░|',
            '└───────┘'
        ]

class Game:
    def __init__(self):
        self.deck = []
        self.show_dealer_card = False
        self.dealer = Player('bobert')
        self.player = Player('kevin')

    def shuffle(self):
        self.deck = [Card(suit, card_value) for suit in suits for card_value in card_values]
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
    # Player's hand
        print("Player has:")
        rows = [''] * 7
        for card in self.player.hand:
            card_display = card.show_rows()
            for i in range(7):
                rows[i] += card_display[i]

        for row in rows:
            print(row)
        print(f"Total value: {self.player.value}\n")

        # Dealer's hand
        print("Dealer has:")
        rows = [''] * 7
        for i, card in enumerate(self.dealer.hand):
            if i == 1 and not self.show_dealer_card:  # Hide the dealer's second card
                card_display = Card.hidden_rows()
            else:
                card_display = card.show_rows()

            for i in range(7):
                rows[i] += card_display[i]

        for row in rows:
            print(row)
        if self.show_dealer_card:
            print(f"Total value: {self.dealer.value}\n")
        else:
            print(f"Total value: ??\n")

# find value of each player's 2 cards
# If dealer hand <= 17 must hit
# if player < 21 provide hit, stand options
# check if player OR dealer = 21, blackjack winner
# check if player OR dealer > 21, game over
# if hit, append value of new card to hand
# if stand, pass until dealer over 17
# compare sum of card value - highest not over 21 wins
# input would you like to play again?
    
    def play_again(self):
        while True:
            response = input("Would you like to play again? (y/n): ").lower()
            if response == 'y':
                clear_output()
                self.reset()
                self.shuffle()
                self.deal()
                self.display()
                self.action()
                break
            elif response == 'n':
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
    
    def reset(self):
        clear_output()
        self.player = Player('Moataz')
        self.dealer = Player('Bobert')
        self.show_dealer_card = False
    
    
    clear_output()
    def action(self):
        print(f"\nHey welcome to the BlackJack table!\n")
        while True:
            response = input("Would you like to hit? Choose 'y' or 'n' ").lower()
            if response == 'y':
                self.hit(self.player)
                clear_output()
                self.display()
                if self.player.value > 21:
                    print("Bust! You lose!")
                    self.play_again()
                    break
            elif response == 'n':
                self.show_dealer_card = True
                self.stand()
                clear_output()
                self.display()

                if self.dealer.value > 21 or self.player.value > self.dealer.value:
                    print("You win!")
                elif self.dealer.value == self.player.value:
                    print("You lose!")
                else:
                    print("You lose!")

                self.play_again()
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