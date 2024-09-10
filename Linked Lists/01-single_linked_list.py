"""
A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer.
The way they are linked together is that each node points to where in the memory the next node is placed.
"""
from typing import Union
class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def insert_node(self, value) -> None:
        '''function to insert a new node to the linked list'''
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        currentNode = self.head
        while currentNode:
            if currentNode.next is None:
                currentNode.next = node
                break
            currentNode = currentNode.next
            
    def display(self) -> None:
        ''' function to display nodes value found in linked list'''
        currentNode = self.head
        while currentNode:
            print(f"{currentNode.value}", end=" -> ")
            currentNode = currentNode.next
        if self.head:
            print("None")
    
    def length(self) -> int:
        ''' function to get the length of the linked list '''
        total = 0
        currentNode = self.head
        while currentNode:
            total += 1
            currentNode = currentNode.next
        return total
    
    def find(self, index=None) -> None:
        ''' function to find a Node by it's index '''
        length = self.length()
        if index is not None:
            # raise typeerror if index is not an int datatype
            if type(index) is not int:
                raise TypeError("[error] index is not an integer")

            # raise indexerror if index is out of range
            elif index >= length or index < 0:
                raise  IndexError("[find] Index outof range")

        else:
            index = length - 1
        
        currentNode = self.head
        current_idx = 0
        while currentNode:
            if current_idx == index:
                print(f"node at index: {index} is {currentNode.value}")
                return 
            currentNode = currentNode.next
            current_idx += 1
    
    def find_index_by_value(self, val=None) -> Union[str, int, None]:
        ''' function to return index of first val found in linkedlist'''
        if val is None:
            raise TypeError("[find_index_by_value] val parameters is a Nonetype")
        
        if self.head is None:
            return "linked list is empty"
        
        currentNode = self.head
        current_idx = 0

        while currentNode:
            if currentNode.value == val:
                return  current_idx
            current_idx += 1
            currentNode = currentNode.next
        return  None

    def clear(self):
        self.head = None
        return
    
    def remove(self, index=None) -> None:
        ''' function to erase a Node by it's index '''
        length = self.length()
        if index is None:
            index = length - 1
        
        # raise TypeError if index passed is not integer
        if not isinstance(index, int):
            raise TypeError(f"[erase] function expects an integer in 'index'")
        
        # raise IndexError if index passed is out of range
        if index < 0 or index >= length:
            raise IndexError("[erase] index out of range")
        
        # erase first node simply
        if index == 0:
            self.head = self.head.next
            return
        
        # traverse to the last node before the one to be erased
        currentNode = self.head
        for _ in range(index-1):
            currentNode = currentNode.next

        # check if the next node is not None
        if currentNode.next:
            currentNode.next = currentNode.next.next

    def remove_by_value(self, val=None) -> None:
        if val is None:
            raise TypeError("[remove_by_value] this function expects one argument")
        if not self.head:
            return 
        
        while self.head and self.head.value == val:
            self.head = self.head.next

        currentNode = self.head

        while currentNode and currentNode.next:
            if currentNode.next.value == val:
                currentNode.next = currentNode.next.next
            else:
                currentNode = currentNode.next
 
    def sort(self, reverse=False) -> None:
        ''' function to sort nodes from smallest int to biggest '''
        switched = True
        while switched:
            switched = False
            currentNode = self.head
            while currentNode.next is not None:
                if currentNode.value > currentNode.next.value:
                    currentNode.value, currentNode.next.value = currentNode.next.value, currentNode.value
                    switched = True
                currentNode = currentNode.next
        if reverse:
            #if reverse is True reverse the sorted linkedlist
            self.reverse()
    
    def reverse(self) -> None:
        ''' function to reverse a linked list '''
        previousNode = None
        currentNode = self.head

        while currentNode:
            # store next node in a temporary variable and replace it with previousNode
            next_node = currentNode.next
            currentNode.next = previousNode

            # initialize previousNode and currentNode step ahead
            previousNode = currentNode
            currentNode = next_node
        # initialize the head with the last truthy element in the linked list
        self.head = previousNode

    def reverse_between(self, left=None, right=None) -> None:
        ''' function to reverse a chosen part from left to right of the linkedlist '''
        length = self.length()

        # raise error if left and right are not integeres
        if not isinstance(left, int) and not isinstance(right, int):
            raise TypeError("[reverse_between] expected integersfor 'left' and 'right'")

        # swap index if left bigger than right to avoid conflict
        if left > right:
            left, right = right, left

        # raise error if left and right are not in the linkedlist range
        if left < 0 or right >= length or left > right:
            raise IndexError("[reverse_between] indexes are out of range")
        
        # no need to go through loops if left = right
        if left == right:
            return
        
        # add dummy node to make process easier
        dummy = Node(0, self.head)

        left_previous = dummy

        # reach the node at position "left"
        for _ in range(left):
            left_previous = left_previous.next

        # reverse from left to right
        currentNode = left_previous.next
        previous = None
        for _ in range(right-left+1):
            nextNode = currentNode.next
            currentNode.next = previous

            previous = currentNode
            currentNode = nextNode
        
        # update pointers 
        left_previous.next.next = currentNode
        left_previous.next = previous

        if left == 0:
            self.head = previous       
    
    def merge(self, linked, sorted=False) -> None:
        ''' function to merge two linkedlist 
             - if sorted it True return sorted merged linkedlist
             - if sorted is False return unsorted merged linkedlist
        '''   
        if not self.head:
            self.head = linked.head
            return
        
        currentNode = self.head
        while currentNode:
            currentNode = currentNode.next

        # return the None value to the head of the new linked list
        currentNode.next = linked.head

        if sorted:
            self.sort()
        
node_list = LinkedList()
node_list2 = LinkedList()

node_list.insert_node(8)
node_list.insert_node(5)
node_list.insert_node(6)
node_list.insert_node(5)
node_list.insert_node(7)
node_list.insert_node(5)

node_list2.insert_node(31)
node_list2.insert_node(58)
node_list2.insert_node(0)
node_list2.insert_node(2)
node_list2.insert_node(13)

node_list.display()
node_list.remove_by_value(5)
node_list.display()
