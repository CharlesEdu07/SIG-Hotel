import os
from datetime import date

from hospede import hospede

a = hospede['1']['nome']

quartos = {
    "101": 80,
    "102": 80,
    "103": 80,
    "104": 80,
    "105": 100,
    "106": 150,
    "107": 200,
    "108": 250
}

reservas = {
  
}

def menu_reserva():
    os.system('cls')

    print("------------------------------")
    print("---------  Reservas  ---------")
    print("------------------------------")
    print('1 - Criar reserva')
    print('2 - Atualizar reserva')
    print("3 - Consultar reserva")
    print("4 - Pesquisar reserva")
    print("5 - Deletar reserva")
    print("0 - Voltar")

    op = input("\nDigite a opção: ")

    return op

def res_create(data):
    if data['apt'] not in reservas:
        reservas[data['apt']] = {'apt': data['apt'], 'is_ocupado': data['is_ocupado'], 'is_reservado': data['is_reservado'], 'nome': data['nome'], 'valor': data['valor']}
        
        print('\nReserva cadastrada com sucesso')

    else:
        print('\nJa existe uma reserva para este quarto')

def res_update(cpf, apt):
    if apt in reservas:
        if  reservas[apt]['nome'] == hospede[cpf]['nome']:
            
            newapt = input("Digite o novo número do quarto: ")

            reservas[newapt] = reservas[apt]
            reservas[newapt]['valor'] = quartos[newapt]
            del reservas[apt]

            print("\nReserva atualizada com sucesso")

        else:
            print("\nNão é possível atualizar a reserva de outro hospede")

    else:
        print('\nQuarto reservado ou inexistente')

def res_read():
    print("--------------------------------------")
    print("--------------Reservas----------------")
    print("--------------------------------------")

    for key,value in reservas.items():
        print("Quarto: ", key, "\tValor: ", value['valor'], "\tNome: ", value['nome'])
    
def res_search():
    apt = input("Digite o número do quarto: ")
    cpf = input("Digite o CPF do hospede: ")
    
    if apt in reservas and cpf in hospede:
        print("\nQuarto: ", apt, "\tValor: ", reservas[apt]['valor'],'\nHospede: ', hospede[cpf]['nome'])
    else:
        print('\nQuarto não reservado')
    
def res_delete(reserva):
    if reserva in reservas:
        del reservas[reserva]
        print("\nReserva cancelada com sucesso")

def modulo_reserva():
    op = menu_reserva()

    while op != '0':
        if op == '1':
            print("\nEscolha o quarto: ")
            
            print("--------------- Quartos ----------------")
            for i in quartos:
                print("Quarto: ",i,"\tValor: ", quartos[i])
            print("----------------------------------------")
                
            apt = input("\nDigite o número do quarto: ")
            cpf = input("Digite o CPF do hospede: ")
            
            if cpf in hospede:
                if apt in quartos:
                    data = {
                        "apt": apt,
                        "is_ocupado": False,
                        "is_reservado": True,
                        "nome": hospede[cpf]['nome'],
                        "valor":quartos[apt]
                    }
                    
                    res_create(data)
                
                else:
                    print('Quarto não disponível ou inexistente')
            else:
                print('Hospede não cadastrado')

        elif op == '2':
            apt = input("Digite o número do quarto atual: ")
            cpf = input("Digite o CPF do hospede: ")
            res_update(cpf, apt)

        elif op == '3':
            res_read()

        elif op == '4':
            res_search()
            
        elif op == '5':
            res = input('Digite a reserva a ser deletada: ')

            res_delete(res)

        else:
            print('\nSeleção inválida') 

        print()
        input('Tecle ENTER para continuar')

        op = menu_reserva()