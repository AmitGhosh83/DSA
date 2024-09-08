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
    
  def r_delete(self, value):
    self.__r_delete(self.root, value)
  
  def __r_delete(self, current_node, value):
    if current_node is None:
      return None
    if value < current_node.value:
      current_node.left = self.__r_delete(current_node.left, value)
    elif value > current_node.value:
      current_node.right = self.__r_delete(current_node.right, value)
    else: 
      if current_node.left is None and current_node.right is None:
        return None
      elif current_node.left is None:
        current_node = current_node.right
      elif current_node.right is None:
        current_node = current_node.left
      else:
        right_subtree_min_value = self.min(current_node.right)
        current_node.value = right_subtree_min_value
        current_node.right = self.__delete(current_node.right, right_subtree_min_value)


    return current_node  
  
  def min_value(self, current_node):
    while current_node.left is not None:
      current_node = current_node.left
      return current_node.value
     



test_bst =BinarySearchTree()
test_bst.r_insert(30)
test_bst.r_insert(20)
test_bst.r_insert(40)
test_bst.r_insert(15)

print("root = ", test_bst.root.value)
print("root.left = ", test_bst.root.left.value)
print("root.left.left = ", test_bst.root.left.left.value)
print("root.right = ", test_bst.root.right.value)


# test_bst.invert()
# print('\nAfter Inversion\n')

# print("root = ", test_bst.root.value)
# print("root.left = ", test_bst.root.left.value)
# print("root.right = ", test_bst.root.right.value)

test_bst.r_delete(15)
print('\nAfter Deletion\n')

print("root = ", test_bst.root.value)
print("root.left = ", test_bst.root.left.value)
print("root.left.left = ", test_bst.root.left.left)
print("root.right = ", test_bst.root.right.value)
        
