import random


keep_playing = "y"
random_number = random.randint(1, 10)

while (keep_playing[0] == "y"):
    player_choice = int(input("Pick a number between 1 and 10: "))
    if player_choice == random_number:
        print("Awesome, you got it!")
        keep_playing = input("Do you want to keep playing? \n")
        random_number = random.randint(1, 10)
    elif player_choice < random_number:
        print("Nope, that's not it...try higher")
    elif player_choice > random_number:
        print("Nope, that's not it. Try lower.")

print("Thanks for playing!")
