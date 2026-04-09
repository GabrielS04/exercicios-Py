lista_compras = []
while True:
    print("\nMenu:")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print('3 - Exibir lista')
    print("4 - Sair")
    opcao = input("Escolha uma opção (1/2/3/4): ")
    
    if opcao == "1":
        item = input("Nome do item: ")
        lista_compras.append(item)
        print(f"{item} adicionado com sucesso!")
    elif opcao == "2":
        item = input("Nome do item para remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print(f"{item} removido com sucesso!")
        else:
            print(f"{item} não encontrado na lista.")
    elif opcao == "3":
        if lista_compras:
            print("Lista de Compras:")
            for i, item in enumerate(lista_compras, start=1):
                print(f"{i}. {item}")
        else:
            print("A lista de compras está vazia.")
    elif opcao == "4":
        print("Fechando o programa!")
        break           