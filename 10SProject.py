#Parity
#Is the number even or uneven?
x = int(input("What's X: "))

if x % 2 == 0:
    print('The number is even!')
else:
    print('The number is uneven!')

#Partiy program with a function

def main():
    x = int(input("Enter Number: "))
    if if_even(x):
        print("The number is even")
    else:
        print("The number is uneven")

def if_even(number):
    return True if number % 2 == 0 else False
    
main()