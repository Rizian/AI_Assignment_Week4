board = [[' ', ' ', ' ',],
         [' ', ' ', ' ',],
         [' ', ' ', ' ',]]

player_mark = 'o'
computer_mark = 'x'

def reset_board():
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '

    return

def print_board():
    print("  1 2 3")
    print('1 ' + board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print("  -+-+-")
    print('2 ' + board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print("  -+-+-")
    print('3 ' + board[2][0] + '|' + board[2][1] + '|' + board[2][2])
    print("\n")

    return

def space_is_free(row, col):
    if (board[row][col] == ' '):
        return True
    
    return False

def play_move(move, row, col):
    if space_is_free(row, col):
        board[row][col] = move
        print_board()

        if check_draw():
            print("Draw!")
            quit()

        if check_win():
            if move == 'x':
                print("Computer Wins!")
                quit()
            elif move == 'o':
                print("Player Wins!")
                quit()

    else:
        print("Invalid move. Try again.")

        row = int(input("Row: "))
        col = int(input("Column: "))
        
        play_move(move, row, col)

def check_draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    
    return True

def check_win():
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != ' ':
            return True
    
    #check columns
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != ' ':
            return True

    #check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    
    return False

def check_winning_mark(mark):
    # check rows
    for row in range(3):
        if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] == mark:
            return True
    
    #check columns
    for col in range(3):
        if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] == mark:
            return True

    #check diagonals
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == mark:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == mark:
        return True
    
    return False
    
def player_move():
    print("Player Turn:")

    row = int(input("Row: "))
    col = int(input("Column: "))

    print("\n")
    play_move(player_mark, row - 1, col - 1)

    return

def computer_move():
    print("Computer Turn:")

    best_score = -1000
    best_move_row = 0
    best_move_column = 0

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = computer_mark
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if (score > best_score):
                    best_score = score
                    best_move_row = row
                    best_move_column = col
    
    play_move(computer_mark, best_move_row, best_move_column)

    return

def minimax(board, depth, maximize: bool):
    if check_winning_mark(computer_mark):
        return 10
    elif check_winning_mark(player_mark):
        return -10
    elif check_draw():
        return 0
    
    if maximize:
        best_score = -1000

        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = computer_mark
                    score = minimax(board, 0, False)
                    board[row][col] = ' '
                    if (score > best_score):
                        best_score = score

        return best_score
    else:
        best_score = 1000

        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = player_mark
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    if (score < best_score):
                        best_score = score

        return best_score

reset_board()
print_board()
while not check_win():
    computer_move()
    player_move()