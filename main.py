
# This board will be displayed at the start of the game
start_board =[
        ["1","2","3"],
        ["4","5","6"],
        ["7","8","9"]
        ]


# This board will be displayed once the game has started being played
board =[
        ["-","-","-"],
        ["-","-","-"],
        ["-","-","-"]
        ]


# This prints out the initial board 
def start_game_board():
    print(start_board[0][0] + "|" + start_board[0][1]+ "|"+ start_board[0][2])
    print(start_board[1][0] + "|" + start_board[1][1]+ "|"+ start_board[1][2])
    print(start_board[2][0] + "|" + start_board[2][1]+ "|"+ start_board[2][2])


# This prints out the board once the game has started being played
def display_game_board():
    print(board[0][0] + "|" + board[0][1]+ "|"+board[0][2])
    print(board[1][0] + "|" + board[1][1]+ "|"+board[1][2])
    print(board[2][0] + "|" + board[2][1]+ "|"+board[2][2])



#global variables
game_still_going = True
winner = None
player = 'X'




#This functions dictates how the game will be played
def play():
    global player
    global game_still_going
    count = 0
    start_game_board()
    while game_still_going:
        print()
        hand_turn(player)
        check_if_game_over()
        flip_player()
        count+=1
        if count == 9:
            game_still_going = False
    
    if winner == "X" or winner == "O":
        print(winner + " won.")
        display_game_board()
        
    elif count == 9:
        print("Tie.")
        display_game_board()


# This function hands the turn to the next player. 
# It also checks if the space is filled and if the user typed in a right input.
def hand_turn(player):
    print(player + "'s turn.")
    range = ["1","2","3","4","5","6","7","8","9"]

    valid = False
    while not valid:
        display_game_board()
        position = input("Please select a number from 1-9: ")
        print()
        while str(position) not in range:
         print()
         display_game_board()
         position = input("Wrong input!Please select a number from 1-9: ")


        if position == "1" or position == "2" or position == "3":
            if board[0][int(position)-1] == "-":
                valid = True
            else:
                print("You cant go there. Go again.")

        elif position == "4" or position == "5" or position == "6":
            if board[1][int(position)-4] == "-":
                valid = True
            else:
                print("Space occupied try a different number")

        elif position == "7" or position == "8" or position == "9":
            if board[2][int(position)-7] == "-":
                valid = True
            else:
                print("Space occupied try a different number")

    if position == "1" or position == "2" or position == "3":
        board[0][int(position)-1] = player
    
    elif position == "4" or position == "5" or position == "6":
        board[1][int(position)-4] = player
    
    elif position == "7" or position == "8" or position == "9":
        board[2][int(position)-7] = player

    

# Checks if game is over.
def check_if_game_over():
    check_win()
    
# Checks if there is a winner
def check_win():
    global winner
    row_winner = check_rows()
    column_winner = check_column()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None
    return


# Checks if there is a winner by rows
def check_rows():
   global game_still_going
   row1 = board[0][0] == board[0][1] == board[0][2] != "-"
   row2 = board[1][0] == board[1][1] == board[1][2] != "-"
   row3 = board[2][0] == board[2][1] == board[2][2] != "-"

   if row1 or row2 or row3:
       game_still_going = False

   if row1:
     return board[0][0]
   elif row2:
     return board[1][0]
   elif row3:
     return board[2][0]

   return


# Checks if there is a winner by columns
def check_column():
   global game_still_going
   col1 = board[0][0] == board[1][0] == board[2][0] != "-"
   col2 = board[0][1] == board[1][1] == board[2][1] != "-"
   col3 = board[0][2] == board[1][2] == board[2][2] != "-"

   if col1 or col2 or col3:
       game_still_going = False

   if col1:
     return board[0][0]
   elif col2:
     return board[0][1]
   elif col3:
     return board[0][2]
   return

# Checks if there is a winner by diagonals
def check_diagonals():
   global game_still_going
   dia1 = board[0][0] == board[1][1] == board[2][2] != "-"
   dia2 = board[0][2] == board[1][1] == board[2][0] != "-"

   if dia1 or dia2:
       game_still_going = False

   if dia1:
     return board[0][0]
   elif dia2:
     return board[0][2]

   return

# Changes the player from X to O
def flip_player():
    global player
    if player == "X":
       player = "O"
    else:
       player = "X"

play()


