class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    #Traverse the Linked List
    def print_list(self):
        temp = self.head  
        while temp is not None:
            print(temp.value)
            temp = temp.next

    #Append to the Linked List
    def append(self, value):
        new_node = Node(value)
        ## while list is empty
        if self.length==0:
            self.head = new_node
            self.tail = new_node
        ## while the list is not empty
        else:
            self.tail.next = new_node # point current tail to new node
            self.tail = new_node  # move tail to now newly added node
        self.length += 1 # increase length by 1
        return True
    
    # Pop from the LinkedList
    def pop(self):
        # if linkedlist if empty
        if self.length == 0:
            return None
        temp = pre = self.head
        #pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    #Add at the start of the Linked List
    def prepend(self,value):
        new_node= Node(value)
        if self.length==0:
            self.head = new_node
            self.tail = new_node
            
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    #Remove at the start of the Linked List
    def pop_first(self):
        if self.length == 0:
            return None

        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -=1
        if self.length==0:
            self.tail = None
        return temp    

    # Get an node from the linked list
    def get(self, index):
        if index < 0 or index >= self.length: 
            return None
        
        temp = self.head
        for i in range(index):
            temp = temp.next
        return temp
    
    # Set an node from the linked list
    def set_value(self, index, value):
        # if index < 0 or index >= self.length: 
        #     return None
        
        # temp = self.head
        # for i in range(index):
        #     temp = temp.next
        #     temp.value=value
        # return temp.value
        ## Refactoring Get method to implement DRY
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return temp.value
        return False    

    #Insert a node at a given index
    def insert(self, index, value):
        if index < 0 or index > self.length: 
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node= Node(value)
        temp= self.head
        for i in range(index-1):
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    # Delete a node at given index
    def delete (self, index):
        if index < 0 or index > self.length:
            return None 
        ## unlike insert, in remove method we will return a node
        ## if successful. So None means absense of value 
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        pre = temp = self.head
        for i in range(index):
            pre = temp
            temp = temp.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    # Reserve the Linked List
    def reserve(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
        after = temp.next
        before = None

        for i in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        return True;    
    


my_linked_list= LinkedList(1)
my_linked_list.append(9)
my_linked_list.append(3)
my_linked_list.append(17)

my_linked_list.print_list()

print("head -->", my_linked_list.head.value)
print("tail -->", my_linked_list.tail.value)
#my_linked_list.insert(0, 8)
#my_linked_list.delete(-1)
my_linked_list.reserve()
# print("Get method-->", my_linked_list.get(1))
# print("Set method-->", my_linked_list.set_value(1,9))

my_linked_list.print_list()

# print("1st value popped: ", my_linked_list.pop().value)
# print("2nd value popped: ",my_linked_list.pop().value)



# my_linked_list.print_list()      



