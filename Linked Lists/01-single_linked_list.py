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
        switched = True
        while switched:
            switched = False
            currentNode = self.head
            while currentNode.next is not None:
                if currentNode.value > currentNode.next.value:
                    currentNode.value, currentNode.next.value = currentNode.next.value, currentNode.value
                    switched = True
                currentNode = currentNode.next
    
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
    
    def merge(self, linked, sorted=False) -> None:
        ''' function to merge two linkedlist 
             - if sorted it True return sorted merged linkedlist
             - if sorted is False return unsorted merged linkedlist
        '''   
        if not self.head:
            self.head = linked.head
            return
        
        currentNode = self.head
        while currentNode.next:
            currentNode = currentNode.next

        # return the None value to the head of the new linked list
        currentNode.next = linked.head

        if sorted:
            self.sort()
        return

node_list = LinkedList()
node_list2 = LinkedList()

node_list.insertNode(5)
node_list.insertNode(6)
node_list.insertNode(9)

node_list2.insertNode(20)
node_list2.insertNode(15)
node_list2.insertNode(7)

node_list.display()
node_list.merge(node_list2, sorted=True)
node_list.display()
