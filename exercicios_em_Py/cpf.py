def valida_cpf(cpf):
    # Removendo caracteres não-numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificando se o CPF possui 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificando se todos os dígitos são iguais
    if len(set(cpf)) == 1:
        return False

    # Calculando o primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    digito1 = 11 - (soma % 11)
    if digito1 > 9:
        digito1 = 0

    # Calculando o segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    digito2 = 11 - (soma % 11)
    if digito2 > 9:
        digito2 = 0

    # Verificando se os dígitos verificadores são válidos
    if int(cpf[-2]) != digito1 or int(cpf[-1]) != digito2:
        return False

    # CPF válido
    return True


cpf = str(input("Digite seu cpf: "))
if valida_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
