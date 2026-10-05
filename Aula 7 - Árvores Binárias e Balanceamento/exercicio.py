class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

def get_height(node):
    return node.height if node else 0

def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    # Rotação
    x.right = y
    y.left = T2

    # Atualiza alturas
    update_height(y)
    update_height(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    # Rotação
    y.left = x
    x.right = T2

    # Atualiza alturas
    update_height(x)
    update_height(y)

    return y

def rotate_left_right(node):
    node.left = rotate_left(node.left)
    return rotate_right(node)

def rotate_right_left(node):
    node.right = rotate_right(node.right)
    return rotate_left(node)

# Teste simples
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

print("Antes da rotação à direita (in-ordem):")
def inorder(n):
    if n:
        inorder(n.left)
        print(n.value, end=" ")
        inorder(n.right)

inorder(root)

root = rotate_right(root)

print("\nDepois da rotação à direita (in-ordem):")
inorder(root)
