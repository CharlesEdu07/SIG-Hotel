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
    hospede[data['cpf']] = {'nome': data['nome'], 'cpf': data['cpf'], 'email': data['email'], 'endereco': data['endereco'], 'telefone': data['telefone']}

def hosp_update(cpf):    
    if cpf in hospede:
        email = input("Digite o email: ")
        endereco = input("Digite o endereco: ")
        telefone = input("Digite o telefone: ")
        
        hospede[cpf]['email'] = email,
        hospede[cpf]['endereco'] = endereco,
        hospede[cpf]['telefone'] = telefone 
            
        print('Hóspede atualizado com sucesso')

    else:
        print('Hóspede não encontrado')

def hosp_read():
    print()
    print("---------------------------------------")
    print("-------- Relatório de Hóspedes --------")
    print("---------------------------------------")
    
    for key, value in hospede.items():
        print("Nome: ", value['nome'], "\tCPF: ", value['cpf'], "\tTelefone: ", value['telefone'], "\tEmail: ", value['email'], "\tEndereço: ", value['endereco'])

def hosp_search():
    cpf = input('Digite o cpf do Hóspede: ')
    name = input('Digite o nome do Hóspede: ')

    for key, value in hospede.items():
        if key == cpf or value['nome'] == name:
            print("Nome: ", value['nome'], "\tCPF: ", value['cpf'], "\tTelefone: ", value['telefone'], "\tEmail: ", value['email'], "\tEndereço: ", value['endereco'])
            return

    print('Hóspede não encontrado')

def hosp_delete(cpf):
    del hospede[cpf]

def modulo_hospede():
    op = menu_hospede()

    while op != '0':
        if op == '1':
            nome = input("Digite o nome do hospede: ")
            cpf = input("Digite o cpf do hospede: ")
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
            cpf = input("Digite o CPF do hospede: ")
            hosp_update(cpf)

        elif op == '3':
            hosp_read()

        elif op == '4':
            hosp_search()
            
        elif op == '5':
            cpf = input('Digite o cpf do hospede: ')
            hosp_delete(cpf)

        else:
            print('\nSeleção inválida') 

        print()
        input('Tecle ENTER para continuar')

        op = menu_hospede()