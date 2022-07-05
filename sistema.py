import os
from datetime import date

funcionario = {}

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
    print("4 - Deletar hóspedes")
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
    print("3 - Consultar funcionário")
    print("4 - Deletar funcionário")
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

def func_create(cpf, nome, salario, ocupacao):
    funcionario[cpf] = {'nome': nome, 'cpf': cpf, 'salario': salario, 'ocupacao': ocupacao}

def func_search():
    pass

def func_update():
    pass

def func_delete(cpf):
    del funcionario[cpf]

def modulo_funcionario():
    op = menu_funcionario()

    while op != '0':
        if op == '1':
            nome = input("Digite o nome do funcionario: ")
            cpf = input("Digite o cpf do funcionario: ")
            #Verificar O Cpf Aqui
            salario = input("Digite o salario do funcionario: ")
            ocupacao = input("Digite a ocupação do funcionário: ")
            
            func_create(cpf, nome, salario, ocupacao)

        elif op == '2':
            func_update()

        elif op == '3':
            print(funcionario)
            #func_search()
            
        elif op == '4':
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
        #modulo_hospede()
        print("a")

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