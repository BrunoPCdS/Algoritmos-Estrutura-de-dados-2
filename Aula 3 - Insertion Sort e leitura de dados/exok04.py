

def insertion_sort(numeros):
    for indice_atual in range(1, len(numeros)):
        valor_a_inserir = numeros[indice_atual]
        indice_anterior = indice_atual -1

        while indice_anterior >= 0 and numeros[indice_anterior] > valor_a_inserir:
            numeros[indice_anterior + 1] = numeros[indice_anterior]
            indice_anterior -= 1

        numeros[indice_anterior + 1] = valor_a_inserir

    return numeros

import csv

def ler_csv(arquivo, limite=None):
    numeros = []
    with open(arquivo, newline='') as f:
        leitor = csv.reader(f)
        next(leitor)  # Ignora o cabeçalho
        for i, linha in enumerate(leitor):
            if limite and i >= limite:
                break
            numeros.append(int(linha[0]))
    return numeros

dados = ler_csv("numeros_1M_embaralhado.csv", limite=10000) #retirar numer , limite=x para ler total
print("Ordenando...") #comando de load

ordenados = insertion_sort(dados)
print("Números ordenados:", ordenados)