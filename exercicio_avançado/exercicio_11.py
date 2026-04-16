# pedir o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo: ")

try:
    with open(nome_arquivo, "r") as arquivo: #ler o arquivo
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError: #erro se nao encontrar
    print("Arquivo não encontrado.")