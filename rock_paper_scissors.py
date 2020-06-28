from random import randint
player_wins = 0
computer_wins = 0
winning_score = int(input("How many rounds do you want to play? "))


def display_header():
    print(f"Player score: {player_wins} Computer score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")


def pick_computer_move():
    moves = {
        1: 'rock',
        2: 'paper',
        3: 'scissors'
    }
    computer_number = randint(1, 3)
    computer_choice = moves.get(computer_number)
    print(f"The computer plays: {computer_choice}")
    return computer_choice


def calculate_winner(player, computer):
    global player_wins
    global computer_wins
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


def start_game(winning_score):
    while player_wins < winning_score and computer_wins < winning_score:
        display_header()
        player = input("Enter your choice: ").lower()
        if player == 'q' or player == 'quit':
            break
        computer = pick_computer_move()
        calculate_winner(player, computer)


def display_winner():
    if player_wins > computer_wins:
        print("CONGRATS, YOU WON!")
    elif player_wins == computer_wins:
        print("IT'S A TIE!")
    else:
        print("OH NO! THE COMPUTER WON...")
    print(f"Player score: {player_wins} Computer score: {computer_wins}")


start_game(winning_score)
display_winner()
