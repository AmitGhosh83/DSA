class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 

    def print_list(self):
        if self.head is None:
            return None
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next


    ## Append to the doubleLinkedList(At End)
    def append(self, value):
        new_node = Node(value)
        if self.head  is None:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1 
        return True         

    # Using Linked LIst logic, Time Complexity O(n)
    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     pre = temp = self.head
    #     while(temp.next):
    #         pre = temp
    #         temp = temp.next
    #     self.tail = pre
    #     self.tail.next = None
    #     temp.prev = None
    #     self.length -= 1
    #     if(self.length == 0):
    #         self.tail = None
    #     return temp              

    # def pop(self):
    #     if self.length == 0:
    #         return None
    #     temp = self.tail
    #     self.tail = self.tail.prev
    #     self.tail.next = None
    #     temp.prev = None
    #     self.length -=1
    #     if(self.length == 0): 
    #         self.head = None
    #         self.tail = None
    #     return temp
    
    # Time comlexity O(1), using prev pointer
    def pop(self):
        if(self.length ==0):
            return None
        temp = self.tail
        if(self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
            self.tail.next = None
        self.length -= 1
        return temp    
    
    def prepend(self, value):
        new_node = Node(value)
        if (self.length == 0 ):
            self.head = new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # def pop_first(self):
    #     if(self.length == 0):
    #         return None
    #     temp = self.head
    #     self.head = self.head.next
    #     self.head.prev = None
    #     temp.next = None
    #     self.length -= 1
    #     if(self.length == 0):
    #         self.tail = None
    #     return temp;    
    def pop_first(self):
        if(self.length ==0):
            return None
        temp = self.head
        if(self.length == 1):
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp       

my_doubly_linked_list = DoublyLinkedList(5)   
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(7)
my_doubly_linked_list.print_list()  
#my_doubly_linked_list.pop()  
#my_doubly_linked_list.prepend(9)
my_doubly_linked_list.pop_first()

my_doubly_linked_list.print_list()  