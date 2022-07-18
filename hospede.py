import os
import pickle
from verificar import *

hospede = {}

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

def hosp_write_file():  
    arq_hospede = open("hospede.dat", "wb")

    pickle.dump(hospede, arq_hospede)

    arq_hospede.close()
            
def hosp_load_file():
    ld_hospede = {}

    try:
        arq_hospede = open("hospede.dat", "rb")
        ld_hospede = pickle.load(arq_hospede)
        arq_hospede.close()

    except:
        arq_hospede = open("hospede.dat", "wb")
        arq_hospede.close()

    return ld_hospede

def hosp_create(data):
    if data["cpf"] not in hospede:
        hospede[data['cpf']] = {'nome': data['nome'], 'cpf': data['cpf'], 'email': data['email'], 'endereco': data['endereco'], 'telefone': data['telefone']}

        print('\nHóspede cadastrado com sucesso')
    else:
        print('\nHóspede já cadastrado')

def hosp_update(cpf):    
    if cpf in hospede:
        email = input("\nDigite o novo email: ")
        endereco = input("Digite o novo endereco: ")
        telefone = input("Digite o novo telefone: ")

        while not(valida_telefone(telefone)):
            print("\nTelefone inválido. Digite novamente")
            telefone = input("\nDigite o novo telefone: ")
        
        hospede[cpf]['email'] = email
        hospede[cpf]['endereco'] = endereco
        hospede[cpf]['telefone'] = telefone 
            
        print('\nHóspede atualizado com sucesso')

    else:
        print('\nHóspede não encontrado')

def hosp_read():
    os.system('cls')

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
    cpf = input('\nDigite o CPF do hóspede (Se não souber, tecle ENTER): ')
    name = input('Digite o nome do hóspede: ')

    print()

    for key, value in hospede.items():
        if key == cpf or value['nome'] == name.capitalize():
            print("Nome: ", value['nome'], "\tCPF: ", value['cpf'], "\tTelefone: ", value['telefone'], "\tEmail: ", value['email'], "\tEndereço: ", value['endereco'])
            return

    print('\nHóspede não encontrado')

def hosp_delete(cpf):
    if cpf in hospede:
        del hospede[cpf]

        print('\nHóspede deletado com sucesso')

    else:
        print('\nHóspede não encontrado')

def hosp_read_data():
    nome = input("\nDigite o nome do hospede: ")

    while not(valida_nome(nome)):
        print("\nNome inválido. Digite novamente")
        nome = input("\nDigite o nome do hospede: ")

    cpf = input("Digite o CPF do hospede: ")

    while not(validaCPF(cpf)):
        print("\nCPF inválido. Digite novamente")
        cpf = input("\nDigite o CPF do hospede: ")

    email = input("Digite o email do hospede: ")
    endereco = input("Digite o endereco do hospede: ")
    telefone = input("Digite o telefone do hospede: ")

    while not(valida_telefone(telefone)):
        print("\nTelefone inválido. Digite novamente")
        telefone = input("\nDigite o telefone do hospede: ")

    data = {
        "nome": nome.capitalize(),
        "cpf": cpf,
        "email": email,
        "endereco": endereco.capitalize(),
        "telefone": telefone
    }

    hosp_create(data)

def modulo_hospede():
    op = menu_hospede()

    global hospede
    hospede = hosp_load_file()

    while op != '0':
        if op == '1':
            os.system('cls')

            print("\nCADASTRO DE HÓSPEDES")

            hosp_read_data()

        elif op == '2':
            os.system('cls')

            print("\nATUALIZAÇÃO DE HÓSPEDES")

            hosp_read()

            cpf = input("\nDigite o CPF do hospede: ")

            hosp_update(cpf)

        elif op == '3':
            os.system('cls')

            print("\nCarregando relatório...")

            hosp_read()

        elif op == '4':
            os.system('cls')

            print("PESQUISA DE HÓSPEDES")

            hosp_search()
            
        elif op == '5':
            os.system('cls')

            print("\nDELETAR HÓSPEDE")

            hosp_read()

            cpf = input('\nDigite o CPF do hospede: ')
            
            hosp_delete(cpf)

        else:
            print('\nSeleção inválida') 
        
        hosp_write_file()

        print()
        input('Tecle ENTER para continuar')

        
        op = menu_hospede()