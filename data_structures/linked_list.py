import uuid
from typing import Optional, Union

from data_structures.node import Node


class LinkedList:
	name: str
	head: Optional[Node]

	def __init__(self, *items: int) -> None:
		# Every unnamed linked list is given a unique id
		self.name = str(uuid.uuid4()).split("-")[0]
		self.head = None
		self.insert_at_end(*items)

	@classmethod
	def from_head(cls, head: Node):
		"""Build a linked list from a head node

		Args:
			head (Node): head of linked list

		Returns:
			_type_: LinkedList
		"""
		current_node: Node = head
		node_items: list[int] = []

		while current_node is not None:
			node_items.append(current_node.data)
			current_node = current_node.next_node

		return cls(*node_items)

	def insert_at_head(self, *items: int) -> bool:
		"""Inserts elements at head of linked list"""
		items = list(items)

		if len(items) == 0:
			return False

		# Reversing the array because we want the first element of the items list
		# to be the final head of the linked list.
		# An element will be set as a linked lists final head if it is the last element
		# on the items list.
		for item in items.__reversed__():
			new_node = Node(item)
			new_node.next_node = self.head
			self.head = new_node

		return True

	def insert_at_middle(self, index: int, *items: int) -> bool:
		items = list(items)

		if len(items) == 0:
			return False

		if self.is_empty():
			self.insert_at_end(*items)
			return True

		if not self.within_range(index):
			raise IndexError(f"Index {index} is out of bounds for linked list with range(0, {self.size() - 1})")

		# traverse to node just before the required index of the new node
		middle_node = self.head
		for i in range(0, index - 1):
			if middle_node.next_node is not None:
				middle_node = middle_node.next_node

		# Create a smaller linked list outside main linked list
		tail_node = middle_node.next_node
		smol_head = Node(items.pop(0))
		middle_node.next_node = smol_head

		for item in items:
			new_node = Node(item)
			smol_head.next_node = new_node
			smol_head = new_node

		# Join smaller linked list to the middle-end (middle tail) of linked list
		smol_head.next_node = tail_node
		return True

	def insert_at_end(self, *items: int) -> bool:
		"""Inserts elements at the end of a linked list"""
		items = list(items)

		if len(items) == 0:
			return False

		if self.is_empty():
			data = items.pop(0)
			self.head = Node(data)

		last_node = self.head
		while last_node.next_node is not None:
			last_node = last_node.next_node

		for item in items:
			new_node = Node(item)
			last_node.next_node = new_node
			last_node = new_node

		return True

	def get_node_at_index(self, index: int) -> Node:
		if not self.within_range(index):
			raise IndexError(f"Index {index} is out of bounds for linked list with range(0, {self.size() - 1})")

		# traverse to node just before the required index of the new node
		node = self.head
		for i in range(0, index):
			if node.next_node is not None:
				node = node.next_node

		return node

	def search(self, value: int, ret_type: Union[int, Node] = int) -> Optional[Union[int, Node]]:
		current_node = self.head
		index = 0

		while current_node is not None:				
			if current_node.data == value:
				return current_node.data if ret_type is int else current_node
			
			current_node = current_node.next_node
			index += 1

		return None
	
	def index_of_node(self, node: Node) -> Optional[int]:
		current_node = self.head
		index = 0

		while current_node is not None:				
			if current_node == node:
				return index
			
			current_node = current_node.next_node
			index += 1

		return None

	def delete_last_node(self) -> Optional[Node]:
		if self.is_empty():
			return None

		if self.size() == 1:
			deleted_node = self.head
			self.head = None
			return deleted_node

		# Traverse to the 2nd last node on the linked list
		current_node = self.head
		while current_node.next_node.next_node is not None:
			current_node = current_node.next_node

		# Detach last node by changing the second_last_node.next_node pointer to -> NULL
		deleted_node = current_node.next_node
		current_node.next_node = None
		return deleted_node
	
	def delete_after_index(self, index: int) -> list[int]:
		if not self.within_range(index):
			raise IndexError(f"Index {index} is out of bounds for linked list with range(0, {self.size() - 1})")
		
		# Get all indexes after index
		deleted_nodes = self.items(index + 1)
		
		# Get node at index and change its next_node to point to NULL
		index_node = self.get_node_at_index(index)
		if index_node is not None:
			index_node.next_node = None
		
		return deleted_nodes			

	def delete_at_index(self, index: int) -> Node:
		if not self.within_range(index):
			raise IndexError(f"Index {index} is out of bounds for linked list with range(0, {self.size() - 1})")

		if index == 0:
			deleted_node = self.head
			self.head = self.head.next_node
			return deleted_node

		# traverse to node just before the required index of the new node
		middle_node = self.head
		for i in range(0, index - 1):
			if middle_node.next_node is not None:
				middle_node = middle_node.next_node

		deleted_node = middle_node.next_node
		middle_node.next_node = middle_node.next_node.next_node
		return deleted_node

	def within_range(self, index: int) -> bool:
		if self.is_empty():
			return False
		
		size = self.size()
		return 0 <= index < size

	def is_empty(self) -> bool:
		return self.head is None

	def size(self) -> int:
		"""Counts the number of nodes in the linked list"""
		current_node = self.head
		count = 0

		while current_node is not None:
			count += 1
			current_node = current_node.next_node

		return count

	def items(self, start_index: int = 0, stop_index: Optional[int] = None, ret_type: Union[int, Node] = int) -> list[Union[int, Node]]:
		"""Returns a list of all node data between start_index and stop_index"""
		node_items = []
		last_index = self.size() - 1

		# set -ve start_indexes to 0
		start_index = 0 if start_index < 0 else start_index
		if not self.within_range(start_index):
			start_index = 0

		# set stop_indexes that are None or > size to last available index
		stop_index = last_index if stop_index is None else stop_index
		if not self.within_range(stop_index):
			stop_index = last_index

		# swap start_index and stop_index if start_index > stop_index
		# order does not matter, we are only looking for a valid range
		if start_index > stop_index:
			temp = start_index
			start_index = stop_index
			stop_index = temp

		start_node = self.get_node_at_index(start_index)
		if start_node is None:
			return node_items
			
		current_node = start_node
		index = start_index

		while current_node is not None and index <= stop_index:
			if ret_type is int:
				node_items.append(current_node.data)
			else:
				node_items.append(current_node)

			current_node = current_node.next_node
			index += 1

		return node_items
			
	def __repr__(self):
		nodes: list[str] = []

		if self.is_empty():
			return "[Head: ?]\n"

		current_node = self.head

		while current_node is not None:
			if current_node == self.head:
				nodes.append(f"[Head: {current_node.data}]")
			elif current_node.next_node is None:
				nodes.append(f"[Tail: {current_node.data}] -> ?")
			else:
				nodes.append(f"[{current_node.data}]")

			current_node = current_node.next_node

		return f"{self.name}: " + "->".join(nodes)
