

class Node:
	def __init__(self, data: int):
		self.data = data
		self.next_node = None

	def __repr__(self):
		if self.next_node is None:
			return f"[Tail: {self.data}]-> ?"
		else:
			return f"[{self.data}]-> "
