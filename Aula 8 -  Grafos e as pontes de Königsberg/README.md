# Aula 8 - Grafos e as pontes de Königsberg

O arquivo representa o problema histórico das pontes de Königsberg como um grafo e usa duas ideias: graus de vértices para analisar um passeio de Euler e DFS para percorrer o grafo.

## O que é um grafo

Um grafo é formado por vértices e arestas. No programa, as letras `A`, `B`, `C` e `D` são vértices, e cada item nas listas de vizinhos representa uma ponte. Repetições representam pontes paralelas. Como cada ponte aparece na lista dos dois extremos, o grafo é não direcionado.

O grau de um vértice é a quantidade de arestas incidentes nele. O programa calcula:

- `A`: grau 5;
- `B`: grau 3;
- `C`: grau 4;
- `D`: grau 2.

## Condição de Euler

Um passeio de Euler atravessa cada aresta exatamente uma vez. Em um grafo conectado, ele existe quando há zero vértices de grau ímpar, caso fechado, ou dois vértices de grau ímpar, caso aberto.

Aqui existem dois vértices ímpares (`A` e `B`), portanto o programa informa que existe um passeio de Euler aberto. A regra responde à possibilidade matemática; ela não imprime a sequência concreta das pontes.

## DFS: busca em profundidade

A função `dfs` visita um vértice, marca-o no conjunto `visitados` e explora recursivamente seus vizinhos. A marcação é essencial em grafos com ciclos: sem ela, o percurso poderia voltar indefinidamente entre os mesmos vértices.

A função `dfs_sem_visitados` existe justamente para demonstrar o problema, mas sua chamada está comentada. Se fosse executada neste grafo, entraria em recursão infinita até gerar um erro de profundidade de recursão.

## Arquivo

### `pointesKonigsberg.py`

Executa quatro etapas: cria a lista de adjacência, calcula os graus, verifica a condição de Euler e realiza uma DFS a partir de `A`. A DFS visita cada vértice alcançável uma vez; considerando a representação por listas, o custo é $O(V + E)$.

## Como executar

```bash
python pointesKonigsberg.py
```

## Quando usar cada ideia

- Use **grau de vértice** para analisar conexões e problemas de rotas.
- Use **Euler** quando a exigência for percorrer cada aresta exatamente uma vez.
- Use **DFS** para explorar conectividade, componentes, ciclos e caminhos.
- Use um conjunto de visitados em percursos que podem retornar a um vértice já explorado.

## Experimentos sugeridos

Adicione uma ponte entre dois vértices e recalcule os graus. Observe como a paridade muda. Depois, altere a origem da DFS e compare a ordem de visita. Para estudar o passeio em si, o próximo passo seria implementar um algoritmo de construção de caminho de Euler, como Hierholzer.
