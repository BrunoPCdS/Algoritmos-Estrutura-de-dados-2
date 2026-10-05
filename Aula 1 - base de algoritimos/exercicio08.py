contatos = {
    "Bruno": "99999-1111",
    "João": "98888-2222",
    "Maria": "97777-3333"
}


def buscar_telefone(nome):
    if nome in contatos:
        print("Telefone:", contatos[nome])
    else:
        print("Contato não encontrado")


def listar_contatos():
    for nome, telefone in contatos.items():
        print(nome, "-", telefone)


buscar_telefone("Maria")

listar_contatos()