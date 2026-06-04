
import requests
from bs4 import BeautifulSoup
from datetime import datetime



HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

TIMEOUT = 10             # Segundos antes de desistir da requisição
TAMANHO_MINIMO = 10      # Ignora textos muito curtos (provavelmente não são títulos)


# ============================================================
# Funções
# ============================================================

def buscar_html(url):
    """
    Faz a requisição HTTP e retorna o conteúdo HTML da página.
    Retorna None se ocorrer qualquer erro.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()  # Lança exceção para erros HTTP (4xx, 5xx)
        return response.text

    except requests.exceptions.ConnectionError:
        print(" Erro: Sem conexão com a internet ou site fora do ar.")
    except requests.exceptions.Timeout:
        print(f" Erro: O site não respondeu em {TIMEOUT} segundos.")
    except requests.exceptions.HTTPError as erro:
        print(f" Erro HTTP: {erro}")
    except requests.exceptions.RequestException as erro:
        print(f" Erro inesperado na requisição: {erro}")

    return None


def extrair_titulos(html, tag, classe=None):
    """
    Analisa o HTML e extrai os textos da tag (e classe) informadas.
    Retorna uma lista de strings com os títulos encontrados.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Busca com ou sem classe CSS, dependendo do que foi passado
    elementos = soup.find_all(tag, class_=classe) if classe else soup.find_all(tag)

    titulos = []
    for elemento in elementos:
        texto = elemento.get_text(strip=True)

        # Filtra textos vazios ou muito curtos
        if len(texto) >= TAMANHO_MINIMO:
            titulos.append(texto)

    return titulos


def salvar_titulos(titulos, nome_arquivo, url):
    """
    Salva a lista de títulos em um arquivo .txt com cabeçalho informativo.
    """
    agora = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")

    try:
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:

            # Cabeçalho do arquivo
            arquivo.write("=" * 60 + "\n")
            arquivo.write("  TÍTULOS DE NOTÍCIAS EXTRAÍDOS\n")
            arquivo.write(f"  Data   : {agora}\n")
            arquivo.write(f"  Fonte  : {url}\n")
            arquivo.write(f"  Total  : {len(titulos)} títulos\n")
            arquivo.write("=" * 60 + "\n\n")

            # Títulos numerados
            for numero, titulo in enumerate(titulos, start=1):
                arquivo.write(f"{numero:02d}. {titulo}\n")

        print(f" {len(titulos)} títulos salvos em '{nome_arquivo}'")

    except PermissionError:
        print(f" Erro: Sem permissão para salvar o arquivo '{nome_arquivo}'.")
    except OSError as erro:
        print(f" Erro ao salvar o arquivo: {erro}")


def extrair_titulos_noticias(url, nome_arquivo="noticias.txt", tag="h2", classe=None):
    """
    Função principal: acessa a URL, extrai os títulos e salva no arquivo.

    Parâmetros:
        url         : endereço do site a ser acessado
        nome_arquivo: nome do arquivo de saída (padrão: 'noticias.txt')
        tag         : tag HTML dos títulos (padrão: 'h2')
        classe      : classe CSS da tag (opcional)

    Como descobrir a tag e classe corretas?
        1. Abra o site no navegador
        2. Clique com o botão direito em um título → "Inspecionar"
        3. Veja qual tag e classe CSS estão sendo usadas
    """
    print(f"\n Acessando: {url}")

    html = buscar_html(url)
    if html is None:
        return  # Encerra se não conseguiu acessar o site

    print(" Extraindo títulos...")
    titulos = extrair_titulos(html, tag=tag, classe=classe)

    if not titulos:
        print("  Nenhum título encontrado. Verifique a tag e a classe informadas.")
        return

    salvar_titulos(titulos, nome_arquivo, url)


# ============================================================
# Exemplo de uso
# ============================================================

if __name__ == "__main__":

    # Cuidado ao fazer scraping: verifique os termos de serviço do site.
    # Ajuste a 'tag' e a 'classe' de acordo com o HTML do site escolhido.

    extrair_titulos_noticias(
        url="https://g1.globo.com/",
        nome_arquivo="noticias.txt",
        tag="a",
        classe="feed-post-link",   # Classe dos links de notícias no G1
    )