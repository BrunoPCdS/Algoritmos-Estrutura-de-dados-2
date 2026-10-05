import time
from numba import njit
import numpy as np


# O decorador @njit compila a função para código de máquina nativo
@njit
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Lendo o arquivo CSV com 1 milhão de números
dados = np.loadtxt("numeros_1M_embaralhado.csv", skiprows=1, dtype=np.int64)

print(f"Dados lidos: {dados.size}")
print("Ordenando...")
inicio = time.time()
insertion_sort(dados)
fim = time.time()

print(f"Concluído em {fim - inicio:.2f} segundos!")
print("Primeiros 10 números ordenados:", dados[:10])
