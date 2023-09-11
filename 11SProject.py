#Create a list
name = input("What's your name? ")

if name in ["Harry", "Hermione", "Ron", "Ginny", "Fred", "George", "Neville", "Lavender", "Parvati", "Seamus"]:
    print("Gryffindor")
elif name in ["Draco", "Severus", "Bellatrix", "Narcissa", "Lucius", "Regulus", "Pansy", "Vincent", "Blaise", "Theodore"]:
    print("Slytherin")
elif name in ["Cedric", "Nymphadora", "Pomona", "Newt", "Tonks", "Ernie", "Hannah", "Susan", "Justin", "Zacharias"]:
    print("Hufflepuff")
elif name in ["Luna", "Cho", "Filius", "Padma", "Terry", "Marietta", "Michael", "Roger", "Mandy", "Lisa"]:
    print("Ravenclaw")
else:
    print("Unknown house")