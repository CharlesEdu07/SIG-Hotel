import os

def func_create():
    pass

def func_search():
    pass

def func_update():
    pass

def func_delete():
    pass

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

    op = int(input("\nDigite a opção: "))

    if op == 1:
        os.system('clear')

        print("------------------------------")
        print("---------  Hóspedes  ---------")
        print("------------------------------")
        print('1 - Cadastrar hóspedes')
        print('2 - Atualizar hóspedes')
        print("3 - Consultar hóspedes")
        print("4 - Deletar hóspedes")
        print("0 - Voltar")

        op = int(input("\nDigite a opção: "))

    elif op == 2:
        os.system('clear')

        print("---------------------------------")
        print("---------  Funcionário  ---------")
        print("---------------------------------")
        print('1 - Cadastrar funcionário')
        print('2 - Atualizar funcionário')
        print("3 - Consultar funcionário")
        print("4 - Deletar funcionário")
        print("0 - Voltar")

        op = int(input("\nDigite a opção: "))

    elif op == 3:
        os.system('clear')

        print("------------------------------")
        print("---------  Reservas  ---------")
        print("------------------------------")
        print('1 - Criar reserva')
        print('2 - Atualizar reserva')
        print("3 - Consultar reserva")
        print("4 - Cancelar reserva")
        print("0 - Voltar")

        op = int(input("\nDigite a opção: "))

    elif op == 4:
        os.system('clear')

        print("1 - Check-in")
        print("2 - Check-out")
        print("0 - Voltar")

        op = int(input("\nDigite a opção: "))