contatos = []
print("\nMenu:")
print("1. Adicionar contato")
print("2. Listar contatos")
print("3. Buscar contatos")
print("4. Sair")

while True:
    opcao = input("Escolha uma opção (1/2/3/4): ")
    
    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        contatos.append({"nome": nome, "telefone": telefone, "email": email})
        print(f"Contato {nome} adicionado com sucesso!")
    
    elif opcao == "2":
        if contatos:
            print("\nLista de Contatos:")
            for contato in contatos:
                print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, email: {contato['email']}")
        else:
            print("Nenhum contato cadastrado.")
    
    elif opcao == "3":
        busca = input("Digite o nome para buscar: ")
        encontrados = [c for c in contatos if busca.lower() in c['nome'].lower()]
        
        if encontrados:
            print("\nContatos Encontrados:")
            for contato in encontrados:
                print(f"Nome: {contato['nome']}, Telefone: {contato['telefone']}, email: {contato['email']}")
        else:
            print("Nenhum contato encontrado com esse nome.")
    
    elif opcao == "4":
        print("Encerrando o programa.")
        break
    
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
