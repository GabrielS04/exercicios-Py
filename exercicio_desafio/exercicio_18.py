
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# Dados fictícios de clientes para visualização
# ============================================================

data = {
    "Nome": ["Luana", "Rafael", "Beatriz", "Thiago", "Mariana", "Caio", "Juliana"],
    "Idade": [24, 31, 19, 45, 28, 37, 22],
    "Cidade": [
        "Salvador", "Fortaleza", "Recife", "Salvador",
        "Fortaleza", "Manaus", "Recife"
    ],
    "Renda": [4200.00, 8500.00, 2800.00, 11000.00, 5300.00, 7100.00, 3600.00],
}

df_vis = pd.DataFrame(data)


# ============================================================
# Gráfico de Pizza: Distribuição de clientes por cidade
# ============================================================

# Conta quantos clientes há em cada cidade
contagem_cidades = df_vis["Cidade"].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    contagem_cidades,                  # Valores (quantidades)
    labels=contagem_cidades.index,     # Nomes das fatias (cidades)
    autopct="%1.1f%%",                 # Exibe a porcentagem em cada fatia
    startangle=90,                     # Começa pelo topo (12h)
    colors=["#4C9BE8", "#F4845F", "#6ECB8A"],  # Cores personalizadas
    wedgeprops={"edgecolor": "white", "linewidth": 2},  # Borda branca entre fatias
)

plt.title("Distribuição de Clientes por Cidade", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("clientes_por_cidade.png")  # Salva o gráfico como imagem
plt.show()                              # Exibe o gráfico


# ============================================================
# Histograma: Distribuição de idades
# ============================================================

plt.figure(figsize=(10, 6))

plt.hist(
    df_vis["Idade"],
    bins=5,
    color="lightcoral",
    edgecolor="black"
)

plt.title("Distribuição de Idades dos Clientes")
plt.xlabel("Idade")
plt.ylabel("Frequência")
plt.grid(axis="y", linestyle="--")
plt.tight_layout()
plt.savefig("distribuicao_idades.png")  # Salva o gráfico como imagem
plt.show()                              # Exibe o gráfico


print("Gráficos 'clientes_por_cidade.png' e 'distribuicao_idades.png' gerados.")