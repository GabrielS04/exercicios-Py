#Ler uma frase do usuário
#Passar por cada letra
#Ver se a letra é vogal
#Somar um contador
#Mostrar o total no final

palavra = str(input("Digite uma palavra: "))
contador = 0
vogais = "aeiouAEIOU"
for letra in palavra:
    if letra in vogais:
        contador += 1
print(f"O total de vogais na palavra '{palavra}' é: {contador}")