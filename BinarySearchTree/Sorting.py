class Node: 
  def __init__(self, value): 
    self.value = value
    self.next = None

class LinkedList: 
  def __init__(self,value):
    new_node = Node(value)
    self.head = new_node
    self.tail = new_node
    self.length = 1

  def append(self, value):
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length += 1

  def print_list(self):
    temp = self.head
    while(temp):
      print(temp.value)
      temp = temp.next   

  def selection_sort(self):
    if self.length < 2:
      return 
    temp = self.head
    while temp.next is not None: 
      smallest = temp
      after = temp.next
      while after is not None:
        if after.value < smallest.value:
          smallest = after
        after = after.next 
      if temp!= smallest:
          temp.value, smallest.value = smallest.value, temp.value
      temp = temp.next 

  def insertion_sort(self):
    if self.length < 2:
      return
    temp = self.head
    while temp.next is not None:
            




mylist = LinkedList(4)
mylist.append(2)
mylist.append(6)
mylist.append(5)
mylist.append(1)
mylist.append(3)

print("Linked List Before Sort:")
mylist.print_list()

mylist.selection_sort()

print("\nSorted Linked List:")
mylist.print_list()