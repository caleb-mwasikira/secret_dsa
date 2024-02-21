#!/usr/bin/python3
import random

from data_structures.linked_list import LinkedList


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
    items = random_array(5)

    print(f"Creating new linked list with nodes {items}")
    linked_list = LinkedList(*items)
    print(linked_list)

    random.seed()
    random_index = random.randint(0, linked_list.size())
    new_item, new_items, newer_items = 32, [15, 14], [16, 0, 12]

    print(f"Inserting new node {new_item} at end")
    linked_list.insert_at_end(new_item)
    print(linked_list)

    print(f"Inserting new nodes {new_items} at head")
    linked_list.insert_at_head(*new_items)
    print(linked_list)
    
    print(f"Deleting last node")
    linked_list.delete_last_node()
    print(linked_list)

    try:
        print(f"Inserting new nodes at index {random_index}")
        linked_list.insert_at_middle(random_index, *newer_items)
        print(linked_list)
        
        print(f"Deleting node at index {random_index}")
        linked_list.delete_at_index(random_index)
        print(linked_list)
        
        print(f"Fetching node at index {random_index}")
        node = linked_list.get_node_at_index(random_index)
        print(node)
        print()

        start, stop = -4, -4
        print(f"Getting items b2n indexes {start} -> {stop}")
        items = linked_list.items(start_index=start, stop_index=stop)
        print(items)
        print()

    except IndexError as e:
        print(e)
    
    value = random.choice(newer_items)
    print(f"Fetching node with value: {value}")
    index, node = linked_list.search(value)
    print(f"Index: {index} Node: {node}")
    print()

    print(f"Fetching all node data in linked list")
    print(linked_list.items())
