#OOP Representation:
class Node:
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right

"""
Some Example Trees:

Valid:
Node( 10, Node(8,None,None), Node(12, Node(11, Node(10,None,None),None), Node(13,None,None)))

Invalid:
Node(7, Node(5,None,None), Node(14, Node(14,None,None), Node(15,None,None)))
"""

root = Node( 10, Node(8,None,None), Node(12, Node(11, Node(10,None,None),None), Node(13,None,None)))


def inorder_traverse(root):
    """
    Traverses a BST in order, producing a sorted list

    @param root: Node which represents root of a tree
    @return list of values from the bst, sorted
    """
    results = []
    if root.left: results.extend(inorder_traverse(root.left))
    results.append(root.value)
    if root.right: results.extend(inorder_traverse(root.right))
    return results
def check_bst(root):
  """
  Checks if a tree is a binary search tree

  @param root: Node which represents root of a tree
  @return True iff tree is a binary search tree 
  """
  if not root.left and not root.right: return True
  return (root.right and root.value <= root.right.value) and (root.left and root.left.value <= root.value) and check_bst(root.left) and check_bst(root.right)

def find(root, x):
  """
  Checks if value x is in a binary search tree

  @param root: Node which represents root of a tree
  @param x: int value to be searched for in tree
  @return True iff x is a value in the tree at root
  """
  if not root: return False
  return x == root.value or find(root.left, x) or find(root.right,x)

def insert(root,x):
  """
  Mutates binary search tree by inserting x at a valid position

  @param root: Node which represents root of a tree
  @param x: int value to be inserted into the tree
  @return True iff opperation successful
  """
  node = root
  # Follow path to valid leaf to perform insert at
  while node.left or node.right:
    if node.left and node.value > x: node = node.left
    elif node.right: node = node.right
  #Now, node is a leaf
  if x <= node.value: node.left = Node(x,None,None)
  else: node.right = Node(x,None,None)
  return True

insert(root,15)
# print(root.right.right.right.value)

def height(root):
  """
  Recursively calculates the height of a bst

  @param root: Node which represents root of a tree
  @return int height of the binary search tree
  """
  if not root: return 0
  return max(height(root.left),height(root.right)) + 1

# print(height(root))

def center(width, items):
  assert width >= len(items)
  line = [" "]*width
  spacing = [" "]*int((width-len(items))/2)
  return spacing + items + spacing

print(center(8,["3","4"]))

def draw(root):
  """
  Prints a visualization of a binary tree

  @param root: Node which represents root of a tree

  """
  print ("---------------BST---------------")
  h = height(root)
  layers = {0:[root]}
  layers_vals = {0:[root.value]}
  for i in range(1,h):
    layers[i] = []
    layers_vals[i] = []
    for parent in layers[i-1]:
      if parent and parent.left:
        layers[i].append(parent.left)
        layers_vals[i].append(parent.left.value)
      else:
        layers[i].append("")
        layers_vals[i].append("")

      if parent and parent.right:
        layers[i].append(parent.right)
        layers_vals[i].append(parent.right.value)
      else:
        layers[i].append("")
        layers_vals[i].append("")

  for i in layers_vals:
    layer = list(map(str,layers_vals[i]))
    layer = ["X" if not item else item for item in layer]
    print(center(2**h,layer))
  print("---------------------------------")

draw(root)

