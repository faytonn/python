import random

ROWS = 6
COLUMNS = 7

def create_board():
    return [[' ' for _ in range(COLUMNS)] for _ in range(ROWS)]


#Creating the table
#region createTable
def print_board(board):
    print('  ' + '   '.join(map(str, range(1, COLUMNS + 1))))
    print('+' + '---+' * COLUMNS)
    for row in board:
        print('|' + '|'.join(f' {cell} ' for cell in row) + '|')
        print('+' + '---+' * COLUMNS)
#endregion


def is_valid_move(board, col):
    return board[0][col] == ' '

def get_next_open_row(board, col):
    for row in reversed(range(ROWS)):
        if board[row][col] == ' ':
            return row
    return None

def drop_piece(board, row, col, piece):
    board[row][col] = piece

#check the horizontal locations
#region checkHorizontal    
def winning_move(board, piece):
    for c in range(COLUMNS - 3):
        for r in range(ROWS):
            if all(board[r][c + i] == piece for i in range(4)):
                return True
#endregion

#check the vertical locations
#region checkVertical            
    for c in range(COLUMNS):
        for r in range(ROWS - 3):
            if all(board[r + i][c] == piece for i in range(4)):
                return True
#endregion

#check the m>0 slope
#region            
    for c in range(COLUMNS - 3):
        for r in range(ROWS - 3):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
#endregion

#check the m<0 slope
#region            
    for c in range(COLUMNS - 3):
        for r in range(3, ROWS):
            if all(board[r - i][c + i] == piece for i in range(4)):
                return True

    return False
#endregion


def is_board_full(board):
    return all(board[0][col] != ' ' for col in range(COLUMNS))

def player_move(board):
    while True:
        try:
            col = int(input("Player 1 (X), choose a column (1-7): ")) - 1
            if col < 0 or col >= COLUMNS:
                print("Invalid column. Try again.")
            elif not is_valid_move(board, col):
                print("Column is full. Try again.")
            else:
                row = get_next_open_row(board, col)
                drop_piece(board, row, col, 'X')
                break
        except ValueError:
            print("Please enter a valid number.")

def computer_move(board):
    # Simple AI: Random valid move
    valid_columns = [col for col in range(COLUMNS) if is_valid_move(board, col)]
    col = random.choice(valid_columns)
    row = get_next_open_row(board, col)
    drop_piece(board, row, col, 'O')
    print(f"Computer (O) chooses column {col + 1}")

def play_game():
    board = create_board()
    game_over = False
    print("Welcome to Connect Four!")
    print_board(board)

    while not game_over:
        # Player 1 move
        player_move(board)
        print_board(board)
        if winning_move(board, 'X'):
            print("Congratulations! You win!")
            game_over = True
            break
        elif is_board_full(board):
            print("The game is a tie!")
            break

        # Computer move
        computer_move(board)
        print_board(board)
        if winning_move(board, 'O'):
            print("Computer wins! Better luck next time.")
            game_over = True
            break
        elif is_board_full(board):
            print("The game is a tie!")
            break

if __name__ == "__main__":
    play_game()