

condicoes = [
    "possui email",
    "possui telefone",
    "possui endereco",
    "possui cpf",
    "possui cartão de crédito", 
    "possui limite de crédito",
    "é um cliente premium",
    "cadastro completo",
]

casos = []

n = len(condicoes)

for numero in range(2 ** n): 
    caso ={}

    for i, condicao in enumerate(condicoes):
        caso[condicao] = bool(numero & (1 << i))

    casos.append(caso)

print("Total de casos gerados:", len(casos))

print("\nExibindo os primeiros 5 casos gerados:\n")


for caso in casos[:5]:  
    print(caso)