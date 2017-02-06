"""
Example Tree:
Bst(10, Bst(8), Bst(12, Bst(11, Bst(10)), Bst(13)))
"""

class Bst:
    def __init__(self,value,left = None,right = None):
        self.value = value
        self.left = left
        self.right = right
    def inorder_traverse(self):
        """
        Traverses a BST in order, producing a sorted list

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
      
      @return True iff tree is a binary search tree 
      """
      
      left_valid = not self.left or self.left and self.left.value <= self.value and self.left.check_bst()
      right_valid = not self.right or self.right and self.right.value >= self.value and self.right.check_bst()
      
      return left_valid and right_valid
    def find(self, x):
      """
      Checks if value x is in a binary search tree

      @param x: int value to be searched for in tree
      @return True iff x is a value in the tree
      """
      if x == self.value or (self.left and self.left.find(x)) or (self.right and self.right.find(x)):return True
      else: return False

    def insert(self,x):
      """
      Mutates binary search tree by inserting x at a valid position
      
      @param x: int value to be inserted into the tree
      @return True iff operation successful
      """
      node = self
      # Follow path to valid leaf to perform insert at
      while node.left and node.right:
        if node.value >= x: node = node.left
        else: node = node.right
      # Now, node is a leaf
      if x < node.value: node.left = Bst(x)
      else: node.right = Bst(x)

    def height(self):
      """
      Recursively calculates the height of a bst
      
      @return int height of the binary search tree
      """
      return max([h.height() for h in [self.left,self.right] if h is not None]+[0]) + 1

    def draw(self):
      """
      Prints a visualization of a binary tree

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

