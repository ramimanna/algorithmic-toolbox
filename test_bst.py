import unittest

class TestBstMethods(unittest.TestCase):
    valid_0 = tree = Node( 10, Node(8,None,None), Node(12, Node(11, Node(10,None,None),None), Node(13,None,None)))

    def test_check_bst(self):
        self.assertTrue(, 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()