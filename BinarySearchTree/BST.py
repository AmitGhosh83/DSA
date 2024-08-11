class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True ## Notice this statement, this is to break out if the tree is getting initialized
        temp = self.root

        while(True):
            if(new_node.value == temp):
                return False
            if(new_node.value < temp.value):
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains_1(self, value):
        if self.root is None:
            return False
        temp = self.root
        while(True):
            if value == temp.value:
                return True
            if (value< temp.value and temp.left is not None):
                temp = temp.left
                if(temp.left is None and temp.value != value):
                    return False
            elif (value > temp.value and temp.right is not None):
                temp = temp.right
                if(temp.right is None and temp.value!= value):
                    return False
                
        return False   

    def contains(self, value):
        temp = self.root
        while (temp is not None):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                temp.value = value
                return True
        return False                      





my_BST = BinarySearchTree()

my_BST.insert(40)
my_BST.insert (37)
my_BST.insert (86)
my_BST.insert(17)
my_BST.insert(21)
my_BST.insert(77)
my_BST.insert(92)

print(my_BST.contains(40))
print(my_BST.contains(1099))
print(my_BST.contains(1))
print(my_BST.contains(17))


        
