import os
from datetime import date

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
''' 
reservas = {
    "apt":{
        "classe":"standard",
        "ocupado":False,
        "data_entrada":date.today(),
        "data_saida":date.today(),
        "hospede": hospede['cpf']
        tentar dizer qual hospede está no quarto


    }
}
'''

#func ={ 
    #cpf:{
        #"nome": nome,
        #"cpf": cpf,
        #"salario": salario,
    #}
#}



def menu_main():
    print("--------------------------------------------")
    print("---------  Sistema do Hotel Feliz  ---------")
    print("--------------------------------------------")
    print('1 - Hóspede')
    print('2 - Funcionario')
    print('3 - Reservas')
    print("4 - Check-in e Check-out")
    print("0 - Sair")

    op = input("\nDigite a opção: ")

    return op

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

def menu_reserva():
    os.system('cls')

    print("------------------------------")
    print("---------  Reservas  ---------")
    print("------------------------------")
    print('1 - Criar reserva')
    print('2 - Atualizar reserva')
    print("3 - Consultar reserva")
    print("4 - Cancelar reserva")
    print("0 - Voltar")

    op = input("\nDigite a opção: ")

    return op

def menu_check():
    os.system('cls')

    print("------------------------------------------")
    print("---------  Check-in e Check-Out  ---------")
    print("------------------------------------------")
    print("1 - Check-in")
    print("2 - Check-out")
    print("0 - Voltar")

    op = input("\nDigite a opção: ")

    return op

def hosp_create(data):
    hospede[data['cpf']] = {'nome': data['nome'], 'cpf': data['cpf'], 'email': data['email'], 'endereco': data['endereco'], 'telefone': data['telefone']}

def hosp_update(cpf):
    cpf = input("Digite o cpf do hospede: ")
    
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

def func_create(data):
    funcionario[data['cpf']] = {'nome': data['nome'], 'cpf': data['cpf'], 'salario': data['salario'], 'ocupacao': data['ocupacao']}

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

op = menu_main()

while op != '0':
    if op == '1':
        modulo_hospede()

    elif op == '2':
        modulo_funcionario()

    elif op == '3':
        #modulo_reserva()
        print("a")

    elif op == '4':
        #modulo_check()
        print("a")

    else:
        print('\nSeleção inválida') 

    print()
    input('Tecle ENTER para continuar')

    op = menu_main()