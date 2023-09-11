#export
""" 
def main():
    hello("World")
    goodbye("World")

def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye, {name}")


if __name__ == "__main__":
    main()
"""
#newtask export
"""
def add(x, y):
    return x + y
def mul(x, y):
    return x * y
"""
#newtask export
"""
def div(x, y, z):
    return x / y / z
"""
#newtask
"""
import random
import sys

full_name =input("Enter your full name: ")

name_parts = full_name.split()
if len(name_parts) > 0:
    first_name = name_parts[0]
else:
    first_name = "unknown"

print(f"|Welcome, {first_name} this is a random number generator game|")

while True:
    choice = input("|Do you want to generate a number from 1 - 100?|\n          *Press 1 for YES*\n          *Press 2 for NO*")
    
    if choice == "1":
        print("Generating number...")
        random_number = random.randint(1, 100)
        print(random_number)
        break
    elif choice == "2":
        sys.exit()
    else:
        print("Invalid Syntax, try again")


print(f"The program generated the number {random_number},\nI'll close the program now g oodbye{first_name}")
"""
#newtask average of numbers
"""
import sys

while True:
    try:
        num_numbers = int(input("Enter the number of numbers you want to calculate: "))
        break
    except ValueError:
        print("You tried to write a string, try again")
    
num_numbers = int(num_numbers)

while True:
    try:
        if 1 <= num_numbers <= 5:
            print(f"We are going to print {num_numbers} numbers")
            numbers = []

            for i in range(num_numbers):
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                average = sum(numbers) / len(numbers)
            break
        elif num_numbers > 5:
            print("Number too high")
            sys.exit()
        elif num_numbers < 0:
            print("Number too low")
            sys.exit()
        else:
            print("Try again")
    except ValueError:
        print("Wrong Syntax, try again")

print(average)
"""