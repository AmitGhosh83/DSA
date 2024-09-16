class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self): 
        self.root = None   

    def insert(self, value): 
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value)
        if (value < current_node.value):
            current_node.left = self.__r_insert(current_node.left, value)
        if (value > current_node.value):
            current_node.right = self.__r_insert(current_node.right, value)  
        return current_node
    
    def delete(self,value):
        self.__r_delete(self.root, value)

    def __r_delete(self, current_node, value):
        if current_node is None:
            return None
        if (value < current_node.value):
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value : 
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None  
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                ## bug here with current_node.right
                right_min_subtree_value = self.min_subtree_value(current_node.right)
                current_node.value = right_min_subtree_value
                current_node.right = self.__r_delete(current_node.right, right_min_subtree_value)
        return current_node    

    def min_subtree_value(self, current_node):
        while current_node is not None:
            current_node = current_node.left
        return current_node.value    
    
    def contains(self, value):
        return self.__r_contains(self.root, value)
    
    def __r_contains(self, current_node, value):
        if self.root is None:
            return None
        if current_node.value == value:
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        elif value > current_node.value:
            return self.__r_contains(current_node.right, value)


      
sampleTree = BinarySearchTree()
sampleTree.insert(2)
sampleTree.insert(1)
sampleTree.insert(3)
sampleTree.insert(4)
sampleTree.insert(5)

print(sampleTree.contains(1))
print(sampleTree.root.value)
print(sampleTree.root.left.value)
print(sampleTree.root.right.value)
print(sampleTree.root.right.left)
print(sampleTree.root.right.right.value)
print(sampleTree.root.right.right.right.value)

sampleTree.delete(5)
print('\nAfter Delete:\n')
print(sampleTree.root.value)
print(sampleTree.root.left.value)
print(sampleTree.root.right.value)
print(sampleTree.root.left.left)
print(sampleTree.root.right.right.value)
print(sampleTree.root.right.right.right)



