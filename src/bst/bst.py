class Node:
    """
    This class defines a node.

    Attributes:
            left (Node): Left child.
            right (Node): Right child.
    """

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BST:
    """
    This is a class for a Binary Search Tree.

    Contains methods to insert and search.

    Attributes:
            root (Node): The initial root node.
    """

    def __init__(self):
        """
        The constructor for the BST class.
        """
        self.root = None

    def insert(self, key, current=None):
        """
        Function to insert a value to the tree.

        Parameters:
                key (int): The value to be inserted.
                current (Node): The current node where we insert the value (Used during recursion).
        """
        if self.root is None:
            self.root = Node(key)
            # print("Node Added to root")
        else:
            if current is None:
                current = self.root
            if key < current.val:
                if current.left is None:
                    current.left = Node(key)
                    # print("Node Added Left")
                else:
                    self.insert(key, current.left)
            elif key > current.val:
                if current.right is None:
                    current.right = Node(key)
                    # print("Node Added Right")
                else:
                    self.insert(key, current.right)
            else:
                # print("Value already present")
                pass

    def search(self, key, current=None):
        """
        Function to search for a value in the BST.

        Parameters:
                key (int): The value to be searched for.
                current (Node): The current node where we search for the value (Used in recursion).

        Returns:
                True if the value is found.
                False if the value is not found.
        """
        if self.root is None:
            # print("Nothing GO away")
            return False
        else:
            if current is None:
                current = self.root
            if key == current.val:
                # print("Found")
                return True
            elif key < current.val and current.left is not None:
                # print("Going Left")
                return self.search(key, current.left)
            elif key > current.val and current.right is not None:
                # print("Hard Right")
                return self.search(key, current.right)
            else:
                # print("Not Found")
                return False

    def delete(self, key, current):
        """
        Function to delete a value in the BST.

        Parameters:
                key (int): The value to be deleted.
                current (Node): The current node from where we search and delete the value.

        Returns:
                True if the value is deleted.
                False if the value is not deleted.
        """
        # current = current if current is not None else self.root

        if current is None:
            return current

        if key<current.val:
            current.left = self.delete(key, current.left)
        elif key>current.val:
            current.right = self.delete(key, current.right)
        else:
            if current.left is None:
                temp = current.right
                current = None
                return temp
            elif current.right is None:
                temp = current.left
                current = None
                return temp

            temp = self.get_inorder_successor(current.right)

            current.val = temp.val
            current.right = self.delete(temp.val, current.right)
        return current

    def inorder(self, current):
        """
        Prints the BST using inorder traversal.

        Parameters:
            current (Node): The root node from which to print the tree (optional).
        """

        if current:
            self.inorder(current.left)
            print(str(current.val) + " ", end="")
            self.inorder(current.right)

    def get_inorder_successor(self, current):
        """
        Returns the inorder successor of the given node.

        Pass the current.right value for the current parameter

        Parameters:
            current(Node): The node who's successor needs to be found.
        """

        while current.left is not None:
            current = current.left
        return current


if __name__ == '__main__':
    TREE = BST()

    while True:
        print("1. Insert a node.")
        print("2. Search for a node")
        print("3. Print Tree (inorder)")
        print("4. Delete a node.")
        print("5. Exit")
        u_input = int(input())
        if u_input == 1:
            print("Enter a value to insert.")
            val = int(input())
            TREE.insert(val)
        elif u_input == 2:
            print("Enter a valueto search.")
            val = int(input())
            TREE.search(val)
        elif u_input == 3:
            TREE.inorder(TREE.root)
        elif u_input == 4:
            print("Enter a value to delete.")
            val = int(input())
            TREE.delete(val, TREE.root)
        else:
            exit()
