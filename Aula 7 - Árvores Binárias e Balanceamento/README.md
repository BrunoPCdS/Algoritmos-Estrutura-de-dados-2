# Aula 7 - Árvores Binárias e Balanceamento

Este exercício foi desenvolvido com base na proposta da aula de estruturas de dados, focando em operações de rotação em árvores AVL e na comparação entre uma árvore binária de busca (BST) e uma árvore AVL.

## Objetivo

O principal objetivo da atividade é:

- implementar as quatro rotações básicas de árvores AVL;
- verificar o comportamento das árvores antes e depois das rotações;
- comparar a altura final de uma BST e de uma AVL após a inserção de uma mesma sequência de valores;
- analisar a quantidade de comparações necessária para buscar um valor específico.

## Exercício 1: Implementar as quatro rotações

A primeira parte do exercício pede que sejam implementadas as rotações:

1. `rotacao_direita`
2. `rotacao_esquerda`
3. `rotacao_esquerda_direita`
4. `rotacao_direita_esquerda`

Essas rotações são fundamentais para manter a árvore balanceada em uma AVL.

### Como testar

Para cada rotação, deve-se:

- criar uma árvore com valores de exemplo;
- imprimir a travessia em ordem antes da rotação;
- aplicar a rotação;
- imprimir novamente a travessia em ordem;
- verificar se a estrutura foi ajustada corretamente.

A ideia é confirmar que a árvore continua representando corretamente a ordem dos elementos e que a operação de rotação foi aplicada de forma consistente.

## Exercício 2: BST vs. AVL

A segunda parte do exercício propõe inserir a sequência de valores na seguinte ordem:

`30 -> 20 -> 10 -> 25 -> 27 -> 40 -> 35`

Esses dados devem ser inseridos em duas estruturas:

- BST
- AVL

Depois disso, é necessário comparar as alturas finais das árvores. O foco é observar que, enquanto a BST pode ficar desbalanceada, a AVL realiza rotações para manter a altura do menor possível.

Além disso, o exercício pergunta:

> Quantas comparações cada busca pelo valor 35 custa?

Esse questionamento mostra a importância do balanceamento, porque em uma árvore balanceada a busca é mais eficiente em termos de custo de comparação.

## Estrutura do código

O arquivo principal do exercício é:

- `exercicio.py`

Nele estão presentes:

- a classe `Node`, que representa cada nó da árvore;
- os métodos de cálculo da altura;
- as funções de rotação;
- um teste simples para demonstrar a rotação à direita.

## Execução

Para executar o exemplo do exercício, basta rodar:

```bash
python exercicio.py
```

A saída mostrará a árvore antes e depois da rotação à direita, permitindo observar o efeito da operação em ordem.

## Conclusão

Este exercício trabalha com dois conceitos centrais da estrutura de dados:

- a manutenção da ordem dos elementos em árvores binárias de busca;
- o balanceamento de árvores AVL para melhorar a eficiência de operações como busca, inserção e remoção.

Ao concluir a atividade, o aluno consegue visualizar de forma prática como as rotações corrigem desequilíbrios e por que árvores AVL são preferíveis em cenários onde a performance de busca é importante.
