# Aula 9 - Busca Gulosa (Greedy Best-First)

Este exercício implementa a busca de um caminho em um labirinto representado
por uma grade. O objetivo é sair da posição `I` (início) e chegar à posição
`F` (fim), atravessando somente as casas livres.

Na representação do labirinto:

- `#` representa uma parede;
- `.` representa uma casa livre;
- `I` representa o início;
- `F` representa a saída;
- `*` marca o caminho encontrado na saída do programa.

## Implementações

O arquivo [`labirinto.py`](./labirinto.py) converte a grade em um grafo. Cada
casa livre é um vértice, e existe uma aresta entre duas casas que são
vizinhas na vertical ou na horizontal.

O programa compara três estratégias:

### Busca em profundidade (DFS)

A DFS usa uma pilha e explora um caminho até o mais longe possível antes de
voltar para testar alternativas. O caminho encontrado depende da ordem dos
vizinhos e não é necessariamente o menor caminho.

### Busca em largura (BFS)

A BFS usa uma fila e explora o grafo por níveis. Como cada movimento possui o
mesmo custo, ela garante o menor caminho em quantidade de movimentos. Seu custo
é `O(V + E)`, em que `V` é o número de casas livres e `E` é o número de
conexões entre elas.

### Busca gulosa (Greedy Best-First)

A busca gulosa usa uma fila de prioridade (`heapq`) e escolhe a casa com menor
distância Manhattan até a saída:

```text
|linha_atual - linha_saida| + |coluna_atual - coluna_saida|
```

Ela tenta avançar na direção do objetivo e, neste exemplo, explora menos casas.
Entretanto, considera somente a estimativa até a saída; por isso, ao contrário
da BFS, não há garantia de que encontrará o menor caminho em labirintos
arbitrários. Com a fila de prioridade, seu custo típico é
`O((V + E) log V)`.

Todas as buscas usam um dicionário de predecessores para reconstruir o caminho
quando a saída é encontrada. O programa também imprime a quantidade de casas
visitadas, permitindo comparar o esforço de cada estratégia.

## Resultados obtidos

Executando o labirinto fornecido, os três algoritmos chegam à saída pelo mesmo
caminho, com 22 movimentos:

| Busca | Movimentos | Casas visitadas |
| --- | ---: | ---: |
| DFS | 22 | 47 |
| BFS | 22 | 55 |
| Gulosa | 22 | 45 |

Neste caso, a busca gulosa visitou 45 casas, menos que a DFS (47) e a BFS (55).
Isso não significa que ela seja sempre melhor: o resultado depende do desenho
do labirinto e da heurística utilizada. A BFS é a referência para garantir o
menor número de movimentos neste tipo de grade.

## Como executar

No terminal, a partir da raiz do repositório, execute:

```powershell
python ".\Aula 9 - Busca Gulosa greedy best-first\labirinto.py"
```

O programa imprime o labirinto com o caminho marcado e, ao final, uma tabela
comparativa entre as três buscas.
