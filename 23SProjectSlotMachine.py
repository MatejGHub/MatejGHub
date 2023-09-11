import random

# Define the symbols for the slot machine
symbols = ["Cherry", "Bell", "Lemon", "Orange", "Plum", "Bar"]

# Function to spin the slot machine
def spin_slot_machine():
    # Spin the wheels and get three random symbols
    return [random.choice(symbols) for _ in range(3)]

# Function to check if the player wins
def check_win(wheels):
    # Check if all three wheels have the same symbol
    return all(wheel == wheels[0] for wheel in wheels)

# Main game loop
while input("Press ENTER to pull the lever...\n") == "":
    # Spin the slot machine
    wheels = spin_slot_machine()

    # Display the results
    print(f"   {' | '.join(wheels)}")

    # Check if the player won and provide feedback
    if check_win(wheels):
        print("Congratulations! You won!")
    else:
        print("Try again. You didn't win this time.")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break