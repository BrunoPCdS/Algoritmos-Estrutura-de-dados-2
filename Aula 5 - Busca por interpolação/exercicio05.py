

valores = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def interpolation (lista):
    low = 0
    high = len(lista) -1

    while low <= high and 70 >= lista[low] and 70 <= lista[high]:
        if lista[low] == lista[high]:
            if lista[low] == 70:
                return low
            break

        position = low + ((70 - lista[low]) * (high - low)) // (lista[high] - lista[low])

        if lista[position] == 70:
            return position
        elif lista[position] < 70:
            low = position +1
        else:
            high = position -1

    return -1

indice = interpolation(valores)

if indice != -1:
    print("Índice encontrado", indice)
else:
    print("Valor não encontrado")