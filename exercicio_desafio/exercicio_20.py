
import random
import os




DESENHOS_FORCA = [
    # 0 erros
    """
       -----
       |   |
           |
           |
           |
           |
    =========""",

    # 1 erro
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========""",

    # 2 erros
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========""",

    # 3 erros
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========""",

    # 4 erros
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",

    # 5 erros
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",

    # 6 erros - enforcado
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
]

MAXIMO_ERROS = len(DESENHOS_FORCA) - 1  # 6 erros = fim de jogo


# ============================================================
# Banco de palavras por categoria
# ============================================================

BANCO_DE_PALAVRAS = {
    "Animais": [
        "cachorro", "elefante", "borboleta", "jacare", "camaleao",
        "tartaruga", "pinguim", "papagaio", "rinoceronte", "chimpanze",
    ],
    "Frutas": [
        "abacaxi", "morango", "melancia", "maracuja", "goiaba",
        "carambola", "pitanga", "acerola", "graviola", "jabuticaba",
    ],
    "Paises": [
        "brasil", "argentina", "portugal", "mozambique", "japao",
        "australia", "noruega", "tanzania", "colombia", "tailandia",
    ],
    "Esportes": [
        "futebol", "basquete", "natacao", "ginastica", "atletismo",
        "voleibol", "handebol", "canoagem", "esgrima", "triatlo",
    ],
    "Profissoes": [
        "engenheiro", "arquiteto", "bombeiro", "veterinario", "fotografo",
        "jornalista", "astronauta", "musico", "nutricionista", "piloto",
    ],
}


# ============================================================
# Classe Palavra
# ============================================================

class Palavra:
    """
    Representa a palavra secreta do jogo.
    Cuida de revelar letras e verificar se a palavra foi descoberta.
    """

    def __init__(self, texto, categoria):
        # A palavra é guardada em minúsculas para facilitar comparações
        self.texto = texto.lower()
        self.categoria = categoria

        # Conjunto com todas as letras únicas da palavra
        self.letras_da_palavra = set(self.texto)

        # Conjunto das letras que o jogador já acertou
        self.letras_descobertas = set()

    def tentar_letra(self, letra):
        """
        Verifica se a letra está na palavra.
        Retorna True se acertou, False se errou.
        """
        letra = letra.lower()

        if letra in self.texto:
            self.letras_descobertas.add(letra)
            return True

        return False

    def get_estado_atual(self):
        """
        Retorna a palavra com as letras descobertas visíveis
        e o restante como underline ( _ ).
        Exemplo: "b _ r _ _ l e t _"
        """
        estado = []
        for letra in self.texto:
            if letra in self.letras_descobertas:
                estado.append(letra.upper())
            else:
                estado.append("_")

        # Junta as letras com espaço entre elas para ficar legível
        return " ".join(estado)

    def foi_descoberta(self):
        """Retorna True se todas as letras já foram encontradas."""
        return self.letras_da_palavra == self.letras_descobertas

    def __len__(self):
        """Retorna o tamanho da palavra (útil para dicas)."""
        return len(self.texto)


# ============================================================
# Classe Jogador
# ============================================================

class Jogador:
    """
    Representa o jogador, guardando seu nome,
    pontuação e histórico de letras tentadas.
    """

    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0
        self.letras_tentadas = []  # Lista com todas as letras já tentadas

    def registrar_tentativa(self, letra):
        """Guarda a letra tentada no histórico."""
        self.letras_tentadas.append(letra.lower())

    def ja_tentou(self, letra):
        """Verifica se a letra já foi tentada antes."""
        return letra.lower() in self.letras_tentadas

    def get_letras_tentadas(self):
        """Retorna as letras tentadas organizadas em ordem alfabética."""
        return sorted(self.letras_tentadas)

    def adicionar_pontos(self, pontos):
        """Adiciona pontos ao placar do jogador."""
        self.pontuacao += pontos

    def resetar_tentativas(self):
        """Limpa o histórico de tentativas para uma nova rodada."""
        self.letras_tentadas = []

    def __str__(self):
        return f"{self.nome} | Pontuação: {self.pontuacao} pontos"


# ============================================================
# Classe Jogo
# ============================================================

class Jogo:
    """
    Controla toda a lógica do jogo da forca:
    - Escolhe a palavra
    - Processa as tentativas do jogador
    - Controla o número de erros
    - Decide quando o jogo acabou
    """

    def __init__(self, jogador):
        self.jogador = jogador
        self.palavra = None
        self.erros = 0
        self.rodada = 0

    def _escolher_palavra(self):
        """
        Escolhe uma categoria e palavra aleatória do banco.
        O underline é necessário pois é método interno da classe.
        """
        categoria = random.choice(list(BANCO_DE_PALAVRAS.keys()))
        texto = random.choice(BANCO_DE_PALAVRAS[categoria])
        return Palavra(texto, categoria)

    def iniciar_rodada(self):
        """Prepara tudo para uma nova rodada."""
        self.palavra = self._escolher_palavra()
        self.erros = 0
        self.rodada += 1
        self.jogador.resetar_tentativas()

    def _calcular_pontos(self):
        """
        Calcula os pontos ganhos com base nos erros cometidos.
        Menos erros = mais pontos!
        """
        pontos_por_erro = {
            0: 100,
            1: 80,
            2: 60,
            3: 40,
            4: 20,
            5: 10,
            6: 0,
        }
        return pontos_por_erro.get(self.erros, 0)

    def processar_tentativa(self, letra):
        """
        Recebe uma letra do jogador e processa a jogada.
        Retorna uma string com o resultado da tentativa.
        """
        # Verifica se a letra já foi tentada
        if self.jogador.ja_tentou(letra):
            return "repetida"

        # Registra a tentativa no histórico do jogador
        self.jogador.registrar_tentativa(letra)

        # Tenta a letra na palavra
        acertou = self.palavra.tentar_letra(letra)

        if acertou:
            return "acerto"
        else:
            self.erros += 1
            return "erro"

    def esta_em_andamento(self):
        """Retorna True enquanto o jogo não terminou."""
        return not self.palavra.foi_descoberta() and self.erros < MAXIMO_ERROS

    def jogador_venceu(self):
        """Retorna True se o jogador descobriu a palavra."""
        return self.palavra.foi_descoberta()


# ============================================================
# Funções de exibição (interface no terminal)
# ============================================================

def limpar_tela():
    """Limpa o terminal para uma exibição mais organizada."""
    os.system("cls" if os.name == "nt" else "clear")


def exibir_cabecalho(jogador, rodada):
    """Exibe o cabeçalho com nome do jogador e pontuação."""
    print("=" * 50)
    print("            JOGO DA FORCA  ")
    print("=" * 50)
    print(f"  Jogador : {jogador.nome}")
    print(f"  Pontos  : {jogador.pontuacao}")
    print(f"  Rodada  : {rodada}")
    print("=" * 50)


def exibir_estado_jogo(jogo):
    """Exibe o desenho da forca, a palavra e as letras tentadas."""
    # Forca
    print(DESENHOS_FORCA[jogo.erros])
    print()

    # Categoria como dica
    print(f"  Categoria : {jogo.palavra.categoria}")
    print(f"  Tamanho   : {len(jogo.palavra)} letras")
    print()

    # Estado da palavra
    print(f"  Palavra   : {jogo.palavra.get_estado_atual()}")
    print()

    # Letras já tentadas
    letras = jogo.jogador.get_letras_tentadas()
    if letras:
        print(f"  Tentadas  : {' '.join(letras).upper()}")
    else:
        print("  Tentadas  : (nenhuma ainda)")

    # Contador de erros
    print(f"  Erros     : {jogo.erros} / {MAXIMO_ERROS}")
    print()


def pedir_letra(jogador):
    """Pede uma letra ao jogador e valida a entrada."""
    while True:
        entrada = input("  Digite uma letra: ").strip().lower()

        # Verifica se digitou exatamente uma letra
        if len(entrada) == 1 and entrada.isalpha():
            return entrada
        else:
            print("    Por favor, digite apenas UMA letra!")


def exibir_resultado_tentativa(resultado, letra, palavra_revelada=None):
    """Exibe uma mensagem após cada tentativa."""
    print()
    if resultado == "acerto":
        print(f"    A letra '{letra.upper()}' está na palavra!")
    elif resultado == "erro":
        print(f"    A letra '{letra.upper()}' não está na palavra!")
    elif resultado == "repetida":
        print(f"     Você já tentou a letra '{letra.upper()}'!")

    if palavra_revelada:
        print(f"\n    Parabéns! A palavra era: {palavra_revelada.upper()}")

    input("\n  Pressione ENTER para continuar...")


def exibir_fim_de_rodada(jogo):
    """Exibe o resultado no fim de cada rodada."""
    limpar_tela()
    exibir_cabecalho(jogo.jogador, jogo.rodada)
    print(DESENHOS_FORCA[jogo.erros])
    print()

    if jogo.jogador_venceu():
        pontos = jogo._calcular_pontos()
        jogo.jogador.adicionar_pontos(pontos)
        print(f"    VOCÊ VENCEU! +{pontos} pontos")
        print(f"  A palavra era: {jogo.palavra.texto.upper()}")
    else:
        print("    VOCÊ PERDEU! A forca está completa.")
        print(f"  A palavra era: {jogo.palavra.texto.upper()}")

    print()


def perguntar_nova_rodada():
    """Pergunta se o jogador quer jogar de novo."""
    while True:
        resposta = input("  Jogar novamente? (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("   Digite 's' para sim ou 'n' para não.")


# ============================================================
# Loop principal do jogo
# ============================================================

def jogar(jogo):
    """Controla o loop de uma rodada completa."""
    jogo.iniciar_rodada()

    while jogo.esta_em_andamento():
        limpar_tela()
        exibir_cabecalho(jogo.jogador, jogo.rodada)
        exibir_estado_jogo(jogo)

        letra = pedir_letra(jogo.jogador)
        resultado = jogo.processar_tentativa(letra)

        # Só exibe mensagem extra se acertou ou repetiu
        # (erro já vai aparecer na próxima tela pelo desenho atualizado)
        if resultado in ("acerto", "repetida"):
            exibir_resultado_tentativa(resultado, letra)
        elif resultado == "erro":
            exibir_resultado_tentativa(resultado, letra)

    # Fim da rodada
    exibir_fim_de_rodada(jogo)


# ============================================================
# Ponto de entrada do programa
# ============================================================

if __name__ == "__main__":

    limpar_tela()

    print("=" * 50)
    print("     BEM-VINDO AO JOGO DA FORCA! ")
    print("=" * 50)
    print()

    # Pede o nome do jogador
    while True:
        nome = input("  Qual é o seu nome? ").strip()
        if nome:
            break
        print("  Por favor, digite seu nome!")

    # Cria o jogador e o jogo
    jogador = Jogador(nome)
    jogo = Jogo(jogador)

    print(f"\n  Olá, {jogador.nome}! Boa sorte! ")
    input("  Pressione ENTER para começar...")

    # Loop de partidas
    continuar = True
    while continuar:
        jogar(jogo)
        continuar = perguntar_nova_rodada()

    # Mensagem de despedida com placar final
    limpar_tela()
    print("=" * 50)
    print("=" * 50)
    print(f"\n  Jogador : {jogador.nome}")
    print(f"  Rodadas : {jogo.rodada}")
    print(f"  Pontos  : {jogador.pontuacao}")
    print()
    print("=" * 50)