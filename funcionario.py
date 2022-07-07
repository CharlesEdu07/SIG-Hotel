import os

funcionario = {
    "1": {
        "nome": "João",
        "cpf": "1",
        "salario": 1000,
        "ocupacao": "Gerente"
    },
    "2": {
        "nome": "Maria",
        "cpf": "2",
        "salario": 2000,
        "ocupacao": "Gerente"
    }
}

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
        print("Nome: ", value['nome'], "\tCpf: ", value['cpf'], "\tSalario: ", value['salario'], "\tOcupacao: ", value['ocupacao'])

def func_search():
    cpf = input('Digite o cpf do Funcionario: ')
    name = input('Digite o nome do Funcionario: ')

    for key, value in funcionario.items():
        if key == cpf or value['nome'] == name:
            print("Nome: ", value['nome'], "\tCpf: ", value['cpf'], "\tSalario: ", value['salario'], "\tOcupacao: ", value['ocupacao'])
            return

    print('Funcionario não encontrado')

def func_update(cpf):
    if cpf in funcionario:
        salario = input("Digite o novo salario do funcionario: ")
        ocupacao = input("Digite a nova ocupação do funcionário: ")
        
        funcionario[cpf]["salario"] = salario
        funcionario[cpf]["ocupacao"] = ocupacao

    else:
        print('Nenhum dado foi alterado')
       
def func_delete(cpf):
    if cpf in funcionario:
        del funcionario[cpf]

        print('Funcionario deletado com sucesso')

    else:
        print('Funcionario não encontrado')

def modulo_funcionario():
    op = menu_funcionario()

    while op != '0':
        if op == '1':
            nome = input("Digite o nome do funcionario: ")
            cpf = input("Digite o cpf do funcionario: ")
            salario = input("Digite o salario do funcionario: ")
            ocupacao = input("Digite a ocupação do funcionário: ")

            data = {
                "nome": nome,
                "cpf": cpf,
                "salario": salario,
                "ocupacao": ocupacao
            }
            
            func_create(data)

        elif op == '2':
            cpf = input("Digite o cpf do funcionario: ")
            #Verificar O Cpf Aqui

            func_update(cpf)

        elif op == '3':
            func_read()

        elif op == '4':
            func_search()
            
        elif op == '5':
            cpf = input('Digite o cpf do Funcionario: ')
            func_delete(cpf)

        else:
            print('\nSeleção inválida') 

        print()
        input('Tecle ENTER para continuar')

        op = menu_funcionario()