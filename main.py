# Constants
EMPTY = '-'
PLAYER1 = 'X'
PLAYER2 = 'O'
BOARD_SIZE = 3


# Function to print the board
def print_board(board):
    for row in board:
        for cell in row:
            print(cell, end=' ')
        print()


# Function to check if a player has won
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True

    if all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True

    return False


# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if EMPTY in row:
            return False
    return True


# Function to evaluate the score of the board for the AI
def evaluate(board):
    if check_win(board, PLAYER1):
        return 1
    elif check_win(board, PLAYER2):
        return -1
    else:
        return 0


# Function to find the best move using the Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, PLAYER1):
        return 1
    elif check_win(board, PLAYER2):
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = float('-inf')
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER1
                    score = minimax(board, depth + 1, False)
                    board[row][col] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER2
                    score = minimax(board, depth + 1, True)
                    board[row][col] = EMPTY
                    best_score = min(score, best_score)
        return best_score


# Function to make the AI's move
def ai_move(board):
    best_score = float('-inf')
    best_move = None

    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == EMPTY:
                board[row][col] = PLAYER1
                score = minimax(board, 0, False)
                board[row][col] = EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    row, col = best_move
    board[row][col] = PLAYER1


# Function to play the game
def play_game():
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    current_player = PLAYER1

    while True:
        print_board(board)

        if current_player == PLAYER1:
            # Player 1's turn
            row, col = map(int, input("Enter row and column (0-2) for your move: ").split())

            while board[row][col] != EMPTY:
                print("Invalid move. Try again.")
                row, col = map(int, input("Enter row and column (0-2) for your move: ").split())

            board[row][col] = PLAYER1

            if check_win(board, PLAYER1):
                print("You won!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            current_player = PLAYER2
        else:
            # AI's turn
            ai_move(board)
            print("AI makes a move.")

            if check_win(board, PLAYER2):
                print("Player 2 wins!")
                break
            elif is_board_full(board):
                print("It's a tie!")
                break

            current_player = PLAYER1

play_game()
