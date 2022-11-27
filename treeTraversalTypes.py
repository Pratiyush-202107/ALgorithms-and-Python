# Class that accommodates all the Tree
# traversal types (Inorder, Preorder, Postorder)

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item

# Function for inorder traversal
def inorder(root):
    if root:
        # Traverse left
        inorder(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        inorder(root.right)

# Function for preorder traversal
def preorder(root):
    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        preorder(root.left)
        # Traverse right
        preorder(root.right)

# Function for postorder traversal
def postorder(root):
    if root:
        # Traverse left
        postorder(root.left)
        # Traverse right
        postorder(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')

root = Node(1)
root.left = Node(5)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)

print("Inorder traversal:- ")
inorder(root)

print("\nPreorder traversal:- ")
preorder(root)

print("\nPostorder traversal:- ")
postorder(root)