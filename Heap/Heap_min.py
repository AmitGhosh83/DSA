class MinHeap:
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
        while current > 0 and self.heap[current] < self.heap[self._parent(current)]:
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
        min_index = index

        while True: 
            left_child_index = self._left_child(index)
            right_child_index = self._right_child(index)

            if(left_child_index < len(self.heap) and
                self.heap[left_child_index] > self.heap[min_index]):
                min_index = left_child_index
            if (right_child_index < len(self.heap) and
                self.heap[right_child_index] > self.heap[min_index]):
                min_index = right_child_index
            if min_index!= index:
                self._swap(index, min_index)    
                index = min_index   
            else: 
                return     


myheap = MinHeap()
myheap.insert(12)
myheap.insert(10)
myheap.insert(8)
myheap.insert(6) 
print (myheap.heap) #[6, 8, 10, 12]

# myheap.insert(12)
# myheap.insert(10)
# myheap.insert(8)
# myheap.insert(6)
# myheap.insert(4)
# myheap.insert(2)

# print(myheap.heap)  # [2, 6, 4, 12, 8, 10]

# removed = myheap.remove()
# print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 2, Heap: [4, 6, 10, 12, 8]

# removed = myheap.remove()
# print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 4, Heap: [6, 8, 10, 12]

# removed = myheap.remove()
# print(f'Removed: {removed}, Heap: {myheap.heap}')  # Removed: 6, Heap: [8, 12, 10]