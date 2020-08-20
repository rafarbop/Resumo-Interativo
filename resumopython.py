#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, sys, time

# Resumo de Python através de um menu no terminal
# com opções qual assunto deseja ver o resumo.


def titulo(texto_titulo):
    i = len(texto_titulo)+4
    print("\n> ",texto_titulo.upper()," <",sep='')
    print(i*"^",sep='')

def subtitulo(texto_subtitulo):
    i = len(texto_subtitulo)+6
    print(i*"_",sep='')
    print("\n>> ",texto_subtitulo.title()," <<",sep='')

def cabecalho():
    subprocess.run(['clear'])
    texto_cabecalho = 'Resumo em Python'
    print(len(texto_cabecalho.center(50,'-'))*'-')
    print(texto_cabecalho.center(50,'-'))
    print(len(texto_cabecalho.center(50,'-'))*'=')


def input_output_basics():
    cabecalho()
    titulo("Demostrações Básicas de Entrada e Saída de Dados em Python")

    subtitulo("Imprimir valores, palavras ou variáveis na saida padrão:".upper())
    print("   Comando:")
    print('\t'+r"print(numero, var_qualquer, True, 'string',f'string {var_qualquer}') ou")
    print('\t'+r"print('string {} e {:.2f}'.format(var_qualquer,var_numero),sep=' ',end='\n')")
    print('\n   OBS.:\n   Vários argumentos com print() é só separar por ,')
    print("   sep=' ' é o separador padrão entre os argumentos e end='\\n' é o fim de linha padrão.'")
    print('   Usar aspas simples ou duplas.')
    print('   :.2f irá retorna um número com 2 casas decimais.')
    print('   print() irá apenas pular uma linha.')

    subtitulo("Receber entrada de dados:".upper())
    print('   Comando:')
    print('\t'+r"input('Texto a ser mostrado antes da entrada de dados: ')")
    print('\n   OBS.:\n   Função input retorna sempre uma string.')
    print('   input() irá esperar ser digitado Enter - Não salva nada do que foi digitado')
    print('   Aceita mesmas opções de formatação que print(), porém input() so aceita 1 argumento')
    
    saida_resumo = input("\n\nDeseja finalizar o programa ou voltar ao menu inicial?\n0 - Finalizar\n1 - Voltar ao Menu Inicial\n:")
    print()
    if saida_resumo == '0':
        subprocess.run(['clear'])
        sys.exit()
    if saida_resumo == '1':
        start_menu()
    else:
        print("Voçe digitou uma opção inválida!")
        time.sleep(1)
        input_output_basics()

def var_basics():
    cabecalho()
    titulo("Veremos como utilizamos variáveis e quais os tipos existentes em python:")

    subtitulo("CONTEUDO "+"CONTEUDO "+"CONTEUDO "+"CONTEUDO "+"CONTEUDO "+"CONTEUDO\n")

    saida_resumo = input("Deseja finalizar o programa ou voltar ao menu inicial?\n0 - Finalizar\n1 - Voltar ao Menu Inicial\n:")
    print()
    if saida_resumo == '0':
        subprocess.run(['clear'])
        sys.exit()
    if saida_resumo == '1':
        start_menu()
    else:
        print("Voçe digitou uma opção inválida!")
        time.sleep(1)
        var_basics()

def operation_basics():
    cabecalho()
    titulo("Vamos rever quais são e como funcionam as principais operações básicas com variáveis em python:")

    subtitulo("CONTEUDO"+"CONTEUDO"+"CONTEUDO"+"CONTEUDO"+"CONTEUDO"+"CONTEUDO\n")

    saida_resumo = input("Deseja finalizar o programa ou voltar ao menu inicial?\n0 - Finalizar\n1 - Voltar ao Menu Inicial\n:")
    print()
    if saida_resumo == '0':
        subprocess.run(['clear'])
        sys.exit()
    if saida_resumo == '1':
        start_menu()
    else:
        print("Voçe digitou uma opção inválida!")
        time.sleep(1)
        operation_basics()

def nao_definido():
    cabecalho()
    titulo("Menu ainda em desenvolvimento - Wait a little longer!")

    subtitulo("CONTEUDO"+"CONTEUDO"+"CONTEUDO"+"CONTEUDO"+"CONTEUDO"+"CONTEUDO\n")

    saida_resumo = input("Deseja finalizar o programa ou voltar ao menu inicial?\n0 - Finalizar\n1 - Voltar ao Menu Inicial\n:")
    print()
    if saida_resumo == '0':
        subprocess.run(['clear'])
        sys.exit()
    if saida_resumo == '1':
        start_menu()
    else:
        print("Voçe digitou uma opção inválida!")
        time.sleep(1)
        nao_definido()


def start_menu():
    cabecalho()
    titulo("Bem Vindo ao Resumo de Python feito com Python")
    print("Escolha qual assunto deseja revisar os principais conceitos e funções:\n")
    print("\t1 - Saída e Entrada de Dados - Básico")
    print("\t2 - Tipos de Variáveis - Declarações e Atribuições")
    print("\t3 - Operações Básicas com Variáveis")
    print("\t4 - ...")
    print("\n\t0 - Finalizar Programa!")
    option_menu = input("\n- Digite um número de acordo com as opções acima: ".upper())
    print()
    if option_menu == '0':
        return
    if option_menu == '1':
        input_output_basics()
    if option_menu == '2':
        var_basics()
    if option_menu == '3':
        operation_basics()
    if option_menu == '4':
        nao_definido()
    else:
        print("Voçe digitou uma opção inválida!")
        time.sleep(1)
        start_menu()

start_menu()

subprocess.run(['clear'])

#print("Voçe digitou a opção {}!".format(option_menu))
#print(f"Voçe digitou a opção {option_menu}!")
