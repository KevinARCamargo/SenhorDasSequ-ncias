#Imports
import sys
from variaveisGlobais.variaveisGlobais import *
from classes.usuario import *
from funcoes.uso import *

sys.setrecursionlimit(10000000)
execucao = True

#Main
while(execucao == True):
    limpar_terminal()
    print(menu)
    opcao = int(input(" Escolha uma opcao: "))

    if igual(opcao,1):
        limpar_terminal()
        print(regras)
        opcao = input()
        limpar_terminal()
        print(regrasSeq)
        opcao = input(" Estamos entendidos ? (s/sim) ou (n/não): ")
        if(opcao == 's'):
            limpar_terminal()
            n1 = input("\n\n Qual o nome do primeiro desafiante?: ")
            n2 = input("\n\n Qual o nome do segundo desafiante?: ")
            player1 = Usuario(n1, 0)
            player2 = Usuario(n2, 0)
            limpar_terminal()
            sequencias = gerar_sequencias()
            start(player1,player2,sequencias)
            rank(player1,player2)
        else:
            limpar_terminal()
            opcao = False

    elif(opcao == 2):
        limpar_terminal()
        print(regras)
        opcao = input()
        limpar_terminal()
        print(regrasSeq)
        opcao = input(" Estamos entendidos ? (s/sim) ou (n/não): ")
        if(opcao == 's'):
            limpar_terminal()
            n1 = input("\n\n Qual o nome do primeiro desafiante?: ")
            n2 = input("\n\n Qual o nome do segundo desafiante?: ")
            n3 = input("\n\n Qual o nome do terceiro desafiante?: ")
            player1 = Usuario(n1, 0)
            player2 = Usuario(n2, 0)
            player3 = Usuario(n3, 0)
            limpar_terminal()
            start(player1,player2, sequencias, player3)
            exibir_sequencias(sequencias)  # Exibir as sequências ao final do jogo
            rank(player1,player2, player3)
        else:
            limpar_terminal()
            opcao = False

    else:
        execucao = False

sequencias = gerar_sequencias()
exibir_sequencias(sequencias)  # Exibir as sequências ao final do jogo
input()