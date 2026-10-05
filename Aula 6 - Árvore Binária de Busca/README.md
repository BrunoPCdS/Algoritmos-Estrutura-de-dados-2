# Aula 6 - Árvore Binária de Busca

Este exercício apresenta uma implementação simples de uma **árvore binária de
busca (Binary Search Tree ou BST)** usando Python. O objetivo é praticar uma
das principais estruturas de dados não lineares e observar como a ordem dos
elementos muda de acordo com a forma de percorrer a árvore.

## Sobre a matéria

Em **Algoritmos e Estruturas de Dados II**, estudamos formas de organizar
informações para que elas possam ser inseridas, consultadas e percorridas de
maneira eficiente.

Uma árvore é formada por **nós** conectados entre si. Cada nó pode possuir:

- um valor;
- um filho à esquerda;
- um filho à direita.

O primeiro nó da árvore é chamado de **raiz**. Um nó que não possui filhos é
chamado de **folha**.

## O que é uma árvore binária de busca?

Em uma árvore binária de busca, para cada nó:

- valores menores ficam na subárvore da esquerda;
- valores maiores ou iguais ficam na subárvore da direita.

Essa regra facilita a busca de valores, pois permite descartar parte da árvore
a cada comparação. Neste exercício, valores repetidos também são inseridos à
direita.

Para os valores usados no programa:

```python
[10, 5, 2, 7, 15, 12, 20]
```

a árvore construída é:

```text
        10
       /  \
      5    15
     / \   / \
    2   7 12 20
```

## Explicação do código

### Classe `Node`

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
```

A classe representa um nó. Cada nó começa com um valor e com os ponteiros
`left` e `right` vazios, que posteriormente podem apontar para outros nós.

### Função `insert`

```python
def insert(root, value):
```

Essa função insere um valor na posição correta:

1. Se a raiz atual for `None`, cria um novo nó.
2. Se o valor for menor que o valor da raiz, continua pela esquerda.
3. Caso contrário, continua pela direita.
4. Retorna a raiz da árvore para manter as ligações entre os nós.

A função utiliza **recursão**, ou seja, chama a si mesma até encontrar uma
posição vazia.

### Percursos da árvore

O programa implementa três formas clássicas de visitar os nós:

#### Pré-ordem (preorder)

Visita na ordem:

```text
raiz -> esquerda -> direita
```

É útil, por exemplo, para copiar ou serializar a estrutura da árvore.

#### Em ordem (inorder)

Visita na ordem:

```text
esquerda -> raiz -> direita
```

Em uma árvore binária de busca, esse percurso apresenta os valores em ordem
crescente.

#### Pós-ordem (postorder)

Visita na ordem:

```text
esquerda -> direita -> raiz
```

Esse percurso é útil quando precisamos processar os filhos antes do pai, como
na remoção de uma árvore ou no cálculo do tamanho de pastas.

## Resultado esperado

Ao executar o programa, a saída será:

```text
Pré-ordem:
10 5 2 7 15 12 20
Em ordem:
2 5 7 10 12 15 20
Pós-ordem:
2 7 5 12 20 15 10
```

Os valores aparecem na mesma linha porque as funções usam `print` com
`end=" "`. O espaço final é normal.

## Como executar

No terminal, entre na pasta da aula e execute:

```bash
python exercicio.py
```

Em alguns ambientes, pode ser necessário usar:

```bash
python3 exercicio.py
```

Não é necessário instalar nenhuma biblioteca externa; o exercício usa apenas
recursos nativos do Python.

## Complexidade

Se a árvore estiver equilibrada, a inserção e a busca costumam ter custo:

```text
O(log n)
```

No pior caso, quando os valores são inseridos em ordem crescente ou
decrescente e a árvore fica parecida com uma lista, o custo pode chegar a:

```text
O(n)
```

Os percursos visitam todos os nós uma vez, portanto possuem custo `O(n)`.

## Sugestões para praticar

1. Altere a lista `values` e desenhe a nova árvore antes de executar.
2. Confirme que o percurso em ordem sempre imprime os valores ordenados.
3. Adicione uma função para contar a quantidade de nós.
4. Crie uma função para encontrar o menor e o maior valor.
5. Implemente uma função de busca usando a mesma lógica da inserção.
6. Teste valores repetidos e observe em qual lado eles são colocados.

## Conceitos principais

- estrutura de dados não linear;
- árvore binária;
- árvore binária de busca;
- raiz, filhos e folhas;
- recursão;
- percurso em pré-ordem;
- percurso em ordem;
- percurso em pós-ordem;
- análise de complexidade.
