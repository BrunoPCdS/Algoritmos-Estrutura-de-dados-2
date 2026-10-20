from collections import deque
from heapq import heappop, heappush


labirinto = [
    "I###########",
    ".........###",
    "#.######.###",
    "#..##...####",
    "##.#####...#",
    "##.###...###",
    "##.........#",
    "##..########",
    "##...###..##",
    "#.#.##...###",
    "#......#.###",
    "#.#..###.F##",
    ]

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]



def livre(lab, coluna, linha):
    dentro = 0 <= coluna < len(lab) and 0 <= linha < len(lab[0])
    return dentro and lab[coluna][linha] != "#"


def montar_grafo(lab):
    grafo = {}
    for coluna in range(len(lab)):
        for linha in range(len(lab[0])):
            if livre(lab, coluna, linha):
                grafo[(coluna, linha)] = [
                    (coluna + dcoluna, linha + dlinha)
                    for dcoluna, dlinha in DIRECOES
                    if livre(lab, coluna + dcoluna, linha + dlinha)
                ]
    return grafo


def localizar(lab, marcador):
    for coluna, linha in enumerate(lab):
        for linha, valor in enumerate(linha):
            if valor == marcador:
                return (coluna, linha)
    raise ValueError(f"Marcador {marcador!r} não encontrado.")


def reconstruir_caminho(anteriores, atual):
    caminho = []
    while atual is not None:
        caminho.append(atual)
        atual = anteriores[atual]
    return caminho[::-1]

# -----------------------------------------------------------------------

def dfs(grafo, inicio, saida):
    """Busca em profundidade. Retorna (caminho, casas_visitadas)."""
    pilha = [inicio]
    anteriores = {inicio: None}
    visitadas = []

    while pilha:
        atual = pilha.pop()
        visitadas.append(atual)
        if atual == saida:
            return reconstruir_caminho(anteriores, atual), visitadas

        for vizinho in reversed(grafo[atual]):
            if vizinho not in anteriores:
                anteriores[vizinho] = atual
                pilha.append(vizinho)

    return [], visitadas


def bfs(grafo, inicio, saida):
    """Busca em largura. Retorna (caminho, casas_visitadas)."""
    fila = deque([inicio])
    anteriores = {inicio: None}
    visitadas = []

    while fila:
        atual = fila.popleft()
        visitadas.append(atual)
        if atual == saida:
            return reconstruir_caminho(anteriores, atual), visitadas

        for vizinho in grafo[atual]:
            if vizinho not in anteriores:
                anteriores[vizinho] = atual
                fila.append(vizinho)

    return [], visitadas


def heuristica(posicao, destino):
    return abs(posicao[0] - destino[0]) + abs(posicao[1] - destino[1])


def gulosa(grafo, inicio, saida):
    """Busca gulosa pela distância Manhattan. Retorna (caminho, visitadas)."""
    fronteira = [(heuristica(inicio, saida), inicio)]
    anteriores = {inicio: None}
    visitadas = []

    while fronteira:
        _, atual = heappop(fronteira)
        visitadas.append(atual)
        if atual == saida:
            return reconstruir_caminho(anteriores, atual), visitadas

        for vizinho in grafo[atual]:
            if vizinho not in anteriores:
                anteriores[vizinho] = atual
                prioridade = heuristica(vizinho, saida)
                heappush(fronteira, (prioridade, vizinho))

    return [], visitadas


#------------------------------------------------------------------------


def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for coluna, linha in caminho:
        if grade[coluna][linha] == ".":
            grade[coluna][linha] = "*"
    for linha in grade:
        print("".join(linha))


def executar(nome, busca, grafo, inicio, saida):
    caminho, visitadas = busca(grafo, inicio, saida)
    print(f"\n===== {nome} =====")
    desenhar(labirinto, caminho)
    print(f"Tamanho do caminho: {len(caminho) - 1} movimentos")
    print(f"Casas visitadas: {len(visitadas)}")
    return len(caminho) - 1, len(visitadas)


grafo = montar_grafo(labirinto)
inicio = localizar(labirinto, "I")
saida = localizar(labirinto, "F")

resultados = {
    "DFS": executar("DFS", dfs, grafo, inicio, saida),
    "BFS": executar("BFS", bfs, grafo, inicio, saida),
    "Gulosa": executar("Gulosa", gulosa, grafo, inicio, saida),
}

print("\n===== TABELA COMPARATIVA =====")
print(f"{'Busca':<10} {'Movimentos':>12} {'Visitadas':>12}")
for nome, (tamanho, visitadas) in resultados.items():
    print(f"{nome:<10} {tamanho:>12} {visitadas:>12}")
