# Classe que representa um nó da árvore.
# Cada nó guarda um valor, seus filhos da esquerda e da direita
# e também a altura do subárvore naquele ponto.
class Node:
    # Inicializa o nó com um valor e define os filhos como vazios.
    # A altura começa em 1, porque o próprio nó conta como nível 1.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


# Retorna a altura de um nó.
# Se o nó for vazio (None), a altura é 0.
def get_height(node):
    return node.height if node else 0


# Atualiza a altura do nó com base nas alturas dos filhos.
# A altura de um nó é 1 + a maior altura entre os filhos.
def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))


# Realiza uma rotação à direita em torno do nó y.
# Essa rotação é usada para balancear a árvore quando a subárvore da esquerda está mais alta.
def rotate_right(y):
    # x será o filho da esquerda de y.
    x = y.left
    # T2 é a subárvore direita de x.
    T2 = x.right

    # Faz a rotação: x passa a ser a nova raiz da parte rotacionada.
    x.right = y
    y.left = T2

    # Atualiza as alturas depois da rotação.
    update_height(y)
    update_height(x)

    # Retorna a nova raiz da rotação.
    return x


# Realiza uma rotação à esquerda em torno do nó x.
# Essa rotação é usada quando a subárvore da direita está mais alta.
def rotate_left(x):
    # y será o filho da direita de x.
    y = x.right
    # T2 é a subárvore esquerda de y.
    T2 = y.left

    # Faz a rotação: y passa a ser a nova raiz da parte rotacionada.
    y.left = x
    x.right = T2

    # Atualiza as alturas depois da rotação.
    update_height(x)
    update_height(y)

    # Retorna a nova raiz da rotação.
    return y


# Rotação esquerda-direita:
# primeiro rotaciona o filho da esquerda para a esquerda e depois rotaciona a raiz para a direita.
def rotate_left_right(node):
    node.left = rotate_left(node.left)
    return rotate_right(node)


# Rotação direita-esquerda:
# primeiro rotaciona o filho da direita para a direita e depois rotaciona a raiz para a esquerda.
def rotate_right_left(node):
    node.right = rotate_right(node.right)
    return rotate_left(node)


# Bloco de teste simples para demonstrar a rotação.
# Cria uma árvore desbalanceada: 30 -> 20 -> 10.
# Nesse caso, a subárvore da esquerda está mais alta e precisa ser balanceada.
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

# Função para percorrer a árvore em ordem (esquerda, raiz, direita).
# Isso permite visualizar a sequência dos valores antes e depois da rotação.
print("Antes da rotação à direita (in-ordem):")
def inorder(n):
    if n:
        inorder(n.left)
        print(n.value, end=" ")
        inorder(n.right)

# Exibe a árvore antes do balanceamento.
inorder(root)

# Aplica a rotação à direita para balancear a árvore.
root = rotate_right(root)

# Exibe a árvore depois da rotação.
print("\nDepois da rotação à direita (in-ordem):")
inorder(root)
