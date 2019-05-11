class Node:
	"""
	This class defines a node.

	Attributes:
		left (Node): Left child.
		right (Node): Right child.
	"""
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
class BST:
	"""
	This is a class for a Binary Search Tree 

	Contains methods to insert and search.

	Attributes:
		root (Node): The initial root node.
	"""
	def __init__(self):
		"""
		The constructor for the BST class.
		"""
		self.root = None

	def insert(self,key,current = None):
		"""
		Function to insert a value to the tree.

		Parameters:
			key (int): The value to be inserted.
			current (Node): The current node where we insert the value (Used during recursion).
		"""
		if self.root == None:
			self.root = Node(key)
			print("Node Added to root")
		else:
			if current == None:
				current = self.root
			if key < current.val:
				if current.left == None:    
					current.left = Node(key)
					print("Node Added Left")
				else:
					self.insert(key,current.left)
			elif key > current.val:
				if current.right == None:
					current.right = Node(key)
					print("Node Added Right")
				else:
					self.insert(key,current.right)
			else:
				print("Value already present")
				pass

	def search(self,key,current = None):
		"""
		Function to search for a value in the BST.

		Parameters:
			key (int): The value to be searched for.
			current (Node): The current node where we search for the value (Used in recursion).
		
		Returns:
			True if the value is found.
			False if the value is not found.
		"""
		if self.root == None:
			print("Nothing GO away")
			return False
		else:
			if current == None:
				current = self.root
			if (key == current.val):
				print("Found")
				return True
			elif (key < current.val and current.left is not None):
				print("Going Left") 
				return self.search(key, current.left)
			elif (key > current.val and current.right is not None):
				print("Hard Right")
				return self.search(key, current.right)
			else:
				print("Not Found")
				return False

if __name__ == '__main__':
	tree = BST()

	while True:
		print("1. Insert a node.")
		print("2. Search for a node")
		print("3. Exit")
		u_input = int(input())
		if u_input == 1:
			print("Enter a value")
			val = int(input())
			tree.insert(val)
		elif u_input == 2:
			print("Enter a value")
			val = int(input())
			tree.search(val)
		else:
			exit()