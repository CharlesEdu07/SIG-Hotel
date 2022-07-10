import os

hospede = {
     "1": {
        "nome": "João",
        "cpf": "1",
        "email": "dasdasd",
        "endereco": "asdasd",
        "telefone": "asdasd"
    },
    "2": {
        "nome": "Maria",
        "cpf": "2",
        "email": "dasdasd",
        "endereco": "asdasd",
        "telefone": "asdasd"
    }
}

def menu_hospede():
    os.system('cls')

    print("------------------------------")
    print("---------  Hóspedes  ---------")
    print("------------------------------")
    print('1 - Cadastrar hóspedes')
    print('2 - Atualizar hóspedes')
    print("3 - Consultar hóspedes")
    print("4 - Pesquisar hóspedes")
    print("5 - Deletar hóspedes")
    print("0 - Voltar")

    op = input("\nDigite a opção: ")

    return op

def hosp_create(data):
    if data["cpf"] not in hospede:
        hospede[data['cpf']] = {'nome': data['nome'], 'cpf': data['cpf'], 'email': data['email'], 'endereco': data['endereco'], 'telefone': data['telefone']}

        print('\nHóspede cadastrado com sucesso')
    else:
        print('\nHóspede já cadastrado')

def hosp_update(cpf):    
    if cpf in hospede:
        email = input("\nDigite o email: ")
        endereco = input("Digite o endereco: ")
        telefone = input("Digite o telefone: ")
        
        hospede[cpf]['email'] = email
        hospede[cpf]['endereco'] = endereco
        hospede[cpf]['telefone'] = telefone 
            
        print('\nHóspede atualizado com sucesso')

    else:
        print('\nHóspede não encontrado')

def hosp_read():
    print()
    print("---------------------------------------")
    print("-------- Relatório de Hóspedes --------")
    print("---------------------------------------")
    
    for key, value in hospede.items():
        print("\nNome: ", value['nome'],
            "\nCPF: ", value['cpf'],
            "\nTelefone: ", value['telefone'],
            "\nEmail: ", value['email'],
            "\nEndereço: ", value['endereco'])

def hosp_search():
    cpf = input('\nDigite o CPF do Hóspede (Se não souber, tecle ENTER): ')
    name = input('Digite o nome do Hóspede: ')

    for key, value in hospede.items():
        if key == cpf or value['nome'] == name:
            print("Nome: ", value['nome'], "\tCPF: ", value['cpf'], "\tTelefone: ", value['telefone'], "\tEmail: ", value['email'], "\tEndereço: ", value['endereco'])
            return

    print('\nHóspede não encontrado')

def hosp_delete(cpf):
    if cpf in hospede:
        del hospede[cpf]

        print('\nHóspede deletado com sucesso')

    else:
        print('\nHóspede não encontrado')

def modulo_hospede():
    op = menu_hospede()

    while op != '0':
        if op == '1':
            nome = input("Digite o nome do hospede: ")
            cpf = input("Digite o CPF do hospede: ")
            email = input("Digite o email do hospede: ")
            endereco = input("Digite o endereco do hospede: ")
            telefone = input("Digite o telefone do hospede: ")

            data = {
                "nome": nome,
                "cpf": cpf,
                "email": email,
                "endereco": endereco,
                "telefone": telefone
            }
            
            hosp_create(data)

        elif op == '2':
            cpf = input("\nDigite o CPF do hospede: ")
            hosp_update(cpf)

        elif op == '3':
            hosp_read()

        elif op == '4':
            hosp_search()
            
        elif op == '5':
            cpf = input('\nDigite o CPF do hospede: ')
            hosp_delete(cpf)

        else:
            print('\nSeleção inválida') 

        print()
        input('Tecle ENTER para continuar')

        op = menu_hospede()