import datetime

def registrar_log(tipo, mensagem):
    # definir o nome do arquivo de log
    arquivo_log = "log.txt"

    # obtem a data e hora atual
    data_hora_atual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # formata a mensagem do log
    log_formatado = f"[{data_hora_atual}] [{tipo.upper()}] {mensagem}\n"

    # escreve a mensagem no arquivo de log
    with open(arquivo_log, "a") as arquivo:
        arquivo.write(log_formatado)

# registrar uma mensagem informativa
registrar_log("info", "O programa iniciou corretamente.")

# registrar um aviso
registrar_log("warning", "O programa iniciou mas com problemas.")

# registrar um erro
registrar_log("erro", "Falha ao conectar ao banco de dados.")

