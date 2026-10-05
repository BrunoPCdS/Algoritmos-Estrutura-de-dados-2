# Algoritmos e Estruturas de Dados II

Repositório de exercícios e experimentos da disciplina de **Algoritmos e
Estruturas de Dados II**. O material foi organizado por aula e apresenta, de
forma progressiva, técnicas de enumeração, ordenação, busca e estruturas de
dados não lineares.

O objetivo deste README é servir como ponto de entrada para:

- localizar o conteúdo de cada aula;
- preparar o ambiente de execução;
- executar os exemplos;
- testar e comparar implementações;
- sugerir uma sequência de estudos e experimentos.

## Conteúdo do repositório

| Aula | Tema | Conceitos principais |
| --- | --- | --- |
| [Aula 1](./Aula%201%20-%20base%20de%20algoritimos/) | Base de algoritmos e estruturas de dados | Percursos, pilha, fila, lista, conjunto e dicionário |
| [Aula 2](./Aula%202%20-%20Enumera%C3%A7%C3%A3o%20de%20casos%20com%20bits/) | Enumeração de casos com bits | Representação binária e geração de combinações |
| [Aula 3](./Aula%203%20-%20Insertion%20Sort%20e%20leitura%20de%20dados/) | Insertion Sort e leitura de dados | Ordenação, CSV, análise de desempenho e Numba |
| [Aula 5](./Aula%205%20-%20Busca%20por%20interpola%C3%A7%C3%A3o/) | Busca por interpolação | Busca em lista ordenada e estimativa de posição |
| [Aula 6](./Aula%206%20-%20%C3%81rvore%20Bin%C3%A1ria%20de%20Busca/) | Árvore Binária de Busca (BST) | Nós, recursão, inserção e percursos |
| [Aula 7](./Aula%207%20-%20%C3%81rvores%20Bin%C3%A1rias%20e%20Balanceamento/) | Árvores binárias e balanceamento | Rotações e árvores AVL |
| [Aula 8](./Aula%208%20-%20%20Grafos%20e%20as%20pontes%20de%20K%C3%B6nigsberg/) | Grafos e pontes de Königsberg | Lista de adjacência, graus, Euler e DFS |

> A numeração não contém uma Aula 4 neste conjunto de arquivos.

Cada pasta possui um README próprio com a explicação detalhada do exercício,
quando disponível. Este arquivo apresenta a visão geral e os comandos mais
importantes.

## Pré-requisitos

Instale:

- **Python 3.9 ou superior**, recomendado para os exercícios em Python;
- **Node.js** e `npm`, necessários apenas para os exercícios JavaScript da
  Aula 1;
- um terminal e um editor de código, como o Visual Studio Code.

Não há uma dependência Python comum para todas as aulas. A maior parte dos
programas usa apenas a biblioteca padrão. `numpy` e `numba` são necessários
somente para o benchmark da Aula 3.

## Como obter e abrir o projeto

Abra a pasta raiz do projeto no terminal. Como os nomes das pastas contêm
espaços e acentos, use aspas no caminho quando necessário:

```powershell
cd "c:\caminho\para\exercicios - Algoritimos e Estruturas de dados II"
```

No Windows, os comandos podem ser executados com `python`. Se esse comando não
estiver disponível, tente `py`:

```powershell
python --version
node --version
npm --version
```

## Instalação das dependências

### JavaScript da Aula 1

Entre na pasta da Aula 1 e instale a dependência declarada no `package.json`:

```powershell
cd "Aula 1 - base de algoritimos"
npm install
```

Isso instala o `prompt-sync`, usado pelos exercícios que recebem entrada do
teclado.

### Benchmark da Aula 3

O arquivo `test.py` usa NumPy e Numba. Instale-os no ambiente Python que será
usado para executar o arquivo:

```powershell
python -m pip install numpy numba
```

## Execução por aula

Os comandos abaixo devem ser executados dentro da pasta indicada.

### Aula 1 — base de algoritmos

```powershell
cd "Aula 1 - base de algoritimos"
node exercicio01.js
node exercicio02.js
python exercicio03.py
python exercicio04.py
python exercicio05.py
python exercicio06.py
python exercicio07.py
python exercicio08.py
```

Os dois programas JavaScript solicitam dados no terminal. O `exercicio04.py`
possui um menu e continua em execução até a opção de saída ser selecionada.

### Aula 2 — enumeração com bits

```powershell
cd "..\Aula 2 - Enumeração de casos com bits"
python 01.py
```

Com oito condições, o programa gera `2^8 = 256` combinações.

### Aula 3 — Insertion Sort

```powershell
cd "..\Aula 3 - Insertion Sort e leitura de dados"
python ex04.py
python exercicio04.py numeros_1M_embaralhado.csv
python exercicio04ok.py
python exok04.py
```

O arquivo `exercicio04.py` também aceita outro CSV como argumento:

```powershell
python exercicio04.py numeros_10M_embaralhado.csv
```

O arquivo `test.py` executa a versão compilada com Numba:

```powershell
python test.py
```

Os arquivos `numeros_1M_embaralhado.csv` e `numeros_10M_embaralhado.csv` são
grandes. O Insertion Sort possui custo quadrático no pior caso (`O(n²)`), por
isso os testes com muitos elementos podem demorar e consumir bastante memória.
A primeira execução de `test.py` inclui o tempo de compilação do Numba; para
comparações, execute mais de uma vez e considere o aquecimento.

### Aula 5 — busca por interpolação

```powershell
cd "..\Aula 5 - Busca por interpolação"
python exercicio05.py
```

O exemplo procura o valor `70` em uma lista ordenada. A busca por interpolação
é mais adequada a dados numéricos ordenados e distribuídos de maneira
aproximadamente uniforme.

### Aula 6 — árvore binária de busca

```powershell
cd "..\Aula 6 - Árvore Binária de Busca"
python exercicio.py
```

O percurso em ordem deve exibir os valores em ordem crescente. A inserção
recursiva pode custar `O(log n)` em uma árvore equilibrada e `O(n)` no pior caso.

### Aula 7 — rotações e AVL

```powershell
cd "..\Aula 7 - Árvores Binárias e Balanceamento"
python exercicio.py
```

O exemplo demonstra uma rotação à direita. O arquivo também contém as
rotações à esquerda, esquerda-direita e direita-esquerda, que são a base do
balanceamento AVL.

### Aula 8 — grafos

```powershell
cd "..\Aula 8 -  Grafos e as pontes de Königsberg"
python pointesKonigsberg.py
```

O programa calcula os graus dos vértices, verifica a condição de existência de
um passeio de Euler e percorre o grafo com busca em profundidade (DFS). A DFS
com controle de visitados custa `O(V + E)`, considerando a representação por
listas de adjacência.

## Testes e experimentos

Não existe, atualmente, uma suíte automatizada única para todo o repositório.
Os próprios programas funcionam como exemplos executáveis e testes manuais.

Para estudar e validar o comportamento:

1. Execute cada arquivo com os dados fornecidos e compare a saída com o README
   da respectiva aula.
2. Teste entradas vazias, valores repetidos, números negativos e valores que
   não estejam presentes.
3. Na Aula 2, altere a quantidade de condições e confirme que o total é `2^n`.
4. Na Aula 3, compare listas pequenas, listas já ordenadas e listas em ordem
   inversa; registre o tempo e a quantidade de elementos.
5. Na Aula 5, altere o valor procurado e mantenha a lista ordenada.
6. Na Aula 6, altere a ordem de inserção e observe como a forma da BST muda.
7. Na Aula 7, confira se a travessia em ordem permanece ordenada antes e depois
   das rotações.
8. Na Aula 8, adicione ou remova uma ponte e observe a mudança na paridade dos
   graus.

Ao comparar algoritmos, mantenha constantes o tamanho e o conteúdo da entrada.
Uma medição com 20 elementos não deve ser comparada diretamente com outra feita
com 1 milhão de elementos.

## Roteiro de estudos sugerido

1. Revise percursos lineares, seleção e complexidade na Aula 1.
2. Estude a representação binária e o crescimento exponencial na Aula 2.
3. Implemente o Insertion Sort manualmente e depois analise os dados da Aula 3.
4. Compare a busca por interpolação com uma busca linear em uma lista ordenada.
5. Desenhe a BST da Aula 6 antes de executar os percursos.
6. Use as rotações da Aula 7 para entender como o balanceamento reduz a altura.
7. Modele o problema das pontes como um grafo e diferencie Euler de DFS.
8. Para cada exercício, identifique entrada, saída, estrutura usada,
   complexidade de tempo e complexidade de memória.

## Organização dos arquivos

Cada pasta de aula contém os códigos e, em algumas aulas, um README específico.
Os arquivos CSV ficam junto do código que os consome. Evite mover esses arquivos
de dados sem atualizar os caminhos usados pelos programas.

Os exercícios são independentes: é possível estudar ou executar uma aula sem
executar as anteriores. A sequência sugerida serve apenas para facilitar a
progressão dos conceitos.
