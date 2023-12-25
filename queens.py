
def initialize(n,board):
    for key in ["queen","row","col","nwtose","swtone"]:
        board[key]= {}
    for i in range(n):
        board["queen"][i] = -1
        board["row"][i] = 0
        board["col"][i] = 0
    for i in range(-(n-1),n):
        board["nwtose"][i] = 0
    for i in range(2*n-1):
        board["swtone"][i] = 0

def add_queen(i,j,board):
    board["queen"][i] = j
    board["row"][i] = 1
    board["col"][j] = 1
    board["nwtose"][j-i] = 1
    board["swtone"][j+i] = 1

def undo_queeen(i,j,board):
    board["queen"][i] = -1
    board["row"][i] = 0
    board["col"][j] = 0
    board["nwtose"][j-i] = 0
    board["swtone"][j+i] = 0

def free(i,j,board):
    return(    board["row"][i] == 0 
           and board["col"][j] == 0
           and board["nwtose"][j-i] == 0 
           and board["swtone"][j+i] == 0)

def place_queen(i,board):
    n = len(board["row"].keys())
    for j in range(n):
        if free(i,j,board):
            add_queen(i,j,board)
            if i == n-1:
                return True
            else:
                extendsoln = place_queen(i+1,board)
            if extendsoln:
                return True
            else:
                undo_queeen(i,j,board)
    else:
        return False

def print_board(board):
    for row in sorted(board["queen"].keys()):
        print((row,board["queen"][row]))
board={}
number_of_queen= int(input("How many queen: "))
initialize(number_of_queen,board)
if place_queen(0,board):
    print_board(board)