

choices = ["rock", "paper", "scissors"]
score1 = 0
score2 = 0

for round in range(3):
    print("\nRound", round + 1)
    p1 = input("Player 1 (rock/paper/scissors): ").lower()
    print("\n" * 50)   # hides player 1's choice
    p2 = input("Player 2 (rock/paper/scissors): ").lower()

    if p1 not in choices or p2 not in choices:
        print("Wrong input, round skipped")
    elif p1 == p2:
        print("Draw!")
    elif (p1 == "rock" and p2 == "scissors") or \
         (p1 == "paper" and p2 == "rock") or \
         (p1 == "scissors" and p2 == "paper"):
        print("Player 1 wins this round!")
        score1 += 1
    else:
        print("Player 2 wins this round!")
        score2 += 1

print("\nFinal score -> P1:", score1, " P2:", score2)
if score1 > score2:
    print("Player 1 wins the game!")
elif score2 > score1:
    print("Player 2 wins the game!")
else:
    print("Game is a draw!")