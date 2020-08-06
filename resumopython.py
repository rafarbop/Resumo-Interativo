# Resumo de Python através de um menu no terminal
# com opções qual assunto deseja ver o resumo.

wellcome = "Bem Vindo ao Resumo de Python feito com Python"
i = len(wellcome)+4
erro = 0
while i > 0:
    print("_",sep='', end='')
    i = i - 1
    erro = erro +1
    if erro == 500:
        break

print("\n| ",wellcome," |",sep='', end='\n\n')

option0 = input("Digite qual comando deseja Revisar ou digite \"menu\" para ver as opções disponíveis!\n:")

if (option0 == "menu" or option0 == "Menu" or option0 == "MENU"):
    print("\nOpções implementadas até o momento:")
    print("1 - Saída e Entrada de Dados - Básico")
    print("2 - Tipos de Variáveis - Declarações e Atribuições")
    print("3 - Operações Básicas com Variáveis")
    print("4 - ...")
    print("0 - Finalizar Programa!")
    option_menu = input(":")
else:
    print("Voçe não digitou um comando válido ou não implementado ainda.\n\nFim do Programa - Volte Sempre ")