import random

choices = ["r", "p", "s"]

player_choice = input("Choose (r)ock, (p)aper, or (s)cissors: ").lower()

if player_choice not in choices:
    print("Invalid choice!")
    quit()

computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "r":
    if computer_choice == "p":
        print("You lose! Paper covers rock.")
    else:
        print("You win! Rock smashes scissors.")
elif player_choice == "p":
    if computer_choice == "s":
        print("You lose! Scissors cut paper.")
    else:
        print("You win! Paper covers rock.")
elif player_choice == "s":
    if computer_choice == "r":
        print("You lose! Rock smashes scissors.")
    else:
        print("You win! Scissors cut paper.")

print(f"You chose: {player_choice}")
print(f"Computer chose: {computer_choice}")

play_again = input("Play again? (y/n): ").lower()

while play_again == "y":

    player_choice = input("Choose (r)ock, (p)aper, or (s)cissors: ").lower()
    computer_choice = random.choice(choices)


    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "r":
        if computer_choice == "p":
            print("You lose! Paper covers rock.")
        else:
            print("You win! Rock smashes scissors.")
    elif player_choice == "p":
        if computer_choice == "s":
            print("You lose! Scissors cut paper.")
        else:
            print("You win! Paper covers rock.")
    elif player_choice == "s":
        if computer_choice == "r":
            print("You lose! Rock smashes scissors.")
        else:
            print("You win! Scissors cut paper.")

    print(f"You chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    play_again = input("Play again? (y/n): ").lower()


print("Thanks for playing!")
