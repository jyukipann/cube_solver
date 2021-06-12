import numpy as np

class State:
	"""
	ルービックキューブの状態を表すクラス
	"""

	def __init__(self, cp, co, ep, eo):
		self.cp = cp
		self.co = co
		self.ep = ep
		self.eo = eo

	def apply_move(self, move):
		"""
		操作を適用し、新しい状態を返す
		"""
		new_cp = [self.cp[p] for p in move.cp]
		new_co = [(self.co[p] + move.co[i]) % 3 for i, p in enumerate(move.cp)]
		new_ep = [self.ep[p] for p in move.ep]
		new_eo = [(self.eo[p] + move.eo[i]) % 2 for i, p in enumerate(move.ep)]
		return State(new_cp, new_co, new_ep, new_eo)

moves_list = {
	'U': State(
		[3, 0, 1, 2, 4, 5, 6, 7],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 2, 3, 7, 4, 5, 6, 8, 9, 10, 11],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
	'D': State(
		[0, 1, 2, 3, 5, 6, 7, 4],
		[0, 0, 0, 0, 0, 0, 0, 0],
		[0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 8],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
	'L': State(
		[4, 1, 2, 0, 7, 5, 6, 3],
		[2, 0, 0, 1, 1, 0, 0, 2],
		[11, 1, 2, 7, 4, 5, 6, 0, 8, 9, 10, 3],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
	'R': State(
		[0, 2, 6, 3, 4, 1, 5, 7],
		[0, 1, 2, 0, 0, 2, 1, 0],
		[0, 5, 9, 3, 4, 2, 6, 7, 8, 1, 10, 11],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
	'F': State(
		[0, 1, 3, 7, 4, 5, 2, 6],
		[0, 0, 1, 2, 0, 0, 2, 1],
		[0, 1, 6, 10, 4, 5, 3, 7, 8, 9, 2, 11],
		[0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0]),
	'B': State(
		[1, 5, 2, 3, 0, 4, 6, 7],
		[1, 2, 0, 0, 2, 1, 0, 0],
		[4, 8, 2, 3, 1, 5, 6, 7, 0, 9, 10, 11],
		[1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0])
}
move_names = []
faces = list(moves_list.keys())
for face_name in faces:
	move_names += [face_name, face_name + '2', face_name + '\'']
	moves_list[face_name + '2'] = moves_list[face_name].apply_move(moves_list[face_name])
	moves_list[face_name + '\''] = moves_list[face_name].apply_move(moves_list[face_name]).apply_move(moves_list[face_name])


class cube:
	def __init__(self,cp,co,ep,eo):
		self.cp = np.array(cp)+1
		self.co = np.array(co)+1
		self.ep = np.array(ep)+1
		self.eo = np.array(eo)+1
		
	def apply_move(self, move):
		self.cp = np.dot(move.cp,self.cp.T)
		self.co = np.mod((np.dot(move.cp,self.co.T)-1 + move.co),3)+1
		self.ep = np.dot(move.ep,self.ep.T)
		self.eo = np.mod((np.dot(move.ep,self.eo.T)-1 + move.eo),2)+1

	def out(self):
		print(self.cp-1)
		print(self.co-1)
		print(self.ep-1)
		print(self.eo-1)

class move:
	def __init__(self,cp,co,ep,eo):
		self.eo = eo
		self.ep = ep
		self.co = co
		self.cp = cp
	"""
	def out(self):
		print(self.cp)
		print(self.co)
		print(self.ep)
		print(self.eo)
	"""



def generate_moves(move_name):
	global moves_list
	cp = np.zeros((8,8),dtype=int)
	for i,p in enumerate(moves_list[move_name].cp):
		cp[i,p] = 1
	co = np.array(moves_list[move_name].co)
	ep = np.zeros((12,12),dtype=int)
	for i,p in enumerate(moves_list[move_name].ep):
		ep[i,p] = 1
	eo = np.array(moves_list[move_name].eo)
	return [cp,co,ep,eo]


moves = {}
for move_name in moves_list.keys():
	moves[move_name] = move(*generate_moves(move_name))

if __name__ == '__main__':
	"""
	for name, move in moves.items():
		print(name)
		print(move)
	"""
	c = cube([i for i in range(8)],[0 for i in range(8)],[i for i in range(12)],[0 for i in range(12)])
	c.out()
	c.apply_move(moves["R2"])
	c.out()
