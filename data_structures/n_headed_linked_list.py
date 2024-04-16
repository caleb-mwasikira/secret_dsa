from typing import Optional

from data_structures.linked_list import LinkedList
from data_structures.node import Node


class NHeadedLinkedList:
    """
    Implementation of a linked list with more than one head.
    """

    branches: list[LinkedList]
    current_branch: LinkedList

    def __init__(self, branches: dict[str, list[int]]) -> None:
        self.branches: list[LinkedList] = []
        self.current_branch: LinkedList

        if len(branches.items()) == 0:
            raise ValueError("Cannot create an empty branched linked list")

        for key, values in branches.items():
            self.new_branch(branch_name=key, items=values)

        self.current_branch = self.branches[0]
        self.head = self.current_branch.head

    def new_branch(self, items: list[int], branch_name: Optional[str] = None):
        linked_list = LinkedList(*items)
        if branch_name is not None:
            linked_list.name = branch_name

        self.branches.append(linked_list)

    def switch_branch(self, branch_name: str):
        branch = self.get_branch(branch_name)

        if branch is None:
            return

        self.current_branch = branch

    def get_branch(self, branch_name: str) -> Optional[LinkedList]:
        for branch in self.branches:
            if branch.name == branch_name:
                return branch

        return None

    def merge(
        self, branch1_name: str, branch2_name: str, on_nodes: tuple[int, int]
    ) -> bool:
        try:
            # get the two branches to merge together
            from_b = self.get_branch(branch1_name)
            to_b = self.get_branch(branch2_name)
            from_index, to_index = on_nodes

            print(
                f"Merging {from_b.name}@index {from_index} to {to_b.name}@index {to_index}"
            )

            if None in [from_b, to_b]:
                missing_b_name: str = branch1_name if from_b is None else branch2_name
                raise ValueError(f"Merge failed due to missing {missing_b_name} branch")

            # get nodes at from_index and to_index
            from_node = from_b.get_node_at_index(from_index)
            to_node = to_b.get_node_at_index(to_index)

            # merge the two branches
            from_node.next_node = to_node

        except IndexError as e:
            # index access error on linked list
            print(f"Merge failed due to error: {e}")
            return False

    def __repr__(self) -> str:
        list_str_repr: list[str] = []

        for linked_list in self.branches:
            on_current_branch: bool = self.current_branch.name == linked_list.name
            list_str_repr.append(
                f"{'*' if on_current_branch else ''} {linked_list.__repr__()}"
            )

        return "\n".join(list_str_repr)


def find_intersection(
    linked1: LinkedList, linked2: LinkedList
) -> Optional[tuple[int, int]]:
    """Finds the intersection indexes of 2 linked lists

    Args:
        linked1: linked list 1
        linked2: linked list 2

    Returns:
        tuple[int, int]: index of head and head2 that intersect
    """
    # declare a hash-set
    intersections: set[Node] = set()

    # insert all the nodes of one linked list into the hash-set
    linked1_nodes: list[Node] = linked1.items(ret_type=Node)

    for node in linked1_nodes:
        intersections.add(node)

    # now, traverse the other linked list, and for each node check if it is present in the hash-set or not.
    # if the node is present, then that is the required intersection point.
    linked2_nodes: list[Node] = linked2.items(ret_type=Node)

    print(f"Finding intersection b2n linked lists {linked1.name} and {linked2.name}...")
    for node in linked2_nodes:
        if node in intersections:
            index1 = linked1.index_of_node(node)
            index2 = linked2.index_of_node(node)

            if None in [index1, index2]:
                return None
            else:
                return index1, index2 - 1

    return None
