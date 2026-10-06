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



## detalhamento para leigo --- Algoritimo de Hierholzer


1. grafo_copia = {v: vizinhos[:] for v, vizinhos in grafo.items()}
grafo.items() → retorna pares (chave, valor) do dicionário.
Exemplo: para grafo = {'A': ['B','C'], 'B':['A']}, o .items() gera:

Código
('A', ['B','C'])
('B', ['A'])
for v, vizinhos in grafo.items() → significa:

v recebe a chave (o vértice, como 'A', 'B'...).

vizinhos recebe a lista associada (os vizinhos daquele vértice).

vizinhos[:] → é uma cópia da lista inteira.

[:] é um “fatiamento” que pega todos os elementos.

Isso evita modificar a lista original.

{v: vizinhos[:] for v, vizinhos in grafo.items()} → cria um novo dicionário, onde cada chave v tem como valor uma cópia da lista de vizinhos.

2. graus = {v: len(vizinhos) for v, vizinhos in grafo.items()}
Estrutura parecida com a anterior.

len(vizinhos) → conta quantos elementos tem a lista de vizinhos (ou seja, o grau do vértice).

Resultado: um dicionário com cada vértice e seu grau.
Exemplo: {'A': 5, 'B': 3, 'C': 4, 'D': 2}.

3. inicio = impares[0] if impares else list(grafo.keys())[0]
impares[0] → pega o primeiro vértice da lista de ímpares.

[0] significa “primeiro elemento”.

if impares else ... → é um “if curto”:

Se impares não está vazio, usa o primeiro ímpar.

Se está vazio, usa o que vem depois do else.

grafo.keys() → retorna todas as chaves do dicionário (os vértices).
Exemplo: dict_keys(['A','B','C','D']).

list(grafo.keys())[0] → transforma em lista e pega o primeiro vértice.

4. grafo_copia[v]
Aqui, v é um vértice (como 'A').

grafo_copia[v] acessa a lista de vizinhos desse vértice.
Exemplo: se v = 'A', então grafo_copia['A'] = ['B','B','C','C','D'].

5. grafo_copia[u]
u é o vizinho escolhido de v.

Exemplo: se v = 'A' e escolhemos u = 'B', então grafo_copia['B'] acessa a lista de vizinhos de 'B'.

6. caminho[::-1]
Isso é um fatiamento invertido.

[::] significa “pega todos os elementos”.

O -1 significa “na ordem inversa”.

Exemplo:

python
lista = [1,2,3,4]
lista[::-1]   # resultado: [4,3,2,1]
Usamos isso porque o algoritmo constrói o caminho ao contrário, então no final precisamos inverter.

🎯 Resumindo
items() → percorre chave e valor do dicionário.

[:] → copia uma lista inteira.

[0] → primeiro elemento de uma lista.

keys() → retorna todas as chaves do dicionário.

grafo_copia[v] → acessa a lista de vizinhos do vértice v.

[::-1] → inverte a ordem de uma lista.