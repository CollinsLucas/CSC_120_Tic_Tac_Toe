import sqlite3

connection = sqlite3.connect('C:/Users/colli/sqlite/databases/BoardGame.db')

print("SQLITE3 Connection Established")

board = {'7': '-' , '8': '-' , '9': '-' , 
        '4': '-' , '5': '-' , '6': '-' ,
        '1': '-' , '2': '-' , '3': '-' }

board_keys = []

for key in board:
    board_keys.append(key)

def print_board(board):
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])
    print('- + - + -')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('- + - + -')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])

def show_winner(turn):
    if turn != 0:    
        print("\nGame Over.\n")                
        print(turn + " won.")
    else:
        print("\nGame Over.\n")                
        print("It's a Tie!!")

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        print_board(board)
        print("It's your turn, " + turn + ". Move to which place?")

        move = input()        

        if board[move] == '-':
            board[move] = turn
            count += 1
        else:
            print("Choose a space that is not taken.\nMove to which place?")
            continue

        if count >= 5:
            if board['7'] == board['8'] == board['9'] != '-':
                print_board(board)
                show_winner(turn)             
                break
            elif board['4'] == board['5'] == board['6'] != '-':
                print_board(board)
                show_winner(turn)
                break
            elif board['1'] == board['2'] == board['3'] != '-':
                print_board(board)
                show_winner(turn)
                break
            elif board['1'] == board['4'] == board['7'] != '-':
                print_board(board)
                show_winner(turn)
                break
            elif board['2'] == board['5'] == board['8'] != '-':
                print_board(board)
                show_winner(turn)
                break
            elif board['3'] == board['6'] == board['9'] != '-':
                print_board(board)
                show_winner(turn)
                break 
            elif board['7'] == board['5'] == board['3'] != '-':
                print_board(board)
                show_winner(turn)
                break
            elif board['1'] == board['5'] == board['9'] != '-':
                print_board(board)
                show_winner(turn)
                break 

        if count == 9:
            show_winner(0)

        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        reset_game()

def reset_game():
    for key in board_keys:
            board[key] = "-"
    game()

if __name__ == "__main__":
    game()
