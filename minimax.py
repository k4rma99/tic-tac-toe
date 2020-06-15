'''

AI is powered by Minmax algorithm. Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assuming that your opponent also plays optimally. 
In Minimax the two players are called maximizer and minimizer. The maximizer tries to get the highest score possible while the minimizer tries to do the opposite and get the lowest score possible.

Here, let's say X is USER and O is AI

'''


def current_board_score(board,r,c):

	# Checking for Rows for X or O victory. 
	for row in range(0, r): 
		if board[row][0] == board[row][1] and board[row][1] == board[row][2]: 
			if board[row][0] == 'x': 
				return 10
			elif board[row][0] == 'o': 
				return -10

	# Checking for Columns for X or O victory. 
	for col in range(0, c): 
		if board[0][col] == board[1][col] and board[1][col] == board[2][col]: 
			if board[0][col]=='x': 
				return 10
			elif board[0][col] == 'o': 
				return -10

	# Checking for Major diagonal for X or O victory. 
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]: 
		if board[0][0] == 'x': 
			return 10
		elif board[0][0] == 'o': 
			return -10

	# Checking for Minor diagonal for X or O victory.
	if board[0][2] == board[1][1] and board[1][1] == board[2][0]: 
		if board[0][2] == 'x': 
			return 10
		elif board[0][2] == 'o': 
			return -10
	
	# Else if none of them have won then return 0 
	return 0


def minimax(board,depth,curTurn):
    
    score = current_board_score(board , 3, 3)

    # print("Current board score : ",score)

    if score == 10 : return score # Maximizer has won
    if score == -10: return score # Minimizer has won
    if noMovesRemain(board): return 0 # No more remaining moves

    if curTurn:
        best = -1
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = ai # AI makes a move
                    best = max(best , minimax(board,depth + 1, not(curTurn)))
                    board[i][j] = None
    
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == None:
                    board[i][j] = ai # AI makes a move
                    best = min(best , minimax(board,depth + 1, not(curTurn)))
                    board[i][j] = None

    return best

def bestMove(board,x):

    ai = x

    bestScore = -1
    brow , bcol = -1 , -1

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:

                # print(i,j)

                board[i][j] = ai

                move = minimax(board,0,False)

                if move > bestScore:
                    brow = i
                    bcol = j
                    bestScore = move
                board[i][j] = None

    return brow, bcol

def noMovesRemain(board):
    return True if all([board[i][j] != None for j in range(3) for i in range(3)]) else False


global board , ai
ai = 'x'
board = [   
            ['x','o','x'],
            ['o','o',None],
            [None,None,None]
        ]

current_board_score(board ,3 ,3)
r , c = bestMove(board,ai)

print(r,c)
