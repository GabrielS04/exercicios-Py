import pandas as pd


try:
    # Ler o arquivo CSV
    df = pd.read_csv("dados_clientes.csv")

    print("\n--- Análise de Dados de Clientes ---")
    print("\nDataFrame Original:")
    print(df)

    # Verificar se as colunas necessárias existem
    colunas_necessarias = ["Idade", "Renda", "Cidade"]

    for coluna in colunas_necessarias:
        if coluna not in df.columns:
            raise KeyError(coluna)

    # Calcular a média de idade e renda
    media_idade = df["Idade"].mean()
    media_renda = df["Renda"].mean()

    print(f"\nMédia de Idade: {media_idade:.2f} anos")
    print(f"Média de Renda: R$ {media_renda:.2f}")

    # Encontrar a cidade com mais clientes
    cidade_mais_clientes = df["Cidade"].value_counts().idxmax()

    print(f"\nCidade com o maior número de clientes: {cidade_mais_clientes}")

    # Filtrar clientes por renda
    renda_minima = float(
        input("\nDigite a renda mínima para filtrar clientes: R$ ")
    )

    clientes_alta_renda = df[df["Renda"] > renda_minima]

    print(f"\nClientes com renda acima de R$ {renda_minima:.2f}:")
    print(clientes_alta_renda)

except FileNotFoundError:
    print("Erro: O arquivo 'dados_clientes.csv' não foi encontrado.")

except KeyError as e:
    print(f"Erro: A coluna '{e.args[0]}' não foi encontrada no arquivo CSV.")

except ValueError:
    print("Erro: Digite um valor numérico válido para a renda.")

except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")