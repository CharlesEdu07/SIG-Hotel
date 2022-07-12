import os
from reserva import res_read, reservas
from hospede import hospede

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

def check_in():
    pass

def check_out():
    pass

def modulo_check():
    op = menu_check()

    while op != '0':
        if op == '1':
            res_read()

            '''cpf = input("\nDigite o CPF para fazer check-in: ")

            print(reservas)

            if cpf in reservas:
                check_in(cpf)

            else:
                print("Reserva não encontrada")'''

        elif op == '2':
            check_out()

        else:
            print('\nSeleção inválida')

        print()
        input('Tecle ENTER para continuar')

        op = menu_check()