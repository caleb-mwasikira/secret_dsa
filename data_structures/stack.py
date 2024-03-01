from typing import Optional


class Stack:
    size: int
    top: int
    items: list[int]

    def __init__(self, size: int) -> None:
        self.size = size # number of elements in the Stack
        self.top = -1 # -1 means stack is empty
        self.items = []

    def push(self, item: int) -> bool:
        if not self.is_full():
            self.items.append(item)
            self.top += 1
            return True
        else:
            return False
        
    def pop(self) -> Optional[int]:
        if not self.is_empty():
            value = self.items[self.top] # remove item at the top of the stack
            self.top -= 1 
            return value
        else:
            return None

    def is_full(self):
        return self.top == self.size - 1
    
    def is_empty(self):
        return self.top == -1
    
    def __repr__(self) -> str:
        top_element: Optional[int] = self.items[self.top] if self.top >= 0 else None
        return f"Stack:- size: {self.size} top: {self.top} top_element: {top_element}"
