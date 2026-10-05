def remover_negativos():

    numero = [1, -2, 3, -4, 5]

    nova_lista = []

    for numero in numero:
        if numero >= 0:
            nova_lista.append(numero)

    print("Lista original:", numero)
    print("Nova lista (sem números negativos):", nova_lista)



remover_negativos()