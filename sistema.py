import os
from datetime import date
from main_menu import *
from hospede import *
from funcionario import *
from reserva import *

op = menu_main()

while op != '0':
    if op == '1':
        modulo_hospede()

    elif op == '2':
        modulo_funcionario()

    elif op == '3':
        modulo_reserva()
      
    elif op == '4':
        #modulo_check()
        print("a")

    else:
        print('\nSeleção inválida') 

    print()
    input('Tecle ENTER para continuar')

    op = menu_main()