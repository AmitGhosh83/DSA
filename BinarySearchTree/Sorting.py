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

 ## By reference 
  def insertion_sort(self):
    if self.length < 2:
      return
    # Distribute the list in sorted and unsorted portion
    sorted_list_head = self.head
    unsorted_list_head = self.head.next
    sorted_list_head.next = None
    
    while unsorted_list_head is not None:
      current = unsorted_list_head
      unsorted_list_head = unsorted_list_head.next

      if current.value < sorted_list_head.value:
        # ensure current is new sorted_list head
        current.next = sorted_list_head # notice current.next is now pointing to the old minimum
        sorted_list_head = current
      else:
        # initialize a pointer to find where to insert the current value in sorted part of the list
        search_pointer = sorted_list_head
        while search_pointer.next is not None and current.value > search_pointer.next.value: # current value has to me more than the pointers next value as the next step takes to the next place
          search_pointer = search_pointer.next
        # Once you find  that make current.next to point to pointer's next
        current.next = search_pointer.next
        # ensure pointer.next is the new current, not search pointer
        search_pointer.next = current  

    
    self.head = sorted_list_head
    temp = self.head
    while temp.next is not None:
      temp = temp.next
    self.tail = temp       







mylist = LinkedList(4)
mylist.append(2)
mylist.append(6)
mylist.append(5)
mylist.append(1)
mylist.append(3)

print("Linked List Before Sort:")
mylist.print_list()

mylist.insertion_sort()

print("\nSorted Linked List:")
mylist.print_list()