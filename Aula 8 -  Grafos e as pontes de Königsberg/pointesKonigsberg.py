# Representação do grafo das pontes de Königsberg
# Cada vértice guarda a lista dos seus vizinhos
# As repetições representam pontes paralelas
grafo = {
    'A': ['B', 'B', 'C', 'C', 'D'],   # A tem 5 pontes
    'B': ['A', 'A', 'C'],             # B tem 3 pontes
    'C': ['A', 'A', 'B', 'D'],        # C tem 4 pontes
    'D': ['A', 'C']                   # D tem 2 pontes
}

# -------------------------------
# 1. Calcular o grau de cada vértice
print("Graus dos vértices:")
graus = {}
for vertice, vizinhos in grafo.items():
    grau = len(vizinhos)
    graus[vertice] = grau
    print(f"Vértice {vertice} tem grau {grau}")

# -------------------------------
# 2. Verificar condição de Euler
# Passeio existe se zero ou dois vértices têm grau ímpar
impares = [v for v, g in graus.items() if g % 2 == 1]
print("\nVértices com grau ímpar:", impares)

if len(impares) == 0 or len(impares) == 2:
    print("Existe um passeio que atravessa cada ponte exatamente uma vez.")
else:
    print("Não existe tal passeio (Euler provou isso).")

# -------------------------------
# 3. DFS (Busca em Profundidade)
def dfs(grafo, inicio, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    print(inicio, end=" ")

    for vizinho in grafo[inicio]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)

print("\n\nDFS a partir de A (com controle de visitados):")
dfs(grafo, 'A')

# -------------------------------
# 4. DFS sem controle de visitados (para ver o problema)
def dfs_sem_visitados(grafo, inicio):
    print(inicio, end=" ")
    for vizinho in grafo[inicio]:
        dfs_sem_visitados(grafo, vizinho)

print("\n\nDFS a partir de A (sem controle de visitados):")
# Atenção: isso vai entrar em loop infinito!
# dfs_sem_visitados(grafo, 'A')