# Classe que representa um nó da árvore binária.
# Cada nó armazena um valor e possui referências para um filho à esquerda e um filho à direita.
class Node:
    # Inicializa um novo nó com o valor recebido.
    # No momento da criação, os filhos começam vazios (None).
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Insere um novo valor na árvore binária de busca.
# Valores menores que o nó atual são encaminhados para a esquerda.
# Valores maiores ou iguais são encaminhados para a direita.
def insert(root, value):
    # Se a posição estiver vazia, cria e retorna um novo nó.
    if root is None:
        return Node(value)

    # Se o valor for menor que o valor do nó atual,
    # a inserção continua recursivamente na subárvore esquerda.
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        # Caso contrário, a inserção continua recursivamente
        # na subárvore direita.
        root.right = insert(root.right, value)

    # Retorna o nó atual para manter a estrutura da árvore.
    return root


# Percorre a árvore no modo pré-ordem.
# A sequência visitada é: raiz, esquerda e direita.
def preorder(root):
    # Só executa a visita quando o nó existe.
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)


# Percorre a árvore no modo em ordem.
# A sequência visitada é: esquerda, raiz e direita.
# Em uma árvore binária de busca, esse percurso imprime os valores em ordem crescente.
def inorder(root):
    # Só executa a visita quando o nó existe.
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)


# Percorre a árvore no modo pós-ordem.
# A sequência visitada é: esquerda, direita e raiz.
def postorder(root):
    # Só executa a visita quando o nó existe.
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")


# Lista de valores que serão inseridos na árvore.
# A ordem desses valores define a estrutura final da árvore binária de busca.
values = [10, 5, 2, 7, 15, 12, 20]

# Inicialmente, a árvore está vazia.
root = None

# Insere cada valor da lista na árvore.
# A variável root recebe o resultado da inserção para manter a referência da raiz.
for v in values:
    root = insert(root, v)


# Exibe os valores usando o percurso pré-ordem.
print("Pré-ordem:")
preorder(root)

# Exibe os valores usando o percurso em ordem.
print("\nEm ordem:")
inorder(root)

# Exibe os valores usando o percurso pós-ordem.
print("\nPós-ordem:")
postorder(root)
