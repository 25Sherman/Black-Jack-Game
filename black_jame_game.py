#
#
#
#  Work of Milan Grewal
#
#
#


####################################################################################################################
# Class Setup
####################################################################################################################

import random
import turtle
from turtle import *

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


print("The Game you are about to play is called Blackjack. The rules are simple:")
print()
print("- You will be dealt a hand of cards and so will the dealer")
print("- Both of you will try to get a hand value as close as or equal to 21")
print("- However, don't go over 21 or you will but")
print("- Your start with a balance of $500. Don't lose all your money!")
print("This is a special version of Blackjack where Aces are only counted as 11, not 1.")
print()
print("As a player the options given to you throughout the game are: ")
print()
print("- Starting/Stopping the Game")
print("- Placing a bet")
print("- Hitting or Staying")
print("- Playing again")
print()
print("Have fun!")
print()


################################
# This creates the individual cards
#################################
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit


########################################
# This creates a deck using the card class
########################################
class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        '''This function shuffles the cards in the deck'''
        random.shuffle(self.deck)

    def dealer_give(self):
        '''This function gives the dealer a hand of cards'''
        self.dealed_out = self.deck.pop()
        return self.dealed_out

    def card_val(self):
        '''This function find the value of cards being dealed out'''
        val = str(self.dealed_out.rank)
        return values[val]


###################################################
# This class holds all the players actions and values
###################################################
class Player:

    def __init__(self):
        self.bet_amount = 0
        self.bet_valid = True
        self.player_hand = []
        self.player_val = []
        self.player_count = 0
        self.balance = 500
        self.hit_loop = True

    def player_draw(self):
        for x in range(2):
            self.player_hand.append(deck.dealer_give())
            self.player_val.append(deck.card_val())
            print(self.player_hand[x])
            self.player_count = sum(self.player_val)
        print(self.player_count)
        return self.player_hand

    def player_hit(self):

        while self.hit_loop:
            if self.player_count < 21:
                self.hit_choice = input("Would you like to hit (Y) or (N): ").upper()
                if self.hit_choice == "Y":
                    self.player_hand.append(deck.dealer_give())
                    print(self.player_hand[-1])
                    self.player_val.append(deck.card_val())
                    self.player_count = sum(self.player_val)
                    print(self.player_count)

                elif self.hit_choice == "N":
                    return self.player_count
                    break
            elif self.player_count == 21:
                print('You already have 21.')
                return self.player_count
                break
            else:
                # for card in self.player_hand:
                #    if card.rank = 'Ace'
                print('You have busted.')
                return self.player_count
                break

    def make_bet(self):
        while self.bet_valid:
            self.bet_amount = int(input("How much would you like to bet: $"))
            if self.bet_amount > self.balance:
                print("You do not have the funds for that.")
            else:
                self.balance = self.balance - self.bet_amount
                with open("balance.txt", "w") as balance:
                    balance.write("Balance record: " + str(self.balance) + "\n")
                break

        return self.bet_amount


#########################################################
# This class holds all the actions and values of the dealer
#########################################################
class Dealer:

    def __init__(self):
        self.dealer_hand = []
        self.dealer_val = []
        self.dealer_count = 0
        self.visible_count = 0

    def dealer_draw(self):
        for x in range(2):
            self.dealer_hand.append(deck.dealer_give())
            self.dealer_val.append(deck.card_val())
            self.dealer_count += self.dealer_val[x]
        print(self.dealer_hand[-1])
        print("Hidden Card")
        print(self.dealer_val[-1])
        return self.dealer_hand

    def dealer_reveal(self):
        for card in self.dealer_hand:
            print(card)
        print(self.dealer_count)

    # def dealer_turn(self):
    #   print(self.dealer_hand[-1])
    #  print(self.dealer_hand[0])

    def dealer_hit(self):
        self.dealer_hand.append(deck.dealer_give())
        print(self.dealer_hand[-1])
        self.dealer_val.append(deck.card_val())
        self.dealer_count = sum(self.dealer_val)
        print(self.dealer_count)


######################################################################################################################
# Class Setup is done
#####################################################################################################################


#############################
# setting classes to objects
############################
try: #if any issues in the classes or functins then game wont run
    player = Player()
    dealer = Dealer()
    deck = Deck()
    deck.shuffle()
except:
    print("Something wrong with classes or functions")
    exit()


run_program = True

balance = player.balance
print(f'Your balance is ${balance}')
print("\n")

start_game = input("Would you like to start Blackjack (Y) or (N): ").upper()

if start_game == "Y":
    game_on = True
else:
    game_on = False
    run_program = False
    exit()

while run_program:

    player_val = 0
    dealer_val = 0
    bet_amount = 0
    player_hand = []
    dealer_hand = []
    return_val = 1
    run_program = True

    while game_on:

        if balance == 0:
            print("You have no more money.")
            game_on = False
            run_program = False
            break

        bet_amount = player.make_bet()
        balance -= bet_amount
        return_money = bet_amount * 2

        print("\n")
        print("Your balance is $" + str(balance))
        print("\n")
        print("Player Cards: ")
        player_hand = player.player_draw()
        player_val = player.player_count
        print("\n")
        print("Dealer Cards: ")
        dealer_hand = dealer.dealer_draw()
        dealer_val = dealer.dealer_count
        print("\n")

        player_val = player.player_hit()

        # figure out how to end game when bust
        if player_val > 21:
            game_on = False
            break

        print("\n")
        print("Dealer Reveals: ")
        dealer.dealer_reveal()

        print("\n")

        while dealer_val < 17 or dealer_val <= player_val:
            print("Dealer Hits:")
            dealer.dealer_hit()
            dealer_val = dealer.dealer_count
        if dealer_val > 21:
            print("The dealer has busted. You win!")

            ###############################################################################
            #Turtle

            import turtle
            from turtle import *

            t = turtle.Turtle()
            t.color("green")
            t.speed(100)

            t.forward(30)
            # step up to thumb
            for i in range(6):
                t.left(90)
                t.forward(10)
                t.right(90)
                t.forward(10)

            # thumb
            t.left(90)
            t.forward(20)
            t.right(90)
            t.forward(20)
            t.right(90)
            t.forward(50)
            t.right(90)
            t.forward(5)
            t.left(90)
            t.forward(10)
            t.left(90)
            t.forward(40)

            # fingers
            for i in range(5):
                t.right(90)
                t.forward(10)
                t.right(90)
                t.forward(8)
                t.left(180)
                t.forward(8)

            # bottom of hand
            t.right(90)
            t.forward(5)
            t.right(90)
            t.forward(145)
            t.right(90)
            t.forward(45)

            turtle.Screen().exitonclick()


            ###########################################################




            balance += return_money
            game_on = False
        else:
            if player_val > dealer_val:
                print("You won the game.")


                ###############################################################
                #Turtle

                import turtle
                from turtle import *

                t = turtle.Turtle()
                t.color("green")
                t.speed(100)

                t.forward(30)
                # step up to thumb
                for i in range(6):
                    t.left(90)
                    t.forward(10)
                    t.right(90)
                    t.forward(10)

                # thumb
                t.left(90)
                t.forward(20)
                t.right(90)
                t.forward(20)
                t.right(90)
                t.forward(50)
                t.right(90)
                t.forward(5)
                t.left(90)
                t.forward(10)
                t.left(90)
                t.forward(40)

                # fingers
                for i in range(5):
                    t.right(90)
                    t.forward(10)
                    t.right(90)
                    t.forward(8)
                    t.left(180)
                    t.forward(8)

                # bottom of hand
                t.right(90)
                t.forward(5)
                t.right(90)
                t.forward(145)
                t.right(90)
                t.forward(45)

                turtle.Screen().exitonclick()




                #####################################################
                balance += return_money
                game_on = False
            elif player_val == 21 and dealer_val == 21:
                print("You have tied.")
                balance += bet_amount
                game_on = False
            else:
                print("The Dealer won the game.")
                balance -= bet_amount
                game_on = False

    player = Player()
    dealer = Dealer()
    deck = Deck()
    deck.shuffle()
    player_val = 0
    dealer_val = 0
    bet_amount = 0
    player_hand = []
    dealer_hand = []

    play_again = input("Would you like to play again? (Y) or (N): ").upper()

    if play_again == "Y":
        game_on = True
    else:
        game_on = False
        run_program = False