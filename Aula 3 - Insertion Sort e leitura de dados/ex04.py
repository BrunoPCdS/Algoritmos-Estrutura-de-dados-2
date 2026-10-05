
# ============================================================
# ALGORITMO DE ORDENAÇÃO - INSERTION SORT
# ============================================================

def insertion_sort(lista):
    # Percorre a lista a partir do segundo elemento.
    # O primeiro elemento é considerado inicialmente ordenado.
    for indice_atual in range(1, len(lista)):

        # Guarda o valor que será colocado na posição correta.
        valor_para_inserir = lista[indice_atual]

        # Começa comparando com o elemento imediatamente anterior.
        indice_anterior = indice_atual - 1

        # Enquanto houver elementos anteriores e o elemento anterior
        # for maior que o valor que queremos inserir:
        while (
            indice_anterior >= 0
            and lista[indice_anterior] > valor_para_inserir
        ):
            # Move o elemento maior uma posição para a direita.
            lista[indice_anterior + 1] = lista[indice_anterior]

            # Volta uma posição para continuar a comparação.
            indice_anterior -= 1

        # Coloca o valor na posição correta.
        lista[indice_anterior + 1] = valor_para_inserir

    # Retorna a lista já ordenada.
    return lista


# ============================================================
# LEITURA DO ARQUIVO CSV
# ============================================================

import csv


def ler_csv(arquivo, limite=None):
    # Lista que armazenará os números encontrados no arquivo.
    numeros = []

    # Abre o arquivo CSV.
    with open(arquivo, newline='') as arquivo_csv:

        # Cria o leitor do arquivo CSV.
        leitor_csv = csv.reader(arquivo_csv)

        # Ignora a primeira linha do arquivo (cabeçalho).
        next(leitor_csv)

        # Percorre todas as linhas do arquivo.
        for indice_linha, linha in enumerate(leitor_csv):

            # Se um limite foi definido e ele foi atingido,
            # interrompe a leitura do arquivo.
            if limite and indice_linha >= limite:
                break

            # Pega o primeiro valor da linha, transforma em inteiro
            # e adiciona à lista de números.
            numeros.append(int(linha[0]))

    # Retorna a lista de números lidos.
    return numeros


# ============================================================
# EXECUÇÃO DO PROGRAMA
# ============================================================

# Lê os números armazenados no arquivo CSV.
# Sem limite, todos os números do arquivo serão lidos.
dados = ler_csv("numeros_1M_embaralhado.csv")

# Informa ao usuário que a ordenação será iniciada.
print("Ordenando...")

# Ordena os números utilizando o Insertion Sort.
ordenados = insertion_sort(dados)

# Mostra os primeiros 50 números depois da ordenação.
print("Primeiros 50 números ordenados:", ordenados[:50])

