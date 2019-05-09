class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key
def insert(root,node):
    if root == None:
        root = node
    else:
        if root.val > node.val:
            if root.left == None:    
                root.left = node
            else:
                insert(root.left,node)
        else:
            if root.right == None:
                root.right = node
            else:
                insert(root.right,node)




