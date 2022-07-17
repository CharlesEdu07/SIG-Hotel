import os
import pickle
from hospede import hospede, hosp_load_file, hosp_write_file

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

reservas = {}

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

def res_write_file():  
    arq_reserva = open("reserva.dat", "wb")

    pickle.dump(reservas, arq_reserva)

    arq_reserva.close()
            
def res_load_file():
    ld_reserva = {}

    try:
        arq_reserva = open("reserva.dat", "rb")
        ld_reserva = pickle.load(arq_reserva)
        arq_reserva.close()

    except:
        arq_reserva = open("reserva.dat", "wb")
        arq_reserva.close()

    return ld_reserva

def res_create(data):
    if data['apt'] not in reservas:
        reservas[data['apt']] = {
            'apt': data['apt'],
            'is_ocupado': data['is_ocupado'],
            'cpf':data['cpf'],
            'nome': data['nome'],
            'valor': data['valor']
        }
        
        print('\nReserva cadastrada com sucesso')

    else:
        print('\nVocê já fez uma reserva ou já existe uma reserva para este quarto')

def res_update(cpf, apt):
    if apt in reservas:
        if  reservas[apt]['nome'] == hospede[cpf]['nome']:
            newapt = input("\nDigite o novo número do quarto: ")

            reservas[newapt] = {
                **reservas[apt],
                'valor': quartos[newapt],
                'apt': newapt
            }

            del reservas[apt]

            print("\nReserva atualizada com sucesso")

        else:
            print("\nNão é possível atualizar a reserva de outro hospede")

    else:
        print('\nQuarto reservado ou inexistente')

def res_read():
    if reservas != {}:
        print()
        print("--------------------------------------------")
        print("---------------  Reservas  -----------------")
        print("--------------------------------------------")

        for key,value in reservas.items():
            print("Quarto: ", key, "\tValor: ", value['valor'], "\tNome: ", value['nome'])

    else:
        print('\nNão existem reservas feitas')
    
def res_search():
    apt = input("\nDigite o número do quarto: ")
    
    if apt in reservas:
        print("\nQuarto: ", apt, "\tValor: ", reservas[apt]['valor'], '\nHospede: ', reservas[apt]['nome'])
        
        if reservas[apt]['is_ocupado'] == "sim" :
            print("\nQuarto: ", apt, "\tValor: ", reservas[apt]['valor'], '\nHospede: ', reservas[apt]['nome'], "\tData de entrada: ", reservas[apt]['data_entrada'])

        elif reservas[apt]['is_ocupado'] == "nao":
            print("\nQuarto: ", apt, "\tValor: ", reservas[apt]['valor'], '\nHospede: ', reservas[apt]['nome'], "\tData de saida: ", reservas[apt]['data_saida'])

    else:
        print('\nQuarto não reservado')
    
def res_delete(reserva):
    if reserva in reservas:
        del reservas[reserva]

        print("\nReserva cancelada com sucesso")

    else:
        print('\nReserva não existe')

def show_quartos():
    print("--------------- Quartos ----------------")
    for i in quartos:
        print("Quarto: ",i,"\tValor: ", quartos[i])
    print("----------------------------------------")

def res_read_data():
    apt = input("\nDigite o número do quarto: ")
    cpf = input("Digite o CPF do hospede: ")
            
    if cpf in hospede:
        if apt in quartos:
            data = {
                "apt": apt,
                "is_ocupado": "vazio",
                "is_reservado": True,
                "cpf": hospede[cpf]['cpf'],
                "nome": hospede[cpf]['nome'],
                "valor": quartos[apt]
            }
                    
            res_create(data)
                
        else:
            print('\nQuarto não disponível ou inexistente')
    else:
        print('\nValores inválidos')

def modulo_reserva():
    op = menu_reserva()

    global hospede
    hospede = hosp_load_file()

    global reservas
    reservas = res_load_file()

    while op != '0':
        if op == '1':
            print("\nEscolha o quarto: ")
            
            show_quartos()
                
            res_read_data()

        elif op == '2':
            print("\nATUALIZAR RESERVA")

            apt = input("\nDigite o número do quarto atual: ")
            cpf = input("Digite o CPF do hospede: ")

            res_update(cpf, apt)

        elif op == '3':
            res_read()

        elif op == '4':
            print("\nPESQUISAR RESERVA")

            res_search()
            
        elif op == '5':
            print("\nDELETAR RESERVA")

            res = input('\nDigite a reserva a ser deletada: ')

            res_delete(res)

        else:
            print('\nSeleção inválida') 

        res_write_file()
        hosp_write_file()

        print()
        input('Tecle ENTER para continuar')

        op = menu_reserva()