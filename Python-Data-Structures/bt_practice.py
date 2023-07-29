import collections

class Node:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

def preorder(Node):
    if Node == None:
        return 
    
    print(Node.value, end=" ")
    preorder(Node.left)
    preorder(Node.right)

def inorder(Node):
    if Node == None:
        return
    
    inorder(Node.left)
    print(Node.value, end=" ")
    inorder(Node.right)

def postorder(Node):
    if Node == None:
        return
    
    postorder(Node.left)
    postorder(Node.right)
    print(Node.value, end=" ")

# def bfs(Node):
#     q = Queue()
#     q.put(Node)

#     while (not q.empty()):
#         node = q.get()
#         print(node.value, end=" ")
        
#         if node.left != None:
#             q.put(node.left)
        
#         if node.right != None:
#             q.put(node.right)
          
def iterPreorder(Node):
    #Time complexity: O(N)
    #Space complexity: O(N) at worst. More appropriately O(H), H = height of tree
    st = collections.deque()
    st.append(Node)

    while (len(st) > 0):
        curr = st.pop()
        print(curr.value, end=" ")
        if curr.right != None:    
          st.append(curr.right)
        if curr.left != None:
          st.append(curr.left)


           

root = Node(1)
root.left = Node(2)
root.right = Node(7)
root.left.left = Node(3)
root.left.right = Node(4)
root.left.right.left = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
root.right.right.left = Node(9)
root.right.right.right = Node(10)

preorder(root)
print()
# inorder(root)
# print()
# postorder(root)
# print()
# bfs(root)
iterPreorder(root)
