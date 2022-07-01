import os
import tkinter as tk

from game_board import GameBoard
from board_searcher import AlphaBetaAgent

SYM = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E']

'''Section for edit the game'''
ATTACK_VALUE = 1.5
DEFENCE_VALUE = 1.5
DEPTH_AGENT_1 = 1
DEPTH_AGENT_2 = 1
NUMBER_OF_GAMES = 1

class BoardCanvas():
	"""Apply the tkinter Canvas Widget to plot the game board and stones."""
	
	def __init__(self, master=None, height=0, width=0):
		
		# tk.Canvas.__init__(self, master, height=height, width=width)
		# self.draw_gameBoard()
		self.gameBoard = GameBoard()
		self.boardSearcher = AlphaBetaAgent()
		self.boardSearcher.board = self.gameBoard.board
		self.turn = 2
		self.undo = False
		self.depth = 1
		self.prev_exist = False
		self.prev_row = 0
		self.prev_col = 0
		self.winner =False
		self.winner_1_2 = -1


	# def draw_gameBoard(self):
	# 	"""Plot the game board."""
	#
	# 	# 15 horizontal lines
	# 	for i in range(15):
	# 		start_pixel_x = (i + 1) * 30
	# 		start_pixel_y = (0 + 1) * 30
	# 		end_pixel_x = (i + 1) * 30
	# 		end_pixel_y = (14 + 1) * 30
	# 		self.create_line(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y)
	#
	# 	# 15 vertical lines
	# 	for j in range(15):
	# 		start_pixel_x = (0 + 1) * 30
	# 		start_pixel_y = (j + 1) * 30
	# 		end_pixel_x = (14 + 1) * 30
	# 		end_pixel_y = (j + 1) * 30
	# 		self.create_line(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y)
	#
	# 	# place a "star" to particular intersections
	# 	self.draw_star(3,3)
	# 	self.draw_star(11,3)
	# 	self.draw_star(7,7)
	# 	self.draw_star(3,11)
	# 	self.draw_star(11,11)
	#
	#
	# def draw_star(self, row, col):
	# 	"""Draw a "star" on a given intersection
	#
	# 	Args:
	# 		row, col (i.e. coord of an intersection)
	# 	"""
	# 	start_pixel_x = (row + 1) * 30 - 2
	# 	start_pixel_y = (col + 1) * 30 - 2
	# 	end_pixel_x = (row + 1) * 30 + 2
	# 	end_pixel_y = (col + 1) * 30 + 2
	#
	# 	self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill = 'black')
	#
	#
	# def draw_stone(self, row, col):
	# 	"""Draw a stone (with a circle on it to denote latest move) on a given intersection.
	#
	# 	Specify the color of the stone depending on the turn.
	#
	# 	Args:
	# 		row, col (i.e. coord of an intersection)
	# 	"""
	#
	# 	inner_start_x = (row + 1) * 30 - 4
	# 	inner_start_y = (col + 1) * 30 - 4
	# 	inner_end_x = (row + 1) * 30 + 4
	# 	inner_end_y = (col + 1) * 30 + 4
	#
	# 	outer_start_x = (row + 1) * 30 - 6
	# 	outer_start_y = (col + 1) * 30 - 6
	# 	outer_end_x = (row + 1) * 30 + 6
	# 	outer_end_y = (col + 1) * 30 + 6
	#
	# 	start_pixel_x = (row + 1) * 30 - 10
	# 	start_pixel_y = (col + 1) * 30 - 10
	# 	end_pixel_x = (row + 1) * 30 + 10
	# 	end_pixel_y = (col + 1) * 30 + 10
	#
	# 	if self.turn == 1:
	# 		self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='black')
	# 		self.create_oval(outer_start_x, outer_start_y, outer_end_x, outer_end_y, fill='white')
	# 		self.create_oval(inner_start_x, inner_start_y, inner_end_x, inner_end_y, fill='black')
	# 	elif self.turn == 2:
	# 		self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='white')
	# 		self.create_oval(outer_start_x, outer_start_y, outer_end_x, outer_end_y, fill='black')
	# 		self.create_oval(inner_start_x, inner_start_y, inner_end_x, inner_end_y, fill='white')
	#
	#
	# def draw_prev_stone(self, row, col):
	# 	"""Draw the previous stone with single color.
	#
	# 	Specify the color of the stone depending on the turn.
	#
	# 	Args:
	# 		row, col (i.e. coord of an intersection)
	# 	"""
	#
	# 	start_pixel_x = (row + 1) * 30 - 10
	# 	start_pixel_y = (col + 1) * 30 - 10
	# 	end_pixel_x = (row + 1) * 30 + 10
	# 	end_pixel_y = (col + 1) * 30 + 10
	#
	# 	if self.turn == 1:
	# 		self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='white')
	# 	elif self.turn == 2:
	# 		self.create_oval(start_pixel_x, start_pixel_y, end_pixel_x, end_pixel_y, fill='black')


	def gameLoop(self):
		"""The main loop of the game. 
		Note: The game is played on a tkinter window. However, there is some quite useful information 
			printed onto the terminal such as the simple visualizaiton of the board after each turn,
			messages indicating which step the user reaches at, and the game over message. The user
			does not need to look at what shows up on the terminal. 
		
		self.gameBoard.board()[row][col] == 1(black stone) / 2(white stone)
		self.gameBoard.check() == 1(black wins) / 2(white wins)
		
		Args:
			event (the position the user clicks on using a mouse)
		"""

		agent1 = AlphaBetaAgent(depth=DEPTH_AGENT_1)
		agent2 = AlphaBetaAgent(depth=DEPTH_AGENT_2)
		self.winner = False

		while True:
			# START START START START START START START START START START START START
			# Change the turn to the program now

			self.turn = 1
			print('Program is thinking for black now...')

			# Determine the position the program will place a white stone on.
			# Place a white stone after determining the position.

			row, col = agent1.get_action(self.gameBoard, self.turn)
			if row == -1:
				self.winner_1_2 = 0
				print('TIE')
				# self.create_text(240, 500, text='TIE')
				# self.unbind('<Button-1>')
				return 0

			# score, row, col = self.boardSearcher.search(self.turn, self.depth)
			# coord = '%s%s' % (chr(ord('A') + row), chr(ord('A') + col))
			print('Program has moved to ', SYM[row] + SYM[col])  # {}\n'.format(coord))
			self.gameBoard.apply_action((row, col), 1)
			# self.draw_stone(row, col)
			if self.prev_exist == False:
				self.prev_exist = True
			else:
				pass
				# self.draw_prev_stone(self.prev_row, self.prev_col)
			self.prev_row, self.prev_col = row, col
			self.gameBoard.show()
			print('\n')

			# bind after the program makes its move so that the user can continue to play
			# self.bind('<Button-1>', self.gameLoop)

			# If the program wins the game, end the game and unbind.
			if self.gameBoard.check(row, col) == 1:
				print('BLACK WINS.')
				self.winner_1_2 = 1
				# self.create_text(240, 500, text='BLACK WINS')
				# self.unbind('<Button-1>')
				self.winner = True

				return 0

			# END END END END END END END END END END END END END END END END END

			# Change the turn to the program now
			self.turn = 2
			print('Program is thinking for white now...')

			# Determine the position the program will place a white stone on.
			# Place a white stone after determining the position.
			row, col = agent2.get_action(self.gameBoard, self.turn)
			if row == -1:
				print('TIE')
				self.winner_1_2 = 0
				# self.create_text(240, 500, text='TIE')
				# self.unbind('<Button-1>')
				self.winner = True

				return 0
			# row, col = self.boardSearcher.search(self.turn, self.depth)
			# coord = '%s%s' % (chr(ord('A') + row), chr(ord('A') + col))
			print('Program has moved to ', SYM[row] + ',' + SYM[col] ) #{}\n'.format(coord))

			self.gameBoard.apply_action((row, col), 2)
			# self.draw_stone(row, col)
			if self.prev_exist == False:
				self.prev_exist = True
			else:
				pass
				# self.draw_prev_stone(self.prev_row, self.prev_col)
			self.prev_row, self.prev_col = row, col
			self.gameBoard.show()
			print('\n')

			# bind after the program makes its move so that the user can continue to play
			# self.bind('<Button-1>', self.gameLoop)

			# If the program wins the game, end the game and unbind.
			if self.gameBoard.check(row, col) == 2:
				print('WHITE WINS.')
				self.winner_1_2 = 2
				# self.create_text(240, 500, text='WHITE WINS')
				# self.unbind('<Button-1>')
				self.winner = True
				return 0



class BoardFrame():
	"""The Frame Widget is mainly used as a geometry master for other widgets, or to
	provide padding between other widgets.
	"""
	
	def __init__(self, master=None):
		self.create_widgets()

	def create_widgets(self):
		attack = [ATTACK_VALUE]
		defence = [DEFENCE_VALUE]


		for a in attack:
			for d in defence:
				if a == d:

					GameBoard.ATTACK_WEIGHTS = a
					GameBoard.DEFENCE_WEIGHTS = d

					self.boardCanvas = BoardCanvas(height=550, width=480)
					# self.boardCanvas.pack()
					# file_name = "results.txt"
					# f = open(file_name, "w")

					games = dict()
					black_wins = 0
					white_wins = 0
					ties = 0

					num_games = NUMBER_OF_GAMES
					# f.write("The used depth is 2 for agent 1 and 3 for agent 2" + os.linesep)
					# f.write("Start {num_games} games with the weights:"+os.linesep)
					# f.write(str(self.boardCanvas.gameBoard.black_counter.WEIGHTS) + os.linesep)  # only for black
					# f.write(f"attack weights = {self.boardCanvas.gameBoard.ATTACK_WEIGHTS}, defence weights = {self.boardCanvas.gameBoard.DEFENCE_WEIGHTS}"+os.linesep)
					for i in range(num_games):
						self.boardCanvas = BoardCanvas(height=550, width=480)
						# self.boardCanvas.pack()

						while not self.boardCanvas.winner:
							self.boardCanvas.gameLoop()
							if self.boardCanvas.winner_1_2 == 0:
								ties += 1
								games[i] = ("tie", self.boardCanvas.gameBoard.move_counter)
							elif self.boardCanvas.winner_1_2 == 1:
								black_wins += 1
								games[i] = ("black", self.boardCanvas.gameBoard.move_counter)
							elif self.boardCanvas.winner_1_2 == 2:
								white_wins += 1
								games[i] = ("white", self.boardCanvas.gameBoard.move_counter)

					# for i in range(num_games):
					# 	f.write("game number {i + 1}" + str(games[i]) + os.linesep)
					# f.write("there where " + str(black_wins) + "wins for black, " + str(white_wins) + " wins for white and " + str(ties) + " ties" + os.linesep+os.linesep+os.linesep)
					print("there where " + str(black_wins) + " wins for black, " + str(white_wins) + " wins for white and " + str(ties) +  " ties" + os.linesep)

					# f.close()

