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
        self.tail = head
    
    def append_node(self, value) -> None:
        ''' function to insert a new node to the end of linked list '''
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
            return
        self.tail.next = node
        self.tail = self.tail.next
    
    def insert_node(self,value, index=None) -> None:
        ''' function to insert node at the given index \n
            if no index was passed it will automatically be inserted at first position
        '''
        if index is not None and index < 0 :
            raise IndexError("[insert_node] index should be greater or equal to '0'")
        
        if not self.head:
            self.head = Node(value)
            return
        
        if index is None or index == 0:
            node = Node(value, self.head)
            self.head = node
            return
        
        node = Node(value)
        current_idx = 0
        currentNode = self.head
        while currentNode and currentNode.next:
            if current_idx == index:
                nextNode = currentNode.next
                currentNode.next = node
                currentNode.next.next = nextNode
                return
            current_idx += 1
            currentNode = currentNode.next
        # insert node at the end if index is greater than the length of linkedlist
        currentNode.next = node     # no need to call append method to avoid looping again over the nodes
            
    def display(self) -> None:
        ''' function to display nodes value found in linked list '''
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
        ''' function to return index of first val found in linkedlist '''
        if val is None:
            raise TypeError("[find_index_by_value] val parameters is a Nonetype")
        
        if self.head is None:
            return "linkedlist is empty"
        
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
        while currentNode.next:
            currentNode = currentNode.next

        # return the None value to the head of the new linked list
        currentNode.next = linked.head

        if sorted:
            self.sort()

    def get_middle(self) -> None:
        ''' function to get the right middle of a linkedlist '''
        fast = self.head
        slow = self.head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        self.head = slow

    def split(self, num=None) -> list:
        ''' function to split linked list into desired parts'''
        if not self.head:
            return [[] for _ in range(num)]
        
        if num is None:
            num = 2
        
        if not isinstance(num, int):
            raise TypeError("[split] expected an integer as an argument")
        
        if num == 0:
            raise ZeroDivisionError("[split] cannot split a list into zero parts")
        
        length = self.length()
        
        parts = length // num
        remaining = length % num

        head_container = []
        currentNode = self.head
        for i in range(num):
            heads_size = parts + (1 if i < remaining else 0)

            child = []
            for j in range(heads_size):
                if currentNode:
                    child.append(currentNode.value)
                    currentNode = currentNode.next
            
            head_container.append(child)

        return head_container
        
node_list = LinkedList()
node_list2 = LinkedList()

node_list.append_node(8)
node_list.append_node(5)
node_list.append_node(6)
node_list.append_node(5)
node_list.append_node(7)
node_list.append_node(5)

# node_list2.append_node(31)
# node_list2.append_node(58)
# node_list2.append_node(0)
# node_list2.append_node(2)
# node_list2.append_node(13)

node_list.display()
node_list.sort()
node_list.display()