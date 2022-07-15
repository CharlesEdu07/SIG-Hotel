import os
import pickle

funcionario = {}

def menu_funcionario():
    os.system('cls')

    print("---------------------------------")
    print("---------  Funcionário  ---------")
    print("---------------------------------")
    print('1 - Cadastrar funcionário')
    print('2 - Atualizar funcionário')
    print("3 - Listar funcionário")
    print("4 - Pesquisar funcionário")
    print("5 - Deletar funcionário")
    print("0 - Voltar")
        
    op = input("\nDigite a opção: ")

    return op

def func_write_file():  
    '''with open('funcionario.dat', 'wb') as f: 
        pickle.dump(funcionario, f)'''

    arq_funcionario = open("funcionario.dat", "wb")

    pickle.dump(funcionario, arq_funcionario)

    arq_funcionario.close()
            
def func_load_file():
    ld_funcionario = {}

    try:
        '''with open('funcionario.dat', 'rb') as f:
            ld_funcionario = pickle.load(f)'''

        arq_funcionario = open("funcionario.dat", "rb")
        ld_funcionario = pickle.load(arq_funcionario)
        arq_funcionario.close()

    except:
        arq_funcionario = open("funcionario.dat", "wb")
        arq_funcionario.close()

    return ld_funcionario

def func_create(data):
    if data['cpf'] not in funcionario:
        funcionario[data['cpf']] = {'nome': data['nome'], 'cpf': data['cpf'], 'salario': data['salario'], 'ocupacao': data['ocupacao']}

        print('\nFuncionario cadastrado com sucesso')

    else:
        print('\nFuncionario ja existe')

def func_read():
    print()
    print("-------------------------------------------")
    print("-------- Relatório de Funcionarios --------")
    print("-------------------------------------------")
    
    for key, value in funcionario.items():
        print("\nNome: ", value['nome'],
        "\nCPF: ", value['cpf'],
        "\nSalario: ", value['salario'],
        "\nOcupacao: ", value['ocupacao'])

def func_search():
    cpf = input('\nDigite o CPF do funcionario (Se não souber, tecle ENTER): ')
    name = input('Digite o nome do funcionario: ')

    print()

    for key, value in funcionario.items():
        if key == cpf or value['nome'] == name:
            print("Nome: ", value['nome'], "\tCPF: ", value['cpf'], "\tSalario: ", value['salario'], "\tOcupacao: ", value['ocupacao'])
            return

    print('\nFuncionario não encontrado')

def func_update(cpf):
    if cpf in funcionario:
        salario = input("Digite o novo salario do funcionario: ")
        ocupacao = input("Digite a nova ocupação do funcionário: ")
        
        funcionario[cpf]["salario"] = salario
        funcionario[cpf]["ocupacao"] = ocupacao

        print('\nFuncionario atualizado com sucesso')

    else:
        print('\nNenhum dado foi alterado')
       
def func_delete(cpf):
    if cpf in funcionario:
        del funcionario[cpf]

        print('\nFuncionario deletado com sucesso')

    else:
        print('\nFuncionario não encontrado')

def func_read_data():
    nome = input("\nDigite o nome do funcionario: ")
    cpf = input("Digite o CPF do funcionario: ")
    salario = input("Digite o salario do funcionario: ")
    ocupacao = input("Digite a ocupação do funcionário: ")

    data = {
        "nome": nome,
        "cpf": cpf,
        "salario": salario,
        "ocupacao": ocupacao
    }
            
    func_create(data)

def modulo_funcionario():
    op = menu_funcionario()

    global funcionario
    funcionario =  func_load_file()
    
    while op != '0':
        if op == '1':
            print('\nCADASTRAR FUNCIONÁRIO')

            func_read_data()

        elif op == '2':
            print('\nATUALIZAR FUNCIONÁRIO')

            cpf = input("\nDigite o CPF do funcionario: ")

            func_update(cpf)

        elif op == '3':
            print('\nLISTAR FUNCIONÁRIO')

            func_read()

        elif op == '4':
            print('\nPESQUISAR FUNCIONÁRIO')

            func_search()
            
        elif op == '5':
            print('\nDELETAR FUNCIONÁRIO')

            cpf = input('\nDigite o CPF do Funcionario: ')

            func_delete(cpf)

        else:
            print('\nSeleção inválida') 

        func_write_file()
        
        print()
        input('Tecle ENTER para continuar')

        op = menu_funcionario()
