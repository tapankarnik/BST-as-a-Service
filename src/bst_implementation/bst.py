class Node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
class BST:
	def __init__(self, key):
		self.root = Node(key)

	def insert(self,key):
		node = Node(key)
		if self.root == None:
			self.root = node
			print("Node Added")
		else:
			if self.root.val > node.val:
				if self.root.left == None:    
					self.root.left = node
					print("Node Added Left")
				else:
					insert(self.root.left,node)
			else:
				if self.root.right == None:
					self.root.right = node
					print("Node Added Right")
				else:
					insert(self.root.right,node)

	#Search
	def search(self,key):
		if self.root == None:
			print("Nothing GO away")
			return False
		else:
			if (key == self.root.val):
				print("Found")
				return True
			elif (key<self.root.val):
				print("Going Left") 
				return self.search(key)
			else:
				print("Hard Right")
				return self.search(key)

if __name__ == '__main__':
	val = 34
	tree = BST(val)
	tree.insert(40)
	tree.insert(20)
	if tree.search(20) == True:
		print("yens")
	else:
		print("nien")
