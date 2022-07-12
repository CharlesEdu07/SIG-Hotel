from genericpath import exists
import os
from reserva import res_read, reservas
from hospede import hospede
from datetime import datetime

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

def check_in(apt):
    if reservas[apt]['is_ocupado'] == "":
        data_entrada = datetime.now()
        data_entrada = data_entrada.strftime("%d/%m/%Y")
        
        reservas[apt].update({'data_entrada': data_entrada})
        reservas[apt]['is_ocupado'] = True

        print("\nCheck-in feito com sucesso. O quarto está agora ocupado")

    else :
        print("\nQuarto ocupado")

def check_out(apt):
    if  reservas[apt]['is_ocupado'] == True:
        data_saida = datetime.now()
        data_saida = data_saida.strftime("%d/%m/%Y")

        reservas[apt].update({'data_saida': data_saida})
        reservas[apt]['is_ocupado'] = False

        d1_aux = (reservas[apt]['data_saida'])
        d2_aux = (reservas[apt]['data_entrada'])

        d1 = datetime.strptime(d1_aux, "%d/%m/%Y")
        d2 = datetime.strptime(d2_aux, "%d/%m/%Y")

        delta = d1 - d2

        aux = (reservas[apt]['valor'] * delta.days)

        if aux > 0:
            print("\nValor da hospedagem: R$", aux)

        else:
            print("\nValor da hospedagem: R$", reservas[apt]['valor']) 
        
        res = input('\nDeseja realmente finalizar a reserva? (S/N): ')

        if(res.upper() == 'S'):
            del reservas[apt]
            print('\nReserva Finalizada')

        else:
            print('\nReserva não finalizada')
           
    else:
        print("\nQuarto não ocupado")

def modulo_check():
    op = menu_check()

    while op != '0':
        if op == '1':
            res_read()

            cpf = input("\nDigite o CPF: ")
            apt = input("Digite o número do quarto: ")
            
            if apt in reservas:
                if cpf in reservas[apt]['cpf']:
                    check_in(apt)

                else:
                    print('\nCPF não vinculado ao quarto')
                    
            else:
                print("\nReserva não encontrada")

        elif op == '2':
            cpf = input("\nDigite o CPF: ")
            apt = input("Digite o número do quarto: ")

            if apt in reservas:
                if cpf in reservas[apt]['cpf']:
                    check_out(apt)

                else:
                    print('CPF não cadastrado')

        else:
            print('\nSeleção inválida')

        print()
        input('Tecle ENTER para continuar')

        op = menu_check()