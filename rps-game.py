from random import randint

# TODO:
#	3. "Play again?" feature
#	4. Add players score

# Game
def game(name):

    # User choice
    user_choice = input("Your choice: ").lower()

    # Validate user choice
    if (user_choice != "rock") and (user_choice != "paper") and (user_choice != "scissors"):
        print("Invalid input!")
        game(name)

    # CPU choice
    choice = int(randint(1,3))

    if choice == 1:
        cpu_choice = "rock"
    if choice == 2:
        cpu_choice = "paper"
    else:
        cpu_choice = "scissors"

    print("CPU choice:", cpu_choice)

    # Check if the user choice is the same as the CPU
    if user_choice == cpu_choice:
        return "It's a tie!"
    else:
        result = check_winner(name, user_choice, cpu_choice)

    return result

# Function to check winner
def check_winner(name, user, cpu):

    # Compare choices and select winner
    if (user == "rock" and cpu == "paper") or (user == "scissors" and cpu == "rock") or (user == "paper" and cpu == "scissors"):
        print("CPU is the winner")
        play_again = input("Play again? (Y/N) ").lower()
    else:
        print(name + " is the winner")
        play_again = input("Play again? (Y/N) ").lower()

    if play_again == "y":
       game(name)
    else:
       print("Thank you for playing!")

# Get user name
username = input("Username: ")

game(username)
