
def inverter_palavra():
    palavra = input("Digite uma palavra: ")

    pilha = []

   
    for letra in palavra:
        pilha.append(letra)

    palavra_invertida = ""

    
    while len(pilha) > 0:
        palavra_invertida += pilha.pop()

    print("Palavra invertida:", palavra_invertida)


inverter_palavra()