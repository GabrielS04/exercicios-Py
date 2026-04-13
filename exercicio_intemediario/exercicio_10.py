def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

print("\nConversor de Temperatura:")
print("1. Celsius para Fahrenheit")
print("2. Fahrenheit para Celsius")
print("3. Sair")
opcao = input("Escolha uma opção (1, 2 ou 3): ")

#formula para converter celsius para fahrenheit: F = (C * 9/5) + 32
#formula para converter fahrenheit para celsius: C = (F - 32) * 5/9

if opcao == '1':
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C é igual a {fahrenheit:.2f}°F")
    
elif opcao == '2':
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F é igual a {celsius:.2f}°C")
    
elif opcao == '3':
    print("Saindo do conversor de temperatura...")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")