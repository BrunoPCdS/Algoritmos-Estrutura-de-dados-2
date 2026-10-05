def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

import csv

def ler_csv(arquivo, limite=None):  # agora aceita 'limite'
    numeros = []
    with open(arquivo, newline='') as f:
        leitor = csv.reader(f)
        # Se o arquivo tiver cabeçalho, descomente a linha abaixo
        next(leitor)
        for i, linha in enumerate(leitor):
            if limite and i >= limite:  # para ler só uma parte
                break
            numeros.append(int(linha[0]))
    return numeros

# Exemplo de uso
dados = ler_csv("numeros_1M_embaralhado.csv")  # lê só 1000 números
print("Ordenando...")
ordenados = insertion_sort(dados)
print("Primeiros 50 números ordenados:", ordenados[:50])
