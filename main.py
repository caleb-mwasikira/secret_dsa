#!/usr/bin/python3
import random

from data_structures.linked_list import LinkedList
from data_structures.n_headed_linked_list import NHeadedLinkedList, find_intersection


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
	main_branch = random_array(10)
	other_branch = random_array(8)

	# Create new branches here
	branches: dict[str, list[int]] = {
		"main": main_branch,
		"other": other_branch,
	}

	# Creating our NHeadedLinkedList
	five_head = NHeadedLinkedList(branches)
	print(f"Before merge: \n{five_head}")
	print()

	# Change these values to merge one branch to another at specific nodes
	from_b, to_b = "other", "main"
	merge_from_index = random.randint(0, len(other_branch))
	merge_to_index = random.randint(0, len(main_branch))

	# Merging other branch to main
	five_head.merge(from_b, to_b, (merge_from_index, merge_to_index))
	print(f"After merge: \n{five_head}")
	print()

	# Finding intersection
	branches: list[LinkedList] = five_head.branches
	branch1, branch2 = branches[0], branches[1]
	intersect = find_intersection(branch1, branch2)

	if intersect is None:
		print(f"No intersection found b2n {branch1.name} and {branch2.name}")
	else:
		index1, index2 = intersect
		print(f"Intersection found at {branch1.name}@index {index1} and {branch2.name}@index {index2}")

	# TODO: To prove that the branches (linked_lists) in five_head are merged we do 2 things:
	# 1. Change nodes before merge and check that other branches are unaffected
	# 2. Change nodes after merge and check that other branches reflect the changes
