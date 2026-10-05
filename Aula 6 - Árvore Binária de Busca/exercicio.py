class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

# Construindo a árvore
values = [10, 5, 2, 7, 15, 12, 20]
root = None
for v in values:
    root = insert(root, v)

print("Pré-ordem:")
preorder(root)
print("\nEm ordem:")
inorder(root)
print("\nPós-ordem:")
postorder(root)
