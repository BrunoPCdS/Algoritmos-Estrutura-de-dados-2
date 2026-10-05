# Aula 1 - Base de algoritmos e estruturas de dados

Esta pasta reúne exercícios introdutórios de processamento de dados e de estruturas de dados clássicas. A sequência começa com percursos simples em texto e números e avança para pilha, fila, listas, conjuntos e dicionários.

## O que, por que e quando

- **Percurso e seleção:** percorremos cada item e decidimos se ele deve ser contado ou transformado. É útil quando o dado precisa ser analisado uma vez.
- **Pilha (stack):** segue a regra LIFO, isto é, o último elemento inserido é o primeiro a sair. Aparece em desfazer ações, chamadas de funções e navegação de histórico.
- **Fila (queue):** segue a regra FIFO, o primeiro a entrar é o primeiro a sair. Representa atendimento, impressão e processamento de tarefas.
- **Lista:** mantém uma sequência ordenada e pode conter repetição. É uma estrutura geral para coleções simples.
- **Conjunto (set):** guarda valores únicos. É indicado para remover duplicatas e testar pertencimento rapidamente.
- **Dicionário (dict):** associa uma chave a um valor. É apropriado para buscas por identificador e contagens.

## Arquivos

### `exercicio01.js` - contagem de dígitos pares

Lê um número como texto e percorre seus caracteres. Converte cada dígito para número e incrementa o contador quando ele é par, ignorando o zero. Tratar a entrada como texto facilita visitar cada dígito sem cálculos de divisão. A complexidade é $O(n)$, em que $n$ é a quantidade de dígitos.

### `exercicio02.js` - substituição de vogais

A versão ativa usa `replace(/[aeiouAEIOU]/g, "*")` para trocar todas as vogais por asteriscos. O bloco comentado mostra a mesma ideia usando um laço, uma alternativa importante para entender o algoritmo antes de usar uma expressão regular. A complexidade também é $O(n)$.

### `exercicio03.py` - inversão com pilha

Insere cada letra em uma lista usada como pilha e depois remove com `pop()`. Como a remoção ocorre do fim para o começo, a palavra é invertida. O exercício demonstra LIFO de forma concreta e usa $O(n)$ tempo e $O(n)$ memória.

### `exercicio04.py` - simulação de fila

Oferece um menu para adicionar pessoas no final (`append`), atender a primeira pessoa (`pop(0)`) e listar a fila. A regra observada é FIFO. Para filas grandes, `collections.deque` seria melhor, pois `pop(0)` desloca os demais elementos e custa $O(n)$.

### `exercicio05.py` - remoção de números negativos

Percorre a lista `[1, -2, 3, -4, 5]` e cria outra contendo apenas valores maiores ou iguais a zero. Criar uma nova lista preserva a original. O laço custa $O(n)$. Observação: a variável do laço reutiliza o nome `numero`, então a mensagem `Lista original` acaba imprimindo o último número percorrido, e não a lista original; isso é um ponto útil para revisar nomes de variáveis e escopo.

### `exercicio06.py` - remoção de duplicatas

Converte uma lista em `set`, eliminando repetições. É uma solução curta quando a ordem dos elementos não importa. Como conjuntos não devem ser usados para representar uma sequência ordenada, a ordem exibida pode variar.

### `exercicio07.py` - contagem de palavras

Separa uma frase com `split()` e usa um dicionário para acumular quantas vezes cada palavra aparece. `get(palavra, 0)` fornece zero para a primeira ocorrência. É um padrão usado em contadores, frequência de termos e histogramas. A complexidade média é $O(n)$.

### `exercicio08.py` - agenda de contatos

Usa um dicionário em que o nome é a chave e o telefone é o valor. `buscar_telefone` faz uma consulta e `listar_contatos` percorre todos os pares com `items()`. Dicionários são adequados quando precisamos localizar um registro pela chave.

## Como executar

Na pasta desta aula, instale a dependência JavaScript uma vez:

```bash
npm install
```

Execute os exemplos com:

```bash
node exercicio01.js
node exercicio02.js
python exercicio03.py
python exercicio04.py
python exercicio05.py
python exercicio06.py
python exercicio07.py
python exercicio08.py
```

Os dois primeiros programas pedem uma entrada no terminal. O `exercicio04.py` continua executando até a opção `4` ser escolhida.

## Roteiro de estudo

1. Observe os laços dos exercícios 01 e 02.
2. Compare a pilha do exercício 03 com a fila do exercício 04.
3. Escolha entre lista, conjunto e dicionário conforme a operação principal: sequência, unicidade ou busca por chave.
4. Teste entradas vazias, valores repetidos, letras maiúsculas e listas já sem elementos especiais.
