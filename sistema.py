import os
from datetime import date

funcionario = {}

def func_create(cpf, nome, salario, ocupacao):
    funcionario[cpf] = {'nome': nome, 'cpf': cpf, 'salario': salario, 'ocupacao': ocupacao}

def func_search():
    pass

def func_update():
    pass

def func_delete(cpf):
    del funcionario[cpf]

def func_read():
    pass

while True:

    print("--------------------------------------------")
    print("---------  Sistema do Hotel Feliz  ---------")
    print("--------------------------------------------")
    print('1 - Hóspede')
    print('2 - Funcionario')
    print('3 - Reservas')
    print("4 - Check-in e Check-out")
    print("0 - Sair")

    op = int(input("Digite: "))

    if op == 1:
        os.system('cls')

        print("------------------------------")
        print("---------  Hóspedes  ---------")
        print("------------------------------")
        print('1 - Cadastrar hóspedes')
        print('2 - Atualizar hóspedes')
        print("3 - Consultar hóspedes")
        print("4 - Deletar hóspedes")
        print("0 - Voltar")

        op = int(input("Digite: "))

    elif op == 2:
        os.system('cls')

        print("---------------------------------")
        print("---------  Funcionário  ---------")
        print("---------------------------------")
        print('1 - Cadastrar funcionário')
        print('2 - Atualizar funcionário')
        print("3 - Consultar funcionário")
        print("4 - Deletar funcionário")
        print("0 - Voltar")
        
        op = int(input("\nDigite a opção: "))
        
        if op == 1:
            nome = input("Digite o nome do funcionario: ")
            cpf = input("Digite o cpf do funcionario: ")
            #Verificar O Cpf Aqui
            salario = input("Digite o salario do funcionario: ")
            ocupacao = input("Digite a ocupação do funcionário: ")
            
            func_create(cpf, nome, salario, ocupacao)

        elif op == 2:
            func_update()

        elif op == 3:
            print(funcionario)
            #func_search()
            
        elif op == 4:
            cpf = input('Digite o cpf do Funcionario: ')
            func_delete(cpf)

    elif op == 3:
        os.system('cls')

        print("------------------------------")
        print("---------  Reservas  ---------")
        print("------------------------------")
        print('1 - Criar reserva')
        print('2 - Atualizar reserva')
        print("3 - Consultar reserva")
        print("4 - Cancelar reserva")
        print("0 - Voltar")

    elif op == 4:
        os.system('cls')

        print("1 - Check-in")
        print("2 - Check-out")
        print("0 - Voltar")