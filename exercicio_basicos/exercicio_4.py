#coletar dado do usuario
num = int(input("Digite um número inteiro: "))

#tabuada do numero ate 10
print(f"Tabuada do {num}:")
for i in range(1, 11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")