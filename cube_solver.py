import numpy
from cubeutil import cube, moves
import time

class cube_solver:
	def __init__(self, scramble):
		self.cube = cube([i for i in range(8)],[0 for i in range(8)],[i for i in range(12)],[0 for i in range(12)])
		self.moves = moves
		self.scrambled_moves = ""
		self.applied_moves = ""
		self.scramble(scramble)

	def scramble(self,scramble):
		self.scramble_move = scramble.split(" ")
		self.cube = cube([i for i in range(8)],[0 for i in range(8)],[i for i in range(12)],[0 for i in range(12)])
		for move_name in scramble.split(" "):
			self.cube.apply_move(self.moves[move_name])

	def solve(self):
		self.cross()
		self.f2l()
		self.oll()
		self.pll()

	def cross(self):
		pass

	def f2l(self):
		pass

	def oll(self):
		pass

	def pll(self):
		pass

	def result(self):
		pass

#　持ち替えの実装


if __name__ == '__main__':
	solver = cube_solver("L D2 R U2 L F2 U2 L F2 R2 B2 R U' R' U2 F2 R' D B' F2")
	solver.cube.out()