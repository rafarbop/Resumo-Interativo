#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess, sys

# Resumo de Python através de um menu no terminal
# com opções qual assunto deseja ver o resumo.


def titulo(wellcome):
    i = len(wellcome)+4
    erro = 0
    while i > 0:
        print("_",sep='', end='')
        i = i - 1
        erro = erro +1
        if erro == 500:
            break
    print("\n* ",wellcome.title()," *",sep='', end='\n\n')

def limpar_tela():
    retorno_limpar_tela = subprocess.run(['clear'])

def input_output_basics():
    limpar_tela()
    titulo("Demostrações Básicas de Entrada e Saída de Dados em Python:")
    print("Em Python3 usamos a função print() para exibir valores, palavras ou o retorno de outra função na saida padrão.")
    print("\tExemplo de código:")
    print('\t'+(len('print(2)')*2+4)*'-')
    print('\t>>> print(2)')
    print('\t{}'.format(2))
    print('\t'+(len('print(2)')*2+4)*'-')
    print("CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO\n")
    saida_resumo = input("Deseja finalizar o programa ou voltar ao menu inicial?\n0 - Finalizar\n1 - Voltar ao Menu Inicial\n:")
    print()
    if saida_resumo == '0':
        limpar_tela()
        sys.exit()
    if saida_resumo == '1':
        start_menu()
    else:
        print("Voçe digitou uma opção inválida!")
        input()
        input_output_basics()

def var_basics():
    limpar_tela()
    titulo("Veremos como utilizamos variáveis e quais os tipos existentes em python:")
    print("CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO\n")
    saida_resumo = input("Deseja finalizar o programa ou voltar ao menu inicial?\n0 - Finalizar\n1 - Voltar ao Menu Inicial\n:")
    print()
    if saida_resumo == '0':
        limpar_tela()
        sys.exit()
    if saida_resumo == '1':
        start_menu()
    else:
        print("Voçe digitou uma opção inválida!")
        input()
        var_basics()

def operation_basics():
    limpar_tela()
    titulo("Vamos rever quais são e como funcionam as principais operações básicas com variáveis em python:")
    print("CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO\n")
    saida_resumo = input("Deseja finalizar o programa ou voltar ao menu inicial?\n0 - Finalizar\n1 - Voltar ao Menu Inicial\n:")
    print()
    if saida_resumo == '0':
        limpar_tela()
        sys.exit()
    if saida_resumo == '1':
        start_menu()
    else:
        print("Voçe digitou uma opção inválida!")
        input()
        operation_basics()

def not_definied():
    limpar_tela()
    titulo("Menu ainda em desenvolvimento - Wait a little longer!")
    print("CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO","CONTEUDO\n")
    saida_resumo = input("Deseja finalizar o programa ou voltar ao menu inicial?\n0 - Finalizar\n1 - Voltar ao Menu Inicial\n:")
    print()
    if saida_resumo == '0':
        limpar_tela()
        sys.exit()
    if saida_resumo == '1':
        start_menu()
    else:
        print("Voçe digitou uma opção inválida!")
        input()
        not_definied()


def start_menu():
    limpar_tela()
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
        not_definied()
    else:
        print("Voçe digitou uma opção inválida!")
        input()
        start_menu()

start_menu()

limpar_tela()

#print("Voçe digitou a opção {}!".format(option_menu))
#print(f"Voçe digitou a opção {option_menu}!")
