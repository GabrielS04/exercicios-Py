import csv


def analisar_vendas(nome_arquivo: str) -> None:
    

    total_vendas = 0
    produtos_vendidos = {}

    try:
        # Abre o arquivo CSV usando encoding UTF-8
        with open(nome_arquivo, mode="r", encoding="utf-8", newline="") as arquivo:
            leitor = csv.DictReader(arquivo)

            # Le cada linha do arquivo CSV
            for linha in leitor:
                produto = linha["produto"]

                # Converte quantidade para inteiro
                quantidade = int(linha["quantidade"])

                # Converte preço para número decimal
                preco = float(linha["preco"])

                # Calcula o total vendido nesta linha
                total_linha = quantidade * preco

                # Soma ao total geral de vendas
                total_vendas += total_linha

                # Soma a quantidade vendida do produto
                if produto in produtos_vendidos:
                    produtos_vendidos[produto] += quantidade
                else:
                    produtos_vendidos[produto] = quantidade

        # Verifica se o arquivo tinha produtos
        if not produtos_vendidos:
            print("Nenhuma venda encontrada.")
            return

        # Encontra o produto com maior quantidade vendida
        produto_mais_vendido = max(produtos_vendidos, key=produtos_vendidos.get)

        # Mostra os resultados
        print(f"Total de vendas: R$ {total_vendas:.2f}")
        print(f"Produto mais vendido: {produto_mais_vendido}")
        print(f"Quantidade vendida: {produtos_vendidos[produto_mais_vendido]}")

    except FileNotFoundError:
        print("Erro: arquivo CSV não encontrado.")

    except ValueError:
        print("Erro: quantidade ou preço com formato inválido.")

    except KeyError:
        print("Erro: o CSV precisa ter as colunas produto, quantidade e preco.")


# Executa a análise
analisar_vendas("vendas.csv")