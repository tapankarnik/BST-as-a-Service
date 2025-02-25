"""Test Case Class which implements all the tests required for BST."""
import io
import sys
import unittest
import bst

class TestBST(unittest.TestCase):
    """
    This class has all the unit tests for testing the BST.
    """

    def test_insert(self):
        """
        This test checks the insert method.
        """
        tree = bst.BST()
        tree.insert(5)
        tree.insert(3)
        tree.insert(4)
        tree.insert(1)
        tree.insert(7)
        tree.insert(6)
        tree.insert(12)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(tree.inorder(tree.root))
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual(output, "[1, 3, 4, 5, 6, 7, 12]\n")

    def test_search(self):
        """This test checks the search method."""
        tree = bst.BST()
        tree.insert(5)
        tree.insert(3)
        tree.insert(4)
        tree.insert(1)
        tree.insert(7)
        tree.insert(6)
        tree.insert(12)
        self.assertTrue(tree.search(3))
        self.assertTrue(tree.search(7))
        self.assertTrue(tree.search(5))
        self.assertTrue(tree.search(12))
        self.assertFalse(tree.search(66))

    def test_get_inorder_successor(self):
        """This tests the get_inorder_successor method."""

        tree = bst.BST()
        tree.insert(5)
        tree.insert(3)
        tree.insert(4)
        tree.insert(1)
        tree.insert(7)
        tree.insert(6)
        tree.insert(12)
        self.assertEqual(tree.get_inorder_successor(tree.root.right).val, tree.root.right.left.val)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(tree.inorder(tree.root))
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual(output, "[1, 3, 4, 5, 6, 7, 12]\n")


    def test_delete_node(self):
        """This test covers the delete method which as the name suggests, deletes nodes."""

        tree = bst.BST()
        tree.insert(5)
        tree.insert(3)
        tree.insert(4)
        tree.insert(1)
        tree.insert(7)
        tree.insert(6)
        tree.insert(12)

        tree.root=tree.delete(5, tree.root)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(tree.inorder(tree.root))
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual(output, "[1, 3, 4, 6, 7, 12]\n")

        tree.root=tree.delete(7, tree.root)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(tree.inorder(tree.root))
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual(output, "[1, 3, 4, 6, 12]\n")

        tree.root=tree.delete(1, tree.root)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(tree.inorder(tree.root))
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual(output, "[3, 4, 6, 12]\n")

        tree.root=tree.delete(3, tree.root)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(tree.inorder(tree.root))
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual(output, "[4, 6, 12]\n")

        tree.root=tree.delete(66, tree.root)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(tree.inorder(tree.root))
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual(output, "[4, 6, 12]\n")

        tree.root=tree.delete(12, tree.root)
        tree.root=tree.delete(6, tree.root)
        tree.root=tree.delete(4, tree.root)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        print(tree.inorder(tree.root))
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual(output, "[]\n")

if __name__ == '__main__':
    unittest.main()
