from random import randint

player_wins = 0
computer_wins = 0

rounds = int(input("How many rounds do you want to play? "))
while player_wins < rounds and computer_wins < rounds:
    print('''
    ... rock...
    ... paper...
    ... scissors...
    ''')

    computer_number = randint(1, 3)
    player = input("Enter Player 1's choice: ").lower()
    if player == "quit" or player == "q":
        break
    if computer_number == 1:
        computer = "rock"
    elif computer_number == 2:
        computer = "paper"
    else:
        computer = "scissors"

    print(f"Computer plays {computer}")

    if player != "rock" and player != "paper" and player != "scissors":
        print("You have to choose between rock, paper and scissors")
    else:
        if player == computer:
            print("It's a tie!")
        elif player == "rock" and computer == "scissors":
            print("player wins")
            player_wins += 1
        elif player == "paper" and computer == "rock":
            print("player wins")
            player_wins += 1
        elif player == "scissors" and computer == "paper":
            print("player wins")
            player_wins += 1
        else:
            print("Computer wins")
            computer_wins += 1
print("")
if player_wins > computer_wins:
    print(f"Player wins the best of {rounds}!")
elif player_wins == computer_wins:
    print("The game ended as a Tie!")
else:
    print(f"Computer wins the best of {rounds}!")
print(f'''
The score was:
Player: {player_wins}
Computer: {computer_wins}
''')
