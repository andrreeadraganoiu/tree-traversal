import unittest
from tree import Tree


class TestTree(unittest.TestCase):

    def test_find_tree(self):
        t = Tree()
        for i in range(2):
            t.add(i)
        self.assertEqual(t.find(1).data, 1)

