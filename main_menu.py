import os

def menu_main():
    os.system('cls')
    
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