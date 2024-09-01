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

    def contains(self, value):
        if self.root == None:
            return False
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
    
    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node        

    






my_BST = BinarySearchTree()

# my_BST.insert(47)
# my_BST.insert (21)
# my_BST.insert (76)
# my_BST.insert(18)
# my_BST.insert(27)
# my_BST.insert(52)
# my_BST.insert(82)

my_BST.r_insert(2)
my_BST.r_insert(1)
my_BST.r_insert(3)


#print(my_BST.contains(82))
print(my_BST.r_contains(3))
# print(my_BST.contains(1099))
# print(my_BST.contains(1))
# print(my_BST.contains(17))


        
