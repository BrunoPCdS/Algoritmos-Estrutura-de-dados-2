def simular_fila():
    fila = []

    while True:
        print("\n--- MENU FILA ---")
        print("1 - Adicionar nome na fila")
        print("2 - Remover nome da fila")
        print("3 - Mostrar fila")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome: ")

            # Adiciona no final da fila
            fila.append(nome)

            print("\nPessoa adicionada!")
            print("Fila atual:", fila)

        elif opcao == "2":
            if len(fila) > 0:
                nome_removido = fila.pop(0)

                print("\nPessoa atendida:", nome_removido)
                print("Fila atual:", fila)
            else:
                print("\nA fila está vazia!")

        elif opcao == "3":
            print("\nFila atual:", fila)

        elif opcao == "4":
            print("\nEncerrando...")
            break

        else:
            print("\nOpção inválida!")


simular_fila()