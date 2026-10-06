## O método clássico para encontrar um caminho euleriano (se existir) é o algoritmo de Hierholzer:

##Escolhe um vértice inicial (se houver dois ímpares, começa em um deles).

## Percorre arestas sem repetir, formando um ciclo ou caminho.

##Se ainda restarem arestas não usadas, “encaixa” novos ciclos no caminho.

##No fim, se todas as arestas foram usadas, temos um caminho euleriano.

def caminho_euleriano(grafo):
    # Copiar o grafo para não destruir o original
    grafo_copia = {v: vizinhos[:] for v, vizinhos in grafo.items()}

    # Encontrar vértices ímpares
    graus = {v: len(vizinhos) for v, vizinhos in grafo.items()}
    impares = [v for v, g in graus.items() if g % 2 == 1]

    # Se não houver 0 ou 2 ímpares, não existe caminho
    if len(impares) not in (0, 2):
        return None

    # Escolher vértice inicial
    inicio = impares[0] if impares else list(grafo.keys())[0]

    caminho = []
    pilha = [inicio]

    while pilha:
        v = pilha[-1]
        if grafo_copia[v]:
            u = grafo_copia[v].pop()   # pega um vizinho
            grafo_copia[u].remove(v)   # remove a ponte dos dois lados
            pilha.append(u)
        else:
            caminho.append(pilha.pop())

    return caminho[::-1]  # inverter para ordem correta


# Testando no grafo das pontes de Königsberg
grafo = {
    'A': ['B', 'B', 'C', 'C', 'D'],
    'B': ['A', 'A', 'C'],
    'C': ['A', 'A', 'B', 'D'],
    'D': ['A', 'C']
}

resultado = caminho_euleriano(grafo)
print("Caminho Euleriano:", resultado)



##Quando você rodar esse código:

##Ele vai tentar construir um caminho euleriano.

##Mas no fim, o resultado será None ou um caminho incompleto, porque não é possível usar todas as pontes sem repetir.

##Isso confirma a prova de Euler: o grafo das pontes de Königsberg não tem caminho euleriano.