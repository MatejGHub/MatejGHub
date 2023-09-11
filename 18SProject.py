#task
"""
import random

def flip_coin():
    while True:
        coin = random.choice(["heads", "tails"])
        print(f"You flipped {coin}")

        replay_game = input("Press 1 to play again\nPress 2 to Exit game")
        if replay_game == 1:
            return coin
        elif replay_game ==2:
            print("Exiting game")
            break
        else:
            print("Error, try again")


flip_coin()  
"""
#newtask
"""
import random

random_number = random.randint(1, 10)

print(random_number)
"""
#newtask
""""
import random

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(, card)
"""
#newtask
"""
import statistics

print(statistics.mean([100, 90]))
"""
#newtask
"""
import sys

try:
    print("Hello my name is", sys.argv[1])
except IndexError: 
    print("Not enough arguments")
"""
#newtask
"""
def print_list(greeting_list):
   print(greeting_list)

def greetings():
   greeting_list = ["Hello", "Goodbye"]
   return greeting_list

my_list = greetings()
print_list(my_list)
"""
