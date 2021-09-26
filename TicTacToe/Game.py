import turtle
import time
class Game:

	'''
	>>> grid = Game()
	>>> grid.get_grid()
	[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

	>>> grid.move(1, 1)
	>>> grid.get_grid()
	[[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

	>>> grid.move(2, 2)
	>>> grid.get_grid()
	[[0, 1, -1, 0, -1], [1, 1, 0, 0, 0], [-1, 0, -1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

	>>> grid.move(1, 1)
	'position already taken'

	>>> grid.move(0, 1)
	'position out of bounds'

	>>> grid.set_grid()
	'''
	def __init__(self):
		#printing the game introdution
		print()
		print("WELCOME TO A NEW GAME")
		#initializing the turtle
		self.bob = turtle.Turtle()
		#setting up the game window
		self.setup_draw()

		#creating the 3 by 3 game grid
		self.grid = [[0]*5 for i in range(5)]
		#setting the turn to player 1
		self.moved = 1

	def main_loop(self):
		while self.check_status() == "not done jet":
			print(self.get_grid())
			self.move(int(input("X")), int(input("Y")))
		if self.check_status() == "player1 won":
			self.draw_win("player1")
		elif self.check_status() == "player2 won":
			self.draw_win("player2")
		elif self.check_status() == "draw":
			self.draw_win("draw")

	def move(self, pos_x=-1, pos_y=-1):
		if pos_x != -1 and pos_y != -1:
			#checking if the move is inside the board
			if pos_x > 0 and pos_y < 4 and pos_y > 0 and pos_y < 4:
				#checking if the position of the move is empty
				if self.grid[pos_y][pos_x] == 0:
					self.grid[pos_y][pos_x] = self.moved
					#setting the turn to the other player
					if self.moved == 1:
						self.draw_cross(pos_x, pos_y)
						self.moved = -1
					elif self.moved == -1:
						self.draw_circle(pos_x, pos_y)
						self.moved = 1
				else:
					return "position already taken"
			else:
				return "position out of bounds"

			self.update()


	def update(self):
		for i in range(1, 4):
				self.grid[0][i] = self.grid[1][i] + self.grid[2][i] + self.grid[3][i]
				self.grid[i][0] = self.grid[i][1] + self.grid[i][2] + self.grid[i][3]

		self.grid[0][4] = self.grid[3][1] + self.grid[2][2] + self.grid[1][3]
		self.grid[0][0] = self.grid[1][1] + self.grid[2][2] + self.grid[3][3]

	def check_status(self):
		if self.is_space() == True:
			for y in range(5):
				for x in range(5):
					if self.grid[y][x] == 3:
						return "player1 won"
					elif self.grid[y][x] == -3:
						return "player2 won"
			return "not done jet"
		else:
			for y in range(5):
				for x in range(5):
					if self.grid[y][x] == 3:
						return "player1 won"
					elif self.grid[y][x] == -3:
						return "player2 won"
			return "draw"

	def is_space(self):
		for y in range(1, 4):
			for x in range(1, 4):
				if self.grid[y][x] == 0:
					return True
				else:
					pass

		return False

	def set_grid(self, new_grid):
		self.grid = new_grid

	def get_grid(self):
		return self.grid

	def get_player(self):
		return self.moved


	def setup_draw(self):

		self.bob.penup()
		self.bob.goto(-100, 300)
		self.bob.pendown()
		self.bob.goto(-100,-300)
		self.bob.penup()
		self.bob.goto(100, -300)
		self.bob.pendown()
		self.bob.goto(100, 300)
		self.bob.penup()
		self.bob.goto(300, 100)
		self.bob.pendown()
		self.bob.goto(-300, 100)
		self.bob.penup()
		self.bob.goto(-300, -100)
		self.bob.pendown()
		self.bob.goto(300, -100)

	def draw_cross(self, pos_x, pos_y):
		if pos_x == 1:
			x = -280
		elif pos_x == 2:
			x = -80
		elif pos_x == 3:
			x = 120

		if pos_y == 1:
			y = 280
		elif pos_y == 2:
			y = 80
		elif pos_y == 3:
			y = -120

		self.bob.penup()
		self.bob.goto(x, y)
		self.bob.pendown()
		self.bob.goto(x+160, y-160)
		self.bob.penup()
		self.bob.goto(x+160, y)
		self.bob.pendown()
		self.bob.goto(x, y-160)

	def draw_circle(self, pos_x, pos_y):
		if pos_x == 1:
			x = -200
		elif pos_x == 2:
			x = 0
		elif pos_x == 3:
			x = 200

		if pos_y == 1:
			y = 120
		elif pos_y == 2:
			y = -80
		elif pos_y == 3:
			y = -280

		self.bob.penup()
		self.bob.goto(x, y)
		self.bob.setheading(0)
		self.bob.pendown()
		self.bob.circle(80)


	def draw_win(self, player):
		if player != "draw":
			self.bob.clear()
			self.bob.penup()
			#P
			self.bob.goto(-300, 100)
			self.bob.pendown()
			self.bob.goto(-300, 300)
			self.bob.goto(-250, 300)
			self.bob.goto(-250, 200)
			self.bob.goto(-300, 200)
			self.bob.penup()
			#L
			self.bob.goto(-200, 300)
			self.bob.pendown()
			self.bob.goto(-200, 100)
			self.bob.goto(-150, 100)
			self.bob.penup()
			#A
			self.bob.goto(-100, 300)
			self.bob.pendown()
			self.bob.goto(-100, 100)
			self.bob.goto(-100, 200)
			self.bob.goto(-50, 200)
			self.bob.goto(-50, 100)
			self.bob.goto(-50, 300)
			self.bob.goto(-100, 300)
			self.bob.penup()
			#Y
			self.bob.goto(0, 300)
			self.bob.pendown()
			self.bob.goto(25, 200)
			self.bob.goto(25, 100)
			self.bob.goto(25, 200)
			self.bob.goto(50, 300)
			self.bob.penup()
			#E
			self.bob.goto(150, 300)
			self.bob.pendown()
			self.bob.goto(100, 300)
			self.bob.goto(100, 200)
			self.bob.goto(150, 200)
			self.bob.goto(100, 200)
			self.bob.goto(100, 100)
			self.bob.goto(150, 100)
			self.bob.penup()
			#R
			self.bob.goto(200, 100)
			self.bob.pendown()
			self.bob.goto(200, 300)
			self.bob.goto(250, 300)
			self.bob.goto(250, 250)
			self.bob.goto(200, 200)
			self.bob.goto(250, 100)
			self.bob.penup()
			if player == "player1":
				#1
				self.bob.goto(-50, 0)
				self.bob.pendown()
				self.bob.goto(0, 50)
				self.bob.goto(0, -50)
				self.bob.goto(25, -50)
				self.bob.goto(-25, -50)
				self.bob.penup()

			elif player == "player2":
				#2
				self.bob.goto(-50, 50)
				self.bob.pendown()
				self.bob.goto(50, 50)
				self.bob.goto(50, 0)
				self.bob.goto(-50, 0)
				self.bob.goto(-50, -50)
				self.bob.goto(50, -50)
				self.bob.penup()

			#W
			self.bob.goto(-250, -100)
			self.bob.pendown()
			self.bob.goto(-250, -300)
			self.bob.goto(-200, -300)
			self.bob.goto(-200, -150)
			self.bob.goto(-200, -300)
			self.bob.goto(-150, -300)
			self.bob.goto(-150, -100)
			self.bob.penup()
			#O
			self.bob.goto(-100, -100)
			self.bob.pendown()
			self.bob.goto(0, -100)
			self.bob.goto(0, -300)
			self.bob.goto(-100, -300)
			self.bob.goto(-100, -100)
			self.bob.penup()
			#N
			self.bob.goto(50, -300)
			self.bob.pendown()
			self.bob.goto(50, -100)
			self.bob.goto(150, -300)
			self.bob.goto(150, -100)

		elif player == "draw":
			self.bob.clear()
			self.bob.penup()
			#D
			self.bob.goto(-300, 200)
			self.bob.pendown()
			self.bob.goto(-300, -200)
			self.bob.goto(-250, -200)
			self.bob.goto(-200, -100)
			self.bob.goto(-200, 100)
			self.bob.goto(-250, 200)
			self.bob.goto(-300, 200)
			self.bob.penup()
			#R
			self.bob.goto(-150, -200)
			self.bob.pendown()
			self.bob.goto(-150, 200)
			self.bob.goto(-50, 200)
			self.bob.goto(-50, 100)
			self.bob.goto(-150,  0)
			self.bob.goto(-50, -200)
			self.bob.penup()
			#A
			self.bob.goto(0, -200)
			self.bob.pendown()
			self.bob.goto(0, 200)
			self.bob.goto(100, 200)
			self.bob.goto(100, -200)
			self.bob.goto(100, 0)
			self.bob.goto(0, 0)
			self.bob.penup()
			#W
			self.bob.goto(150, 200)
			self.bob.pendown()
			self.bob.goto(150, -200)
			self.bob.goto(225, -200)
			self.bob.goto(225, 50)
			self.bob.goto(225, -200)
			self.bob.goto(300, -200)
			self.bob.goto(300, 200)

		time.sleep(20)


if __name__ == "__main__":
	game = Game()
	game.main_loop()
