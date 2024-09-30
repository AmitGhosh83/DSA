class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length =1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length +=1

    def print(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next           

    def selection_sort(self):
        if self.head is not None and self.length < 2:
            return
        temp = self.head
        while temp.next is not None:
            smallest = temp
            after = temp.next 
            while after is not None:
                if smallest.value > after.value:
                    smallest = after
                after = after.next  
            # Break out of inner loop, before you compare      
            if temp!= smallest:
                temp.value, smallest.value = smallest.value, temp.value
            temp = temp.next                     


myList = LinkedList(4)
myList.append(2)
myList.append(6)
myList.append(5)
myList.append(1)
myList.append(3)

myList.print()
print('\n')

myList.selection_sort()
myList.print()