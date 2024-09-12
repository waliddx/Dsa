"""
A stack is a data structure that can hold many elements.
- Think of a stack like a pile of pancakes.

- In a pile of pancakes, the pancakes are both added and removed from the top.
So when removing a pancake, it will always be the last pancake you added.
* This way of organizing elements is called LIFO: Last In First Out.
"""

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, value) -> None:
        ''' function to push element at the end '''
        stack = self.stack
        if value is None:
            raise TypeError("[push] can't push a NoneType value")
        stack.append(value)
    
    def pop(self) -> None:
        ''' function to delete  last element '''
        stack = self.stack
        if not stack:
            print("stack is yet empty!")
            return
        stack.pop()

    def size(self) -> int:
        ''' function to get stack size '''
        stack = self.stack
        if not stack:
            print("stack is yet empty!")
            return
        return len(stack)
    
    def peek(self) -> None:
        ''' function to get last element '''
        stack = self.stack
        if not stack:
            print("stack is yet empty!")
            return
        print(f"Peek: {stack[-1]}")
        return

    def isEmpty(self) -> bool:
        ''' function to check if stack is empty or not '''
        stack = self.stack
        return not bool(stack)

stack = Stack()

