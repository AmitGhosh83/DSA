class Stack:
    def __init__(self):
        self.stack_list= []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1): # what for 0
            print(self.stack_list[i])

    def is_empty(self):
        if len(self.stack_list)==0:
            return True
    def size(self):
        return len(self.stack_list)
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
        
    def push(self, value):
        return self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            temp = self.stack_list.pop()
            return temp    


mystack_list = Stack()
mystack_list.push(7)
mystack_list.push(3)
mystack_list.push(2)
print("\nBefore pop:")
mystack_list.print_stack()

mystack_list.pop()
print("\nAfter pop:")
mystack_list.print_stack()



    
    