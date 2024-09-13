"""
Just like previous queue but using LinkedList
"""

from typing import Union, Any

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, head=None):
        self.queue = head
        self.tail = head
        self.len = 0

    def enqueue(self, value: Any) -> None:
        ''' function to add element to the end of queue '''
        if value is None:
            raise TypeError("[enqueue] can't add a NoneType value")
        if not self.queue:
            self.len += 1
            self.queue = self.tail = Node(value)
            return
        
        self.len += 1
        self.tail.next = Node(value)
        self.tail = self.tail.next

    def dequeue(self) -> Any:
        ''' function to remove first element of queue '''
        if not self.queue:
            raise IndexError("[dequeue] can't dequeue from an empty queue")
        prev = self.queue.value
        if not self.queue.next:
            self.len -= 1
            self.queue = self.tail = None
            return prev
        self.len -= 1
        self.queue = self.queue.next
        return prev

    def peek(self) -> Any:
        ''' function return the first element '''
        if not self.queue:
            return None
        return self.queue.value

    def clear(self) -> None:
        ''' function to clear the queue '''
        if not self.queue:
            return
        self.len = 0
        self.queue = self.tail = None
    
    def isEmpty(self) -> bool:
        ''' function to check if queue is empty '''
        return not bool(self.queue)
    
    def size(self) -> int:
        ''' function to return the size of the queue'''
        return self.len
    
    def contains(self, value: Any) -> bool:
        ''' function check if a value is in the queue '''
        if value is None:
            raise TypeError("[contain] can't search for a NoneType value")
        
        if not self.queue:
            return False
        
        if self.queue.value == value:   # No iteration if queue equal value
            return True
        
        if self.tail.value == value:    # No iteration if tail equal value
            return True
        
        currentNode = self.queue
        while currentNode:
            if currentNode.value == value:
                return True
            currentNode = currentNode.next
        return False

    def display(self) -> None:
        ''' function to display all elements in the queue '''
        if not self.queue:
            return None
        currentNode = self.queue
        while currentNode:
            print(currentNode.value, end=" <- ") # arrow to the opposite direction to respect [FIFO] 
            currentNode = currentNode.next
        print("None")

# Example usage
queue = Queue()

queue.enqueue(5)
queue.enqueue(6)
print(queue.peek())     # Output: 5
queue.display()         # Output: 5 <- 6 <- None
print(queue.dequeue())  # Output: 5
queue.display()         # Output: 6 <- None
print(queue.size())     # Output: 1
print(queue.contains(6))# Output: True
