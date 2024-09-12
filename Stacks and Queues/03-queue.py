"""
A queue is a data structure that can hold many elements.
- Think of a queue as people standing in line in a supermarket.
The first person to stand in line is also the first who can pay and leave the supermarket.
* This way of organizing elements is called FIFO: First In First Out.
"""

from typing import Union, Any
from collections import deque   # for better performance in removing elements

class Queue:
    def __init__(self):
        self.queue = deque()
        self.len = 0

    def enqueue(self, value: Any) -> None:
        ''' function to add element to the end of queue '''
        if value is None:
            raise TypeError("[enqueue] can't add a NoneType value")
        self.len += 1
        self.queue.append(value)

    def dequeue(self) -> Any:
        ''' function to remove first element of queue '''
        if not self.queue:
            raise IndexError("[dequeue] can't dequeue from an empty queue")
        self.len -= 1
        return self.queue.popleft() # efficient removal from start

    def peek(self) -> Any:
        ''' function return the first element '''
        if not self.queue:
            return None
        return self.queue[0]

    def clear(self) -> None:
        ''' function to clear the queue '''
        self.len = 0
        self.queue.clear()
    
    def isEmpty(self) -> bool:
        ''' function to check if queue is empty '''
        return not bool(self.queue)
    
    def size(self) -> int:
        ''' function to return the size of the queue'''
        return self.len
    
    def contains(self, value: Any) -> bool:
        ''' function check if a value is in the queue '''
        if value is None:
            raise TypeError("[contain] can't search for a None value")
        return value in self.queue

    def display(self) -> Union[list, None]:
        ''' function to display all elements in the queue '''
        if not self.queue:
            return
        return list(self.queue)

# Example usage
queue = Queue()

queue.enqueue(5)
queue.enqueue(6)
print(queue.display())  # Output: [5, 6]
print(queue.dequeue())  # Output: 5
print(queue.display())  # Output: [6]
print(queue.size())     # Output: 1
print(queue.contains(6)) # Output: True
