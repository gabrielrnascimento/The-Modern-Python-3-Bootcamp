print('''
... rock...
... paper...
... scissors...
''')

player1 = input("(enter Player 1's choice): ")
print("*** NO CHEATING *** \n\n" * 10)
player2 = input("(enter Player 2's choice): ")

if player1 != "rock" and player1 != "paper" and player1 != "scissors":
    print("Something went wrong")
elif player2 != "rock" and player2 != "paper" and player2 != "scissors":
    print("Something went wrong")
else:
    if player1 == player2:
        print("It's a tie!")
    elif player1 == "rock" and player2 == "scissors":
        print("player1 wins")
    elif player1 == "paper" and player2 == "rock":
        print("player1 wins")
    elif player1 == "scissors" and player2 == "paper":
        print("player1 wins")
    else:
        print("player2 wins")
