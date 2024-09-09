"""
A Linked List is, as the word implies, a list where the nodes are linked together. Each node contains data and a pointer.
The way they are linked together is that each node points to where in the memory the next node is placed.
"""
class Node:
    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None) -> None:
        self.head = head
    
    def insertNode(self, value) -> None:
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
        print("null")
        return
    
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
                raise TypeError("'error' index is not an integer")

            # raise indexerror if index is out of range
            elif index >= length or index < 0:
                raise  IndexError("'find' Index out of range")

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
        return

    def erase(self, index=None) -> None:
        ''' function to erase a Node by it's index '''
        length = self.length()
        if index is None:
            index = length - 1
        
        # raise TypeError if index passed is not integer
        if not isinstance(index, int):
            raise TypeError("'erase' index is not an integer")
        
        # raise IndexError if index passed is out of range
        if index < 0 or index >= length:
            raise IndexError("'erase' index out of range")
        
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

    def sort(self) -> None:
        ''' function to sort nodes from smallest int to biggest '''
        currentNode = self.head
        while currentNode:
            minNode = currentNode
            temp = currentNode.next
            while temp:
                if temp.value < minNode.value:
                    temp.value, minNode.value = minNode.value, temp.value
                temp = temp.next
            currentNode = currentNode.next
        return
    
    def reverse(self) -> None:
        ''' funtion to reverse a linked list '''
        length = self.length()
        if length <= 1:
            return 
        
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
        return 


node_list = LinkedList()

node_list.insertNode(5)
node_list.insertNode(6)
node_list.insertNode(9)
node_list.insertNode(21)
node_list.insertNode(1)
node_list.insertNode(8)

node_list.display()
node_list.find()
node_list.erase()
node_list.display()
