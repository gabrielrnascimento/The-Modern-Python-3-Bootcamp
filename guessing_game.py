from random import randint

choice = "y"
options = ["y", "n"]

while choice == "y":
    random_number = randint(1, 10)
    guess = int(input("Guess a number between 1 and 10: "))
    while guess != random_number:
        if guess > random_number:
            print("Too high, try again!")
            guess = int(input("Guess a number between 1 and 10: "))
        else:
            print("Too low, try again!")
            guess = int(input("Guess a number between 1 and 10: "))
    print("You guessed it! You won!")
    choice = input("Do you want to play again? (y/n) ")
    while choice not in options:
        print("Invalid option")
        choice = input("Do you want to play again? (y/n) ")
print("Thanks for playing. Bye!")
