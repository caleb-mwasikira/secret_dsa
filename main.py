#!/usr/bin/python3
import random
from data_structures.n_headed_linked_list import LinkedList
from data_structures.n_headed_linked_list import NHeadedLinkedList, find_intersection

def random_array(len: int, min: int = 0, max: int = 10) -> list[int]:
    arr = []

    if len < 0 or min > max:
        return arr

    random.seed()
    for _ in range(0, len):
        rand_num = random.randint(min, max)
        arr.append(rand_num)

    return arr


if __name__ == "__main__":
    branches: dict[str, list[int]] = {
        "main": random_array(10),
        "other": random_array(8),
    }

    # creating our NHeadedLinkedList
    n_headed_linkedlist = NHeadedLinkedList(branches)
    print(f"Initial state: \n{n_headed_linkedlist}\n")

    # select random node indexes to merge in main and other branches
    from_index = random.randint(0, len(branches["main"]))
    to_index = random.randint(0, len(branches["other"]))

    # merging other banch to main on specified node indexes
    n_headed_linkedlist.merge("other", "main", (from_index, to_index))
    print(f"After merge: \n{n_headed_linkedlist}\n")

    # finding intersection
    branches: list[LinkedList] = n_headed_linkedlist.branches
    branch1, branch2 = branches[0], branches[1]
    intersect = find_intersection(branch1, branch2)

    if intersect is None:
        print(f"No intersection found b2n {branch1.name} and {branch2.name}")
    else:
        index1, index2 = intersect
        print(
            f"Intersection found at {branch1.name}@index {index1} and {branch2.name}@index {index2}"
        )
