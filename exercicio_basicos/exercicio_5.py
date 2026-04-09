#coletar dados
num1 = float(input("Digite a primeira nota: "))
num2 = float(input("Digite a segunda nota: "))
num3 = float(input("Digite a terceira nota: "))

#calcular a media
media = (num1 + num2 + num3) / 3
print(f'A media das notas é: {media:.2f}')

#verificar se foi aprovado ou nao
if media >=7:
    print('O aluno foi aprovado!')   
else:
    print('O aluno foi reprovado.')