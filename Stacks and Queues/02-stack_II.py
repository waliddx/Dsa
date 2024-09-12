"""
Just like previous stack but using LinkedList
"""

from typing import Any

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, head=None):
        self.head = self.tail = None
        self.len = 0

    def push(self, value: Any) -> None:
        ''' function to push element at the end '''
        if value is None:
            raise TypeError("[push] can't push a NoneType value")
        
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
            self.len += 1
            return
        
        self.tail.next = node
        self.tail = self.tail.next
        self.len += 1

    def pop(self) -> None:
        ''' function to delete last element '''
        if not self.head:
            raise IndexError("[pop] pop from an empty stack")
        
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            currentNode = self.head
            while currentNode.next != self.tail:
                currentNode = currentNode.next
            currentNode.next = None
            self.tail = currentNode
        self.len -= 1

    def size(self) -> int:
        ''' function to get stack size '''
        return self.len
    
    def peek(self) -> Any:
        ''' function to get last element '''
        if not self.head:
            return None
        return self.tail.value

    def isEmpty(self) -> bool:
        ''' function to check if self.stack is empty or not '''
        return self.head is None
    
    def clear(self) -> None:
        ''' function to clear the whole stack '''
        self.head = self.tail = None
        self.len = 0

    def contains(self, value: Any) -> bool:
        ''' function to check if a value is in the stack '''
        if not self.head:
            return False
        
        if value is None:
            raise TypeError("[contains] can't search for a NoneType value")
        
        currentNode = self.head
        while currentNode:
            if currentNode.value == value:
                return True
            currentNode = currentNode.next
        return False
    
    def display(self) -> None:
        ''' function to display the full stack '''
        if not self.head:
            return
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        if self.head:
            print(None)

# Example usage
stack = Stack()

stack.push(5)
stack.push(6)
stack.push(7)

stack.display()  # Output: 5 -> 6 -> 7 -> None
stack.pop()
stack.display()  # Output: 5 -> 6 -> None
print(stack.contains(5))  # Output: True
print(stack.peek())  # Output: 6
stack.clear()
print(stack.isEmpty())  # Output: True
print(stack.size())
