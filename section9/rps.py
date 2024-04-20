import random as rd

print("...rock...\n...paper...\n...scissors")
player1 = input("PLAYER 1 - Enter your choice: ").lower()
player2 = rd.choice(['rock','paper','scissors'] )
if player1 not in ['rock','paper','scissors'] or player2 not in ['rock','paper','scissors']:
    print('Wrong input. Try again :(')
elif player1 == "rock" and player2 == "paper" or player1 == "paper" and player2 == "scissors" or player1 == "scissors" and player2 == "rock":
    print(f"Computer picked {player2} and WINS!")
elif player1 == player2:
    print(f"It's a tie!!!!! P1:{player1} P2:{player2}")
else:
    print(f"PLAYER 1 WINS over computers {player2}!")