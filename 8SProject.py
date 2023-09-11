#if, elif, else
#Compare X and Y using statements
#1 Task
x = int(input('Whats X? '))
y = int(input('Whats Y? '))

if x > y:
    print('X is greater than Y')

elif x < y:
    print('X is less than Y')

else:
    print('X is equal to Y')

#Compare two variables
#2 Task
x = input("Enter first variable X: ")
y = input("Enter second variable Y: ")

if x < y or x > y:
    print('X is not equal to Y')
else:
    print('X is equal to Y')


#Enter full name and use statement(if,else)
#3 Task
x = input("Enter your full name: ")


if x == 'Matej Stremfelj':
    print('Hello,', x)

else:
    print('Who on earth are you?')