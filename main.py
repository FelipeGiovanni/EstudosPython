import sqlite3
import csv
from conecta import *
from armas import arma

def NovaArma():
    nome = input('Digite o nome da arma: ')
    custo = int(input('Digite o custo da arma: '))
    dano = int(input('Digite o dano da arma: '))
    peso = int(input('Digite o peso da arma: '))
    global NArma
    NArma = arma(nome, custo, dano, peso)

CriaTabela()

print('### Bem Vindo a Forja ###')
print('O que deseja?')
opcao = int(input('1 - Inserir nova arma\n2 - Consulta arsenal\nOpção: '))
if (opcao == 1):
    NovaArma()
    InsereDados(NArma.nome, NArma.custo, NArma.dano, NArma.peso)
    while (True):
        opcao = int(input('Deseja adicionar outra arma?\n1 - Sim\n2 - Não\nOpção: '))
        if (opcao == 1):
            NovaArma()
            InsereDados(NArma.nome, NArma.custo, NArma.dano, NArma.peso)
        else:
            print('Obrigado por utilizar a forja')
            break

elif opcao==2:
    ConsultaArsenal()
    while (True):
        opcao = int(input('Deseja adicionar outra arma?\n1 - Sim\n2 - Não\nOpção: '))
        if (opcao == 1):
            NovaArma()
            InsereDados(NArma.nome, NArma.custo, NArma.dano, NArma.peso)
        else:
            print('Obrigado por utilizar a forja')
            break

'''
def NovaLista(nome, custo, dano, peso):
    with open('armas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nome", "Custo", "Dano", "Peso"])
        writer.writerow([nome, custo, dano, peso])        

def AdicionaLista(nome, custo, dano, peso):
    with open('armas.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, custo, dano, peso])

print('### Bem Vindo a Forja ###')
print('O que deseja?')
opcao = int(input('1 - Novo arsenal nova arma\n2 - Nova arma\nOpção: '))
if (opcao == 1):
    NovaArma()
    NovaLista(NArma.nome, NArma.custo, NArma.dano, NArma.peso)

    while (True):
        opcao = int(input('Deseja adicionar outra arma?\n1 - Sim\n2 - Não\nOpção: '))
        if (opcao == 1):
            NovaArma()
            AdicionaLista(NArma.nome, NArma.custo, NArma.dano, NArma.peso)
        else:
            print('Obrigado por utilizar a forja')
            break

elif opcao==2:
    NovaArma()
    AdicionaLista(NArma.nome, NArma.custo, NArma.dano, NArma.peso)

    while (True):
        opcao = int(input('Deseja adicionar outra arma?\n1 - Sim\n2 - Não\nOpção: '))
        if (opcao == 1):
            NovaArma()
            AdicionaLista(NArma.nome, NArma.custo, NArma.dano, NArma.peso)
        else:
            print('Obrigado por utilizar a forja')
            break
'''