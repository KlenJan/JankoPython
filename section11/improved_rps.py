import random as rd

player_wins = 0
computer_wins = 0
rounds = 0
winning_message = "It's a tie."
print(
    "...rock...\n...paper...\n...scissors\nThe winner will be decided by best of 3!!!"
)
while (rounds) < 3:
    player1 = input("PLAYER 1 - Enter your choice: ").lower()
    player2 = rd.choice(["rock", "paper", "scissors"])
    if player1[0] == "q":
        print("You manually quit the game.")
        break
    if player1 not in ["rock", "paper", "scissors"] or player2 not in [
        "rock",
        "paper",
        "scissors",
    ]:
        print("Wrong input. Try again :(")
    elif (
        player1 == "rock"
        and player2 == "paper"
        or player1 == "paper"
        and player2 == "scissors"
        or player1 == "scissors"
        and player2 == "rock"
    ):
        print(f"Computer picked {player2} and WINS!")
        computer_wins += 1
        rounds += 1
    elif player1 == player2:
        print(f"It's a tie!!!!! P1:{player1} Computer:{player2}")
        rounds += 1
    else:
        print(f"PLAYER 1 WINS over computers {player2}!")
        player_wins += 1
        rounds += 1
print(f"The game is over..... Here are the results after 3 rounds:")
if player_wins > computer_wins:
    winning_message = "PLAYER 1 wins!"
elif computer_wins > player_wins:
    winning_message = "Computer wins!"
print(winning_message)
