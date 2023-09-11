#Output quotation marks

print('Hello, what\'s your name?')
x = input('My name is: ')
print(x, '"Nice to meet you"')

#F string program

name = input('Input your name: ')
print(f'Why did you say that?, {name}')

#Remove spaces and Capitalize
#Split user's name into first or last name

name = input('Enter you name: ').strip().title()

first, last = name.split(' ')

print(f'Welcome to Python, {first}')