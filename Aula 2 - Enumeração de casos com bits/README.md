# Aula 2 - Enumeração de casos com bits

O arquivo desta pasta gera todas as combinações possíveis de oito condições de cadastro. Cada condição pode estar em dois estados: falsa ou verdadeira.

## O que está sendo estudado

O programa usa a representação binária dos números de `0` a `2^n - 1`. Cada bit representa uma condição:

- bit `0`: possui email;
- bit `1`: possui telefone;
- bit `2`: possui endereço;
- e assim por diante até as oito condições.

A expressão `numero & (1 << i)` verifica se o bit `i` está ligado. O resultado é convertido para `bool` e armazenado em um dicionário.

Para `n` condições existem $2^n$ casos. Como `n = 8`, o programa gera $2^8 = 256$ combinações.

## Arquivo

### `01.py`

1. Define a lista de condições.
2. Calcula a quantidade de condições com `len`.
3. Percorre todos os números de `0` até `2 ** n - 1`.
4. Converte os bits de cada número em valores booleanos.
5. Guarda cada caso na lista `casos`.
6. Exibe o total e os cinco primeiros casos.

O custo de geração é proporcional a $n \cdot 2^n$, porque cada um dos $2^n$ casos examina as $n$ condições. A memória usada para guardar todos os casos também cresce exponencialmente.

## Por que e quando usar

Essa técnica é útil para testar regras de negócio, validar tabelas-verdade, explorar subconjuntos e gerar cenários de testes. Ela deixa de ser prática quando o número de condições cresce muito: com 20 condições já são mais de um milhão de combinações.

## Como executar

```bash
python 01.py
```

A saída informa `256` casos e mostra uma amostra inicial. O primeiro caso representa todos os bits desligados; os casos seguintes ligam as condições gradualmente conforme a contagem binária avança.

## Experimentos sugeridos

- Altere a lista para quatro condições e confira que surgem $2^4 = 16$ casos.
- Adicione uma condição e observe que o total dobra.
- Remova `casos.append(caso)` e compare o custo de apenas imprimir com o custo de armazenar tudo.
- Relacione cada caso a uma regra, por exemplo: cliente premium exige cadastro completo.
