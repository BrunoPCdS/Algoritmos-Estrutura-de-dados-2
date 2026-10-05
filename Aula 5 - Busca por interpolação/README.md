# Aula 5 - Busca por interpolação

O exercício desta pasta procura o valor `70` em uma lista ordenada e distribuída uniformemente: `[10, 20, 30, 40, 50, 60, 70, 80, 90]`.

## O que é busca por interpolação

A busca por interpolação estima a posição do valor usando a distância proporcional entre os extremos. A fórmula usada é:

$$
posicao = baixo + \frac{(alvo - lista[baixo]) (alto - baixo)}{lista[alto] - lista[baixo]}
$$

Depois da estimativa, o algoritmo compara o valor encontrado com o alvo e reduz o intervalo para a parte inferior ou superior.

## Por que e quando usar

Em dados numéricos ordenados e aproximadamente uniformes, a interpolação pode localizar o alvo muito rapidamente, com desempenho médio próximo de $O(\log \log n)$. Em dados concentrados ou mal distribuídos, pode cair para $O(n)$.

A busca binária é uma alternativa mais previsível, com $O(\log n)$, e funciona sem depender da distribuição dos valores. A interpolação só deve ser escolhida quando a lista está ordenada, os valores são numéricos e a distribuição favorece a estimativa.

## Arquivo

### `exercicio05.py`

- Define a lista ordenada.
- Mantém os limites `low` e `high`.
- Enquanto o alvo estiver dentro do intervalo, calcula uma posição estimada.
- Retorna o índice quando encontra `70`.
- Retorna `-1` quando o valor não está presente.
- Trata o caso em que os extremos são iguais para evitar divisão por zero.

Na lista atual, o valor `70` está no índice `6`, então a saída informa esse índice.

## Como executar

```bash
python exercicio05.py
```

## Experimentos sugeridos

Altere o alvo no código e teste um valor inexistente, como `75`. Também teste listas com intervalos irregulares e compare o comportamento com uma busca binária. Lembre-se de manter a lista ordenada: sem essa condição, os limites deixam de representar um intervalo válido para o algoritmo.
