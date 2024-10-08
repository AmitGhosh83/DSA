class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index): 
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        return True
    
    
    
    def insert(self, value):
        self.heap.append(value)
        # pointer to the location of the list
        # where the new value is inserted
        current = len(self.heap)-1

        # 1. Stop for current to go out of bound as it
            # traverses from child to its subsequent parent every swap
        # 2. Check that the current index value is greater than its 
            # corresponding parent, if not stop swapping. 
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0: 
            return None
        if len(self.heap) == 1:
        # returning and deleting the only heap value 
            return self.heap.pop()
        
        max_value = self.heap[0]
        # deleting the last value in the heap and placing at the start of the heap
        self.heap[0] = self.heap.pop()
        self.sink_down(0)
        return max_value
    
    def sink_down(self, index): 
        max_index = index

        while True: 
            left_child_index = self._left_child(index)
            right_child_index = self._right_child(index)

            if(left_child_index < len(self.heap) and
                self.heap[left_child_index] > self.heap[max_index]):
                max_index = left_child_index
            if (right_child_index < len(self.heap) and
                self.heap[right_child_index] > self.heap[max_index]):
                max_index = right_child_index
            if max_index!= index:
                self._swap(index, max_index)    
                index = max_index   
            else: 
                return     


myheap = MaxHeap()
# myheap.insert(99)       
# myheap.insert(72)
# myheap.insert(61)
# myheap.insert(58) 
# print (myheap.heap)

# myheap.insert(100)
# print (myheap.heap)

# myheap.insert(75)
# print(myheap.heap)

myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)
print(myheap.heap)

myheap.remove()
print(myheap.heap)

myheap.remove()
print(myheap.heap)