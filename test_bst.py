import unittest
from bst import *

#Add tests for cases with duplicate number

class TestBstMethods(unittest.TestCase):
    """
    inorder_traverse(self) tests:

    Partition input as follows:

    * number of nodes: 1, > 1
    * tree has: only left children, only right children, both
    """
    def test_inorder_traverse_1node(self):
        tree = Bst(4)
        self.assertEqual(tree.inorder_traverse(),[4])

    def test_inorder_traverse_both(self):
        tree = Bst(10, Bst(8), Bst(12, Bst(11, Bst(10)), Bst(13)))
        self.assertEqual(tree.inorder_traverse(), [8,10,10,11,12,13])

    def test_inorder_traverse_left(self):
        tree = Bst(6,Bst(4,Bst(3,Bst(2))))
        self.assertEqual(tree.inorder_traverse(), [2,3,4,6])

    def test_inorder_traverse_right(self):
        tree = Bst(3,None, Bst(5,None, Bst(8)))
        self.assertEqual(tree.inorder_traverse(),[3,5,8])

    """
    check_bst(self) method tests:

    Partition input as follows:
    * number of nodes: 1, > 1
    * mistake: left child > parent, right child < parent
    * tree has: only left children, only right children, both

    Cover each part.
    """
    def test_check_bst_1node(self):
        good_tree = Bst(4)
        self.assertTrue(good_tree.check_bst())

    def test_check_bst_both(self):
        good_tree = Bst(10, Bst(8), Bst(12, Bst(11, Bst(10)), Bst(13)))
        self.assertTrue(good_tree.check_bst())

    def test_only_left(self):
        good_tree = Bst(6,Bst(4,Bst(3,Bst(2))))
        self.assertTrue(good_tree.check_bst())

    def test_only_right(self):
        good_tree = Bst(3,None, Bst(5,None, Bst(8)))
        self.assertTrue(good_tree.check_bst())

    def test_check_bst_left_greater(self):
        bad_tree = Bst(8, Bst(10),Bst(11))
        self.assertFalse(bad_tree.check_bst())

    def test_check_bst_right_smaller(self):
        bad_tree = Bst(12, Bst(4),Bst(15,Bst(13),Bst(10)))
        self.assertFalse(bad_tree.check_bst())
    """
    find(self,x) method tests:

    Partition input as follows:
    * number of nodes: 1, > 1
    * tree has: only left children, only right children, both
    * x is in tree: True, False

    Cover each part.
    """
    def test_find_1node(self):
        tree = Bst(4)
        self.assertTrue(tree.find(4))
        self.assertFalse(tree.find(6))

    def test_find_both(self):
        tree = Bst(10, Bst(8,Bst(7),Bst(9)), Bst(12, Bst(11, Bst(10)), Bst(13)))
        self.assertTrue(tree.find(13))#x on right
        self.assertTrue(tree.find(7)) #x on left
        self.assertFalse(tree.find(3))#x not in bst

    def test_find_left(self):
        tree = Bst(6,Bst(4,Bst(3,Bst(2))))
        self.assertTrue(tree.find(3))
        self.assertFalse(tree.find(8))

    def test_find_right(self):
        tree = Bst(3,None, Bst(5,None, Bst(8)))
        self.assertTrue(tree.find(8))
        self.assertFalse(tree.find(2))
    
    """
    insert(self,x) method tests:

    Partition input as follows:
    * number of nodes: 1, > 1
    * tree has: only left children, only right children, both
    * tree already had x: True, False

    Cover each part.
    """
    def test_insert_1node(self):
        tree = Bst(4)
        tree.insert(6)
        self.assertTrue(tree.find(6))
        self.assertTrue(tree.check_bst())

    def test_insert_both(self):
        tree = Bst(10, Bst(8,Bst(7),Bst(9)), Bst(12, Bst(11, Bst(10)), Bst(13)))
        tree.insert(16)
        tree.insert(7)
        self.assertTrue(tree.find(7) and tree.find(16))
        self.assertTrue(tree.check_bst())

    def test_insert_left(self):
        tree = Bst(6,Bst(4,Bst(3,Bst(2))))
        tree.insert(1)
        self.assertTrue(tree.find(1))
        self.assertTrue(tree.check_bst())

    def test_insert_right(self):
        tree = Bst(3,None, Bst(5,None, Bst(8)))
        tree.insert(2)
        tree.insert(4)
        self.assertTrue(tree.find(2) and tree.find(4))
        self.assertTrue(tree.check_bst())
    """
    height(self) method tests:

    Partition input as follows:
    * number of nodes: 1, > 1
    * tree has: only left children, only right children, both
    * tree height: 1, >1

    Cover each part.
    """
    def test_height_1node(self):
        tree = Bst(4)
        self.assertEqual(tree.height(), 1)

    def test_height_both(self):
        tree = Bst(10, Bst(8,Bst(7),Bst(9)), Bst(12, Bst(11, Bst(10)), Bst(13)))
        self.assertEqual(tree.height(), 4)

    def test_height_left(self):
        tree = Bst(6,Bst(4,Bst(3,Bst(2))))
        self.assertEqual(tree.height(), 4)

    def test_height_right(self):
        tree = Bst(3,None, Bst(5,None, Bst(8)))
        self.assertEqual(tree.height(), 3)
            
if __name__ == '__main__':
    unittest.main()