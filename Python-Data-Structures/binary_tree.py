#Binary traa implementation in Python

#For defining nodes with 3 data fields
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

#For defining the tree
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def preorder_traversal(self, node):
        #Base condition
        if node == None:
            return
        
        print(node.data, end=" ") #root
        self.preorder_traversal(node.left) #left node
        self.preorder_traversal(node.right) #right node
    
    def inorder_traversal(self, node):
        #Base condition
        if node == None:
            return 
        
        self.inorder_traversal(node.left) #left node
        print(node.data, end=" ") #root
        self.inorder_traversal(node.right) #right node

    def postorder_traversal(self, node):
        #Base condition
        if node == None:
            return
        
        self.postorder_traversal(node.left)
        self.postorder_traversal(node.right)
        print(node.data, end=" ")

tree = BinaryTree(10)
tree.root.left = Node(20)
tree.root.right = Node(30)
tree.root.left.left = Node(40)
tree.root.left.right = Node(50)
tree.root.right.left = Node(60)
tree.root.right.right = Node(70)

tree.preorder_traversal(tree.root)
print()
tree.inorder_traversal(tree.root)
print()
tree.postorder_traversal(tree.root)
    
