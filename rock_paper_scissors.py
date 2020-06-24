from random import randint

print('''
... rock...
... paper...
... scissors...
''')

computer_number = randint(1, 3)
player = input("Enter Player 1's choice: ").lower()

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
    elif player == "paper" and computer == "rock":
        print("player wins")
    elif player == "scissors" and computer == "paper":
        print("player wins")
    else:
        print("Computer wins")
