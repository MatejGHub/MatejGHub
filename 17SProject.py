#try:
#    x = int(input("What's X? "))
#    print(f"x is {x}")
#except ValueError:
#    print("x is not an intiger, try again ")

#while True:
#    try:
#        x = int(input("What's X? "))
#    except ValueError:
#        print("X is not an intiger, try again")
#    else:
#        break

#print(f"x is {x}")


#while True:
#    try:
#        x = int(input("Enter X: ")) 
#        print(f"You have entered the number {x} do you want to input another number?")
#        break
#    except ValueError:
#        print("The number is not an intiger")
#        break

        
#if x == x:
#    print("Press 1 for Yes")
#else:
#    print("Press 2 for No")


#while True:
#    print("In this program we will measure your BMI(Body Mass Index), enter information below")
#    try:   
#        height_cm = int(input("What's your height? "))
#        weight_kg = int(input("What's your weight? "))
#    except ValueError:
#        print("The value you entered is invalid")

            
#    print(f"Your BMI is {(height_cm * weight_kg)/100}")    
#    x = int(input("Measure BMI again?\n press 1 for yes\n press 2 for no "))
#    break

#if x  != 1:
#    print("Your program has stopped")
#else: 
#    print("Your program has restarted")

def main():
    x = get_int("What's X?")
    print(f"X is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass

main()
