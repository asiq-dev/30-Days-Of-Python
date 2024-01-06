# 1) Write a generator that generates prime numbers in a specified range.

def gen_primes(limit):
    for number in range(2, limit):
        for divisor in range(2, number):
            if number % divisor == 0:
                break
        else:
            yield number

limit = int(input("Enter limit number for check prime number: "))
prime = gen_primes(limit)

print(*prime, sep=",")


# 2) Below we have an example where map is being used to process names in a list. Rewrite this code using a generator expression.
# names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
# names = map(lambda name: name.strip().title(), names)

names = [" rick", " MORTY  ", "beth ", "Summer", "jerRy    "]
names = (name.strip().title() for name in names )
print(*names, sep=",")



# 3 Write a small program to deal cards for a game of Texas Hold'em.
import itertools
import random
ranks = (2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king", "ace")
suits = ("clubs", "diamonds", "hearts", "spades")


# cards = [] # its a way to create our deck of cards
# for rank in ranks:
#     for suit in suits:
#         cards.append((rank, suit))

# cards = [(rank, suit) for suit in suits for rank in ranks]  # its a way to create our deck of cards

def get_players():
    while True:
        number_of_players = input("How many players are there? ").strip()

        try:
            number_of_players = int(number_of_players)
        except ValueError:
            print("You must enter an integer.")
        else:
            if number_of_players in range(2, 11):
                return number_of_players
            elif number_of_players < 2:
                print("You must have at least 2 players.")
            else:
                print("You can have a maximum of 10 players.")
                

def suffle_deck(cards):
    deck = list(cards)
    random.shuffle(deck)
    return iter(deck)


cards = list(itertools.product(ranks, suits))
