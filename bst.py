"""
Example Tree:
Node( 10, Node(8,None,None), Node(12, Node(11, Node(10,None,None),None), Node(13,None,None)))
"""

#OOP Representation:
class Node:
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
    def inorder_traverse(self):
        """
        Traverses a BST in order, producing a sorted list

        @param root: Node which represents root of a tree
        @return list of values from the bst, sorted
        """
        results = []
        if self.left: results.extend(self.left.inorder_traverse())
        results.append(self.value)
        if self.right: results.extend(self.right.inorder_traverse())
        return results
    def check_bst(self):
      """
      Checks if a tree is a binary search tree

      @param root: Node which represents root of a tree
      @return True iff tree is a binary search tree 
      """
      if not self.left and not self.right: return True
      return (self.right and self.value <= self.right.value) and (self.left and self.left.value <= self.value) and self.left.check_bst() and self.right.check_bst()
    def find(self, x):
      """
      Checks if value x is in a binary search tree

      @param root: Node which represents root of a tree
      @param x: int value to be searched for in tree
      @return True iff x is a value in the tree
      """
      if not self.left and not self.right: return False
      return x == self.value or (self.left and self.left.find(x)) or (self.right and self.right.find(x))

    def insert(self,x):
      """
      Mutates binary search tree by inserting x at a valid position

      @param root: Node which represents root of a tree
      @param x: int value to be inserted into the tree
      @return True iff opperation successful
      """
      node = self
      # Follow path to valid leaf to perform insert at
      while node.left or node.right:
        if node.left and node.value > x: node = node.left
        elif node.right: node = node.right
      #Now, node is a leaf
      if x <= node.value: node.left = Node(x,None,None)
      else: node.right = Node(x,None,None)
      return True

    def height(self):
      """
      Recursively calculates the height of a bst

      @param root: Node which represents root of a tree
      @return int height of the binary search tree
      """
      return max([h.height() for h in [self.left,self.right] if h is not None]+[0]) + 1

    def draw(self):
      """
      Prints a visualization of a binary tree

      @param root: Node which represents root of a tree

      """
      print ("-"*14 + "BST" + "-"*14)
      h = self.height()
      layers = {0:[self]}
      layers_vals = {0:[self.value]}
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

      def center(width, items):
        assert width >= len(items)
        line = [" "]*width
        spacing = [" "]*int((width-len(items))/2)
        return spacing + items + spacing

      for i in layers_vals:
        layer = list(map(str,layers_vals[i]))
        layer = ["X" if not item else item for item in layer]
        print(center(2**h,layer))
      print("-"*31)