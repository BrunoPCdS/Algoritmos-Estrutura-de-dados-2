# Aula 3 - Insertion Sort e leitura de dados

Esta aula aplica o **Insertion Sort** a números armazenados em arquivos CSV. Há versões progressivas do mesmo exercício: uma implementação mais didática, versões enxutas e uma tentativa de medir o ganho de desempenho com NumPy e Numba.

## O que, por que e quando

O Insertion Sort considera que a parte inicial da lista já está ordenada. Para cada novo elemento, guarda a chave, desloca para a direita os valores maiores e insere a chave na posição correta.

Ele é simples, estável e funciona bem em listas pequenas ou quase ordenadas. No pior caso, seu tempo é $O(n^2)$; no melhor caso, quando a lista já está ordenada, é $O(n)$. A ordenação ocorre na própria lista, usando memória extra $O(1)$, além da entrada.

## Arquivos Python

### `ex04.py`

É a versão mais explicada. `ler_csv` ignora o cabeçalho `numero`, lê os valores do arquivo e pode receber um limite. Depois carrega todos os números de `numeros_1M_embaralhado.csv`, ordena a lista e mostra os 50 primeiros resultados. Para um milhão de elementos, o custo quadrático pode ser muito alto.

### `exercicio04.py`

É uma versão mais robusta e modular. Lê valores válidos, pode ignorar linhas vazias, seleciona apenas os 20 primeiros números, remove duplicatas preservando a primeira ocorrência e só então aplica o Insertion Sort. Também aceita o nome do CSV pela linha de comando.

Exemplo:

```bash
python exercicio04.py numeros_1M_embaralhado.csv
```

### `exercicio04ok.py` e `exok04.py`

São versões simplificadas do mesmo algoritmo. Ambas ignoram a primeira linha como cabeçalho, aceitam um limite opcional na função de leitura e ordenam dados do arquivo de 1 milhão de números. A principal diferença é o limite usado na chamada: `exok04.py` usa 10.000 elementos, enquanto `exercicio04ok.py` chama a função sem limite e, portanto, lê o arquivo inteiro.

### `test.py`

Usa `numpy.loadtxt` para carregar o CSV como um array de inteiros e `@njit`, do Numba, para compilar o Insertion Sort. Mede somente o tempo da ordenação com `time.time()`. A primeira execução pode incluir o custo de compilação do Numba, então comparações justas devem considerar aquecimento e repetir os testes.

Esse arquivo depende de `numpy` e `numba`, ao contrário das outras versões. Mesmo compilado, o algoritmo continua sendo Insertion Sort: a implementação melhora a constante de tempo, mas não muda a ordem de crescimento $O(n^2)$.

## Arquivos de dados

- `numeros_1M_embaralhado.csv`: CSV com cabeçalho `numero` e aproximadamente 1 milhão de números.
- `numeros_10M_embaralhado.csv`: conjunto maior, útil para observar o impacto do tamanho da entrada. Ele pode exigir bastante tempo e memória.

## Como executar

A partir desta pasta:

```bash
python ex04.py
python exercicio04.py numeros_1M_embaralhado.csv
python exercicio04ok.py
python exok04.py
```

Para a versão otimizada, instale as dependências no ambiente Python e execute:

```bash
python -m pip install numpy numba
python test.py
```

## Cuidados importantes

As funções `ler_csv` das versões didáticas chamam `next` para descartar o cabeçalho. Portanto, elas esperam um CSV no formato atual. `exercicio04.py` é a versão mais defensiva quando há linhas vazias ou valores inválidos.

Ao comparar resultados, confirme se todas as versões estão lendo a mesma quantidade de elementos. Comparar um arquivo inteiro com uma amostra de 10.000 números não mede o mesmo trabalho.

## Roteiro de estudo

1. Simule manualmente a inserção de um elemento em uma lista pequena.
2. Execute `ex04.py` com um limite baixo e acompanhe os deslocamentos.
3. Compare tempo e quantidade de dados entre as versões.
4. Pense em que cenário outro algoritmo, como Merge Sort ou Quick Sort, seria mais adequado.
