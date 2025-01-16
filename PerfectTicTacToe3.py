board = [
[' ',' ',' '],
[' ',' ',' '],
[' ',' ',' ']]

cache = {}

while True:
	answer = input('X or O\n').upper()
	if answer == 'X':
		human = 'X'
		bot = 'O'
		break
	elif answer == 'O':
		human = 'O'
		bot = 'X'
		break
player = human

scores = {bot:10,human:-10, 'Tie':0}

def draw_board(game):
	global board
	print(f'\n\n  {game[0][0]}  |  {game[0][1]}  |  {game[0][2]}  ')
	print('-----------------')
	print(f'  {game[1][0]}  |  {game[1][1]}  |  {game[1][2]}  ')
	print('-----------------')
	print(f'  {game[2][0]}  |  {game[2][1]}  |  {game[2][2]}  ')

def equals3(a,b,c):
	return a == b and b == c and a != ' '

def checkWinner():
	global board
	winner = 'Null'
	#horizontal
	for i in range(3):
		if equals3(board[i][0], board[i][1], board[i][2]):
			winner = board[i][0]
	#vertical
	for i in range(3):
		if equals3(board[0][i], board[1][i], board[2][i]):
			winner = board[0][i]
	#diagonal
	if equals3(board[0][0], board[1][1], board[2][2]):
		winner = board[0][0]

	if equals3(board[2][0], board[1][1], board[0][2]):
		winner = board[2][0]

	openslots = 0
	for i in range(3):
		for j in range(3):
			if board[i][j] == ' ':
				openslots += 1
	if winner == 'Null' and openslots == 0:
		return 'Tie'
	else:
		return winner

def human_move():
	global player, baord
	while True:
		position = input('Choose a number between 1 and 9\n')
		try:
			position = int(position) -1
			if position <= 8 and position >= 0 and board[int(position/3)][position%3] == ' ':
				board[int(position/3)][position%3] = human
				break
		except ValueError:
			continue
	player = bot

def minimax(board, depth, isMaximizing):
	global cache
	try:
		return cache[str((board, isMaximizing))]
	except:
		pass
	result = checkWinner()
	if result != 'Null':
		return scores[result]

	if isMaximizing:
		bestScore = float('-inf')
		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = bot
					score = minimax(board, depth+1, False)
					board[i][j] = ' '
					bestScore = max(score,bestScore)
		cache[str((board, isMaximizing))] = bestScore
		return bestScore

	else:
		bestScore = float('inf')
		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = human
					score = minimax(board,depth+1,True)
					board[i][j] = ' '
					bestScore = min(score, bestScore)
		cache[str((board, isMaximizing))] = bestScore
		return bestScore


def bot_move():
	global player, board
	bestScore = float('-inf')
	for i in range(3):
		for j in range(3):
			if board[i][j] == ' ':
				board[i][j] = bot
				score = minimax(board, 0, False)
				board[i][j] = ' '
				if score > bestScore:
					bestScore = score
					move = (i,j)
	board[move[0]][move[1]] = bot
	player = human

boardex = [
['1','2','3'],
['4','5','6'],
['7','8','9']]

while True:
	if player == human:	
		draw_board(boardex)		
		draw_board(board)
		human_move()

	elif player == bot:
		bot_move()
	

	if checkWinner() != 'Null':
		draw_board(board)
		if checkWinner() != 'Tie':
			print(f'{checkWinner()} has won!')
		else:
			print('Tie')
		break