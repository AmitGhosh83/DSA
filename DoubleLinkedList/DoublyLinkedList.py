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
            self.tail.next = new_node # connect tail.next to the new node
            new_node.prev = self.tail # connect next.prev to tail
            self.tail = new_node # make new node the new tail
            self.length += 1 
        return True         

    # Using Linked List logic instead of Double Linked List, Time Complexity O(n)
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

    ##
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
    
    def get(self,index):
        if( index < 0 or index >= self.length):
            return None
        if ( index < self.length/2):
            temp = self.head
            for i in range(index):
                temp = temp.next
        else: 
            temp = self.tail
            for i in range(self.length -1, index, -1):
                temp = temp.prev
        return temp           

    def set_value(self, index, value):
        if( index < 0 or index >=self.length):
            return None
        
        # if ( index < self.length/2):
        #     temp = self.head
        #     for i in range(index):
        #         temp= temp.next
        # else: 
        #     temp = self.tail
        #     for i in range(self.length -1, index, -1):
        #         temp = temp.prev
        temp = self.get(index)
        temp.value = value
        return True

    def insert(self, index, value):
        if( index < 0 or index > self.length):
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        else:
            before = self.get(index-1)
            new_node = Node(value)
            after = before.next
            before.next = new_node
            new_node.prev = before
            new_node.next = after
            after.prev = new_node
            self.length += 1
        return True        

    def remove(self, index):
        if( index < 0 or index > self.length):
            return None
        if index == 0:
            return self.pop_first()
        # 0 based index, so self.length -1 is the last element
        if index == self.length - 1: 
            return self.pop()
        else:
            temp = self.get(index)
            after = temp.next
            before = temp.prev
            before.next = after
            after.prev = before
            temp.next = None
            temp.prev = None
            self.length -= 1
        return temp 

my_doubly_linked_list = DoublyLinkedList(1)   
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.print_list()  
#my_doubly_linked_list.pop()  
#my_doubly_linked_list.prepend(9)
#my_doubly_linked_list.pop_first()
#my_doubly_linked_list.get(3)
my_doubly_linked_list.set_value(3,9)
#my_doubly_linked_list.insert(4,6)
#my_doubly_linked_list.remove(5)
print("\nAfter update:")
my_doubly_linked_list.print_list()  