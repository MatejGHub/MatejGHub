#Vnesi vrednost večjo od 0 da se program zaključi in ne večjo od 10

while True:
    i = int(input("Value: "))
    if i < 0:
        print("The value is lower than zero")
        continue
    elif i > 10:
        print("The value is higher than 10")
        continue
    elif 0 < i < 10:
        break

for _ in range(i):
    print("Writting value")