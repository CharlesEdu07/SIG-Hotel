def validaCPF(cpf):
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0

    if tam != 11:
        return False

    for i in range(11):
        if (cpf[i] < '0') or (cpf[i] > '9'):
            return False

    for i in range(9):
        soma += (int(cpf[i]) * (10 - i))

    d1 = 11 - (soma % 11)

    if (d1 == 10 or d1 == 11):
        d1 = 0

    if d1 != int(cpf[9]):
        return False

    soma = 0

    for i in range(10):
        soma += (int(cpf[i]) * (11 - i))

    d2 = 11 - (soma % 11)

    if (d2 == 10 or d2 == 11):
        d2 = 0

    if d2 != int(cpf[10]):
        return False

    return True

def valida_salario(valor):
    if not valor.isdigit():
        return False

    if valor < '0':
        return False

    if valor == "":
        return False

    return True

def valida_telefone(telefone):
    if not telefone.isdigit():
        return False

    if len(telefone) != 11:
        return False

    return True

def valida_nome(nome):
    if not nome.isalpha():
        return False

    if nome == "":
        return False

    return True

def valida_email(email):
    if email == "":
        return False

    if "@" not in email and "." not in email:
        return False

    return True