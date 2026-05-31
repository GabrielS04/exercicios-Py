def validar_cpf(cpf: str) -> bool:
    
    

    #a funcao aceita cpf com ou sem pontuação.
    #Exemplo:
    #- "12345678909"
    #- "123.456.789-09"
    

    # Remove tudo que não for número
    cpf = ''.join(numero for numero in cpf if numero.isdigit())

    # CPF precisa ter exatamente 11 dígitos
    if len(cpf) != 11:
        return False

    # CPFs com todos os números iguais são inválidos
    # Exemplo: 111.111.111-11
    if cpf == cpf[0] * 11:
        return False


    # Se passou por todas as verificações, o CPF é válido
    return True


# Testes simples
cpf_digitado = input("Digite um CPF: ")

if validar_cpf(cpf_digitado):
    print("CPF válido.")
else:
    print("CPF inválido.")