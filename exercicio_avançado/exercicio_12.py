import random
#tamanho da senha
tamanho_senha = int(input("Digite o tamanho da senha: "))
#menu de tipos de caracteres
incluir_minusculas = input("Incluir letras minúsculas? (s/n): ").lower() == "s"
incluir_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == "s"
incluir_numeros = input("Incluir números? (s/n): ").lower() == "s"
incluir_simbolos = input("Incluir símbolos? (s/n): ").lower() == "s"

#conjunto de caracteres
caracteres = ""

if incluir_minusculas:
    caracteres += "abcdefghijklmnopqrstuvwxyz"
if incluir_maiusculas:
    caracteres += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
if incluir_numeros:
    caracteres += "0123456789"
if incluir_simbolos:
    caracteres += "!@#$%^&*()"
#gerar senha
senha = "".join(random.choice(caracteres) for _ in range(tamanho_senha))
print("Senha gerada:", senha)
if len(senha) <= 0:
    print("Erro: Tamanho da senha inválido.")