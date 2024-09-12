"""
A self.stack is a data structure that can hold many elements.
- Think of a self.stack like a pile of pancakes.

- In a pile of pancakes, the pancakes are both added and removed from the top.
So when removing a pancake, it will always be the last pancake you added.
* This way of organizing elements is called LIFO: Last In First Out.
"""

from typing import Union, Any

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value) -> None:
        ''' function to push element at the end '''
        if value is None:
            raise TypeError("[push] can't push a NoneType value")
        self.stack.append(value)
    
    def pop(self) -> Union[int, None]:
        ''' function to delete last element '''
        if not self.stack:
            raise IndexError("[pop] pop from an empty list")
        return self.stack.pop()

    def size(self) -> int:
        ''' function to get stack size '''
        return len(self.stack)
    
    def peek(self) -> Any:
        ''' function to get last element '''
        if not self.stack:
            raise IndexError("[peek] peek from an empty list")
        return self.stack[-1]

    def isEmpty(self) -> bool:
        ''' function to check if self.stack is empty or not '''
        return not bool(self.stack)
    
    def clear(self) -> None:
        ''' function to clear the whole stack '''
        self.stack.clear()

    def contains(self, value=None) -> bool:
        ''' function to check if a value is in the stack '''
        if value is None:
            raise TypeError("[contains] can't search for a NoneType value")
        return value in self.stack
    
    def display(self) -> list:
        ''' function to display the full stack '''
        return self.stack.copy()

# Example usage
stack = Stack()

stack.push(5)
stack.push(6)
stack.push(7)

print(stack.display())  # Output: [5, 6, 7]
print(stack.contains(6))  # Output: True
print(stack.isEmpty())  # Output: False

stack.pop()
print(stack.display())  # Output: [5, 6]
stack.clear()
print(stack.isEmpty())  # Output: True