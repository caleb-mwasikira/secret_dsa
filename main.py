#!/usr/bin/python3
import random

from data_structures.stack import Stack


def random_array(arr_len: int, min_value: int = 0, max_value: int = 10) -> list[int]:
	rand_arr = []

	if arr_len < 0 or min_value > max_value:
		return rand_arr

	random.seed()
	for _ in range(0, arr_len):
		random_number = random.randint(min_value, max_value)
		rand_arr.append(random_number)

	return rand_arr


if __name__ == "__main__":
	num = 10
	items = random_array(num)

	my_stack = Stack(num)
	print(my_stack)

	print(f"Adding items {items} to stack ...")
	for item in items:
		my_stack.push(item)

	print(my_stack)
	print()

	for i in range(0, 5):
		popped_item = my_stack.pop()
		print(f"Popped item {popped_item} from stack")
		print(my_stack)
		print()
