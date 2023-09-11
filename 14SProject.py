"""
Write a program where you input a number and print out the word based on the number
"""
#while True:
#    n = int(input("Write number: "))
#    if n < 0:
#        continue
#    else:
#        break


#for i in range(n):
#    n = print("Meow")

"""
Write a program where you write a number between 1-5 and then guess the number
"""
#while True:
#    random_number = int(input("Enter a random number between 1-5:"))
#    if 1 <= random_number <= 5:
#        break  # Exit the loop when a valid number is provided
#    else:
#        print("The number is invalid, try again")

# Guess a number between 1-5
#for i in range(random_number):
#    guess = int(input("Guess the number between 1-5:"))
#    if guess == random_number:
#        print("Congratulations! You guessed the number correctly.")
#        break

"""
Write a program where you must guess a number to break the loop out of 100
"""

#while True:
#    random_number = int(input("Enter a random number between 1-10: "))
#    if 0 < random_number <= 10:
#        break
#    else:
#        print("The number you entered is invalid")


#for number in range(random_number):
#    guess = int(input("Guess the random number from 1 to 10: "))
#    if guess == random_number:
#        print("You guessed the random number, ", random_number)
#        break
#    else: 
#        print("Try again")

"""
Define some functions
"""
#def main():
#    number = get_number()
#    meow(number)

#def get_number():
#    while True:
#        n = int(input("Enter n: "))
#        if n > 0:
#            return n
    
#def meow(n):
#    random_word = input("Enter a random word: ")
#    for _ in range(n):
#        print(random_word)
#
#main()

#Rewrite
#def main():
#    number = get_number()
#    meow(number)

#def get_number():
#    n = int(input("What's n? "))
#    if n > 0:
#        return n
    
#def meow(n):
#    random_word = input("Enter random word: ")
#    for i in range(n):
#        print(random_word)

#main()

#def main():
#    number = get_number()
#    word(number)

#def get_number():
#    n = int(input("What's number n? "))
#    if 0 < n < 10:
#        return n
    
#def word(n):
#    Random_word = input("What's the word you want to print? ")
#    for i in range(n):
#        print(Random_word)

#main()

#import random

#random_number = random.randint(1, 10)

#while True:
#    random_n = int(input("Select a random number 1 - 10: "))
#    if 0 < random_n < 10:
#        break

#while True:
#    if random_number == random_n:
#        print("You guessed the right number! ")
#        break
#    elif random_n > random_number:
#        print("The number is too high: ")
#        random_n = int(input("Select a random number 1 - 10: "))
#    else: 
#        random_n < random_number
#        print("The number is too low: ")
#        random_n = int(input("Select a random number 1 - 10: "))

#play_again = int(input("Press 1 to play again or 2 to stop: "))

#def convert_temperature(n):
#    temp_fah = temperature()
#    print("It's ", temp_fah, "fahrenheit outside")
    

#def temperature():
#    temp_cel = int(input("Enter celsius: "))
#    temp_fah = int(temp_cel * 9/5) + 32
#    return temp_fah

#n = int
#convert_temperature(n)

