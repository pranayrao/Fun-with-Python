board = [' ']*10
gameState=True
message = ''

def clear_board():
    global board,gameState
    board = [' ']*10
    gameState=True

def printBoard():
    print " "+board[7]+" | "+board[8]+" | "+board[9]+" "
    print "------------"
    print " "+board[4]+" | "+board[5]+" | "+board[6]+" "
    print "------------"
    print " "+board[1]+" | "+board[2]+" | "+board[3]+" "

def win(board,player):
    if(board[7]==board[8]==board[9]==player) or \
        (board[4]==board[5]==board[6]==player) or \
        (board[1]==board[2]==board[3]==player) or \
        (board[7]==board[4]==board[1]==player) or \
        (board[8]==board[5]==board[2]==player) or \
        (board[9]==board[6]==board[3]==player) or \
        (board[7]==board[5]==board[3]==player) or \
        (board[1]==board[5]==board[9]==player):
            return True
    else:
        return False

def boardFull(board):
    if " " in board[1:]:
        return False
    else:
        return True

def plyr_move(xo):
    global board
    ask= 'Place your mark '+xo+' on\n'
    while True:
        try:
            move=int(raw_input(ask))
        except ValueError:
            print "Incorrect value. Please choose a number between 1 & 9"
            continue
            
        if board[move]==" ":
            board[move]=xo
            break
        else:
            print "This cell is taken"
            continue

def plyrChoice(xo):
    global board,gameState,message
    message=''
    xo=str(xo)
    plyr_move(xo)
    
    if win(board,xo):
        printBoard()
        message=xo+" wins!"
        gameState=False
        
    printBoard()
    
    if boardFull(board):
        message="Tie!"
        gameState=False
        
    return gameState,message

def play():
    clear_board()
    global message
    
    X='X'
    O='O'
    
    while True:
        printBoard()
        
        gameState,message = plyrChoice(X)
        print message
        if gameState==False:
            break
        
        gameState,message = plyrChoice(O)
        print message
        if gameState==False:
            break
            
    rematch = raw_input('Rematch? y/n \n')
    if rematch == 'y':
            play()
    else:
            print "End Game"
