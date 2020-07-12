
board = []
for x in range(10):
    board.append(" ")

def printTitle():
    print()
    print("Welcome to Tic Tac Toe Game!".upper())
    print()
    
def clean_board(board):
    for i in range(10):
        board[i] = " "
    return board

# Checks if there is no more ' ' space to make a move
def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    return True

# Prints the actual board with the moves
def printBoard(board):
    print("------------------------------------")
    print(f"|     {board[1]}     |    {board[2]}     |     {board[3]}     |")
    print("------------------------------------")
    print(f"|     {board[4]}     |    {board[5]}     |     {board[6]}     |")
    print("------------------------------------")
    print(f"|     {board[7]}     |    {board[8]}     |     {board[9]}     |")
    print("------------------------------------")


# Checks if the chosen place in the board is available
def validMove(board, move):
    if board[move] == " ":
        return True
    return False
    

# Return the player choice between 1-9
def playerMove(board):
    while True:
        move = int(input("Choose a board square to play (1-9): "))
        if move in list(range(1,10)):
            if validMove(board, move):
                board[move] = 'X'
                return printBoard(board)
            else:
                print("This board square is already occupied")
        else:
            print("Choose a number between 1 and 9")
# STILL NEED FIXING NOT INT INPUT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<



# Return the computer move based on an algorithm
def compMove(board):
    from random import choice

    # 1. computer win chance
    for i in range(1,10):
        move = i
        if validMove(board, move):
            board[i] = "O"
            if isWinner(board, "O"):
                return printBoard(board)
            else:
                board[i] = " "

    # 2. player win chance (block player)
    for i in range(1,10):
        move = i
        if validMove(board, move):
            board[i] = "X"
            if isWinner(board, "X"):
                board[i] = "O"
                return printBoard(board)
            else:
                board[i] = " "

    # 3. available corners of the board
    corners = [1, 3, 7, 9]
    move = choice(corners)
    if validMove(board, move):
        board[move] = "O"
        return printBoard(board)

    # 4. center of the board (if available)
    if validMove(board, 5):
        board[5] = "O"
        return printBoard(board)

    # 5. random available place
    while True:
        move = choice(list(range(1,10)))
        if validMove(board, move):
            board[move] = "O"
            return printBoard(board)

    """
    algorithm
        1. computer win chance
        2. player win chance (block player)
        3. available corners of the board
        4. center of the board (if available)
        5. random available place
    """

# Checks if whether "O" or "X" wins the game
def isWinner(board, letter):
    if  (board[1] == letter and board[2] == letter and board[3] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or (board[7] == letter and board[8] == letter and board[9] == letter) or (board[1] == letter and board[4] == letter and board[7] == letter) or (board[2] == letter and board[5] == letter and board[8] == letter) or (board[3] == letter and board[6] == letter and board[9] == letter) or (board[1] == letter and board[5] == letter and board[9] == letter) or (board[3] == letter and board[5] == letter and board[7] == letter):
        return True
    return False

def main():
    replay_bool = True
    while replay_bool:
        printTitle()
        clean_board(board)
        printBoard(board)
        while not isWinner(board, "X") and not isWinner(board, "O"):
            playerMove(board)
            if isBoardFull(board):
                break
            compMove(board)
        if isWinner(board, "X"):
            print("X wins")
        elif isWinner(board, "O"):
            print("O wins")
        elif isBoardFull(board):
            print("Tie!")
        replay = input("Do you want to play another round? (y/n) ")
        if replay == "y":
            replay_bool = True
        else:
            replay_bool = False
    print("Thank you for playing!")

main()
