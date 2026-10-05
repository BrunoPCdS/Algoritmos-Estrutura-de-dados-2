# Algoritmos e Estruturas de Dados II
# Atividade em Duplas - Insertion Sort
# Integrantes: Bruno e [Nome do colega]

import csv
import sys

def ler_csv(nome_arquivo):
    """
    Lê um arquivo CSV e retorna uma lista de inteiros.
    Ignora linhas vazias ou valores inválidos.
    """
    dados = []
    with open(nome_arquivo, newline='') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha and linha[0].strip():
                try:
                    dados.append(int(linha[0]))
                except ValueError:
                    continue
    return dados

def remover_duplicados(lista):
    """
    Remove valores duplicados preservando a ordem da primeira ocorrência.
    """
    valores_vistos = set()
    valores_unicos = []

    for valor in lista:
        if valor not in valores_vistos:
            valores_vistos.add(valor)
            valores_unicos.append(valor)

    return valores_unicos

def insertion_sort(lista):
    """
    Ordena a lista usando Insertion Sort.
    """
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista

if __name__ == '__main__':
    arquivo_csv = sys.argv[1] if len(sys.argv) > 1 else 'numeros_1M_embaralhado.csv'

    # 1. Ler somente os 20 primeiros números
    dados = ler_csv(arquivo_csv)[:20]
    print("20 primeiros elementos lidos:", dados)

    # 2. Remover duplicados
    dados_sem_repetidos = remover_duplicados(dados)
    print("Total de elementos após remover duplicados:", len(dados_sem_repetidos))

    # 3. Ordenar
    ordenados = insertion_sort(dados_sem_repetidos)

    print("Elementos ordenados sem repetição:", ordenados)
