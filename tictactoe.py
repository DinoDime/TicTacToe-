def print_board(board):
    print(board[1],"|",board[2],"|",board[3])
    print("---------")
    print(board[4], "|", board[5], "|", board[6])
    print("---------")
    print(board[7], "|", board[8], "|", board[9])

def game():
    board = ['*', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    gameintro()

    while True:
        print_board(board)
        user1choice = getuser1choice()
        updateboard(board, user1choice, 'O')
        flag = checkforwinner(board)  # Add 2 condition 1
        if flag == 1:
            print("Player 1 wins!")
            break
        elif flag == 2:
            print("Player 2 wins!")
            break
        print_board(board)
        user2choice = getuser2choice()
        updateboard(board, user2choice, 'X')
        flag = checkforwinner(board)  # Add 2 condition 1
        if flag == 1:
            print(user1, " wins!")
            break
        elif flag == 2:
            print(user2, " wins!")
            break

def gameintro():
    print("Welcome to Tic Tac Toe!")
    user1 = input("User 1, please type your name: ")
    user2 = input("User 2, please type your name: ")
    print(user1, " your marker is O")
    print(user2, " your marker is X")

def getuser1choice():
    choice1 = input(user1, "where do you want to place your O? ")
    choice1 = int(choice1)
    return choice1

def getuser2choice():
    choice2 = input(user2, "where do you want to place your X? ")
    choice2 = int(choice2)
    return choice2

def user_choice_y_n():
    choice = input("Do you play again? Please press y for yes or n for no: ")
    return choice

def updateboard(board, userchoice, sign):
    board[userchoice] = sign

def checkforwinner(board):
    flag = 0
    if (board[1]==board[2] and board[2]==board[3] and board[3]=='O'): flag = 1
    elif (board[1]==board[2] and board[2]==board[3] and board[3]=='X'): flag = 2
    elif (board[4]==board[5] and board[5]==board[6] and board[6]=='O'): flag = 1
    elif (board[4]==board[5] and board[5]==board[6] and board[6]=='X'): flag = 2
    elif (board[7]==board[8] and board[8]==board[9] and board[9]=='O'): flag = 1
    elif (board[7]==board[8] and board[8]==board[9] and board[9]=='X'): flag = 2
    elif (board[1]==board[4] and board[4]==board[7] and board[7]=='O'): flag = 1
    elif (board[1]==board[4] and board[4]==board[7] and board[7]=='X'): flag = 2
    elif (board[2]==board[5] and board[5]==board[8] and board[8]=='O'): flag = 1
    elif (board[2]==board[5] and board[5]==board[8] and board[8]=='X'): flag = 2
    elif (board[3]==board[6] and board[6]==board[9] and board[9]=='O'): flag = 1
    elif (board[3]==board[6] and board[6]==board[9] and board[9]=='X'): flag = 2
    elif (board[1]==board[5] and board[5]==board[9] and board[9]=='O'): flag = 1
    elif (board[1]==board[5] and board[5]==board[9] and board[9]=='X'): flag = 2
    elif (board[3]==board[5] and board[5]==board[7] and board[7]=='O'): flag = 1
    elif (board[3]==board[5] and board[5]==board[7] and board[7]=='X'): flag = 2
    return flag

if __name__ == "__main__":
    game()

    while True:
        choice_y_n = user_choice_y_n()
        if choice_y_n == 'n':
            print("Exiting Tic Tac Toe")
            exit()
        elif choice_y_n == 'y':
            game()
        else:
            print("Invalid input!")