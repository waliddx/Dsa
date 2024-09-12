"""
A doubly linked list has nodes with addresses to both the previous and the next node, and therefore takes up more memory.
But doubly linked lists are good if you want to be able to move both up and down in the list.
"""

from typing import Union

class Node:
    def __init__(self, value, prev=None, next=None) -> None:
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
        self.tail = head

    def insert(self, value) -> None:
        ''' function to insert a node at the end of the linkedlist '''
        if not self.head:
            self.head = self.tail = Node(value)
            return
        
        self.tail.next = Node(value, self.tail)
        self.tail = self.tail.next
    
    def display(self) -> None:
        ''' function to display all nodes in the linkedlist '''
        currentNode = self.head
        while currentNode:
            print(currentNode.value, end=" -> ")
            currentNode = currentNode.next
        if self.head:
            print("None")
    
    def delete_node_by_value(self, value=None) -> bool:
        ''' Function to delete node by value if it's not None, else delete the last element '''
        if self.head is None:
            return False

        # Delete the last node if value is None
        if value is None:
            if self.tail is None:
                return False
            if self.head == self.tail:  # Only one node
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
            return True

        # Handling the case where the node to delete is the head
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return True
        
        currentNode = self.head
        while currentNode is not None:
            if currentNode.value == value:
                if currentNode == self.tail: 
                    self.tail = currentNode.prev
                    if self.tail:
                        self.tail.next = None
                else:
                    currentNode.prev.next = currentNode.next
                    if currentNode.next:
                        currentNode.next.prev = currentNode.prev
                return True
            currentNode = currentNode.next

        return False
        
node_list = LinkedList()

node_list.insert(5)
# node_list.insert(8)
# node_list.insert(12)
node_list.display()
node_list.delete_node_by_value()
node_list.display()