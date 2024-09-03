class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree: 
  def __init__(self):
    self.root = None

  def r_insert(self, value):
    if self.root is None:
      self.root = Node(value)
      return True
    self.__r_insert(self.root, value)

  def __r_insert(self, current_node, value):
    if current_node is None:
      return Node(value)
    if value < current_node.value:
      current_node.left = self.__r_insert(current_node.left, value)
    elif value > current_node.value:
      current_node.right = self.__r_insert(current_node.right, value)
    return current_node    
  
  def invert(self):
    self.__r_invert_tree(self.root)

  def __r_invert_tree(self, current_node):
    if current_node is  None: 
      return None
    temp = current_node.left
    current_node.left = self.__r_invert_tree(current_node.right)
    current_node.right = self.__r_invert_tree(temp)
    return current_node
    



test_bst =BinarySearchTree()
test_bst.r_insert(30)
test_bst.r_insert(20)
test_bst.r_insert(40)

print("root = ", test_bst.root.value)
print("root.left = ", test_bst.root.left.value)
print("root.right = ", test_bst.root.right.value)

test_bst.invert()
print('\nAfter Inversion\n')

print("root = ", test_bst.root.value)
print("root.left = ", test_bst.root.left.value)
print("root.right = ", test_bst.root.right.value)

        
