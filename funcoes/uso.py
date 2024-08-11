#Imports
import random
import os
from funcoes.recursivas import *
from variaveisGlobais.variaveisGlobais import *

#Funções de Uso
def limpar_terminal():
    os.system('cls')

def gerar_sequencias():
    sequencias = []
    for i in range(5):
        operacao = random.randint(0, 8)
        if(operacao == 0): #Soma
            x = random.randint(0, 100)
            saveX = x
            y = random.randint(1, 100)
            lista = []
            for i in range(3):
                lista.append(x)
                x = soma(x, y)
            lista.append("a")
            lista.append(saveX)
            lista.append(y)
            sequencias.append(lista)
            

        if(operacao == 1): #Subtracao
            x = 1
            y = 1
            while(x < 2 * y):
                x = random.randint(0, 100)
                y = random.randint(0, 50)
            lista = []
            saveX = x
            for i in range(3):
                lista.append(x)
                x = subt(x, y)
            lista.append("b")
            lista.append(saveX)
            lista.append(y)
            sequencias.append(lista)

        if(operacao == 2): #Multiplicacao
            x = random.randint(0, 100)
            y = random.randint(0, 10)
            lista = []
            saveX = x
            for i in range(3):
                lista.append(x)
                x = mult(x, y)
            lista.append("c")
            lista.append(saveX)
            lista.append(y)
            sequencias.append(lista)

        if(operacao == 3): #Potência
            x = random.randint(0, 4)
            y = random.randint(0, 2)
            lista = []
            saveX = x
            for i in range(3):
                lista.append(x)
                x = elevado(x, y)
            lista.append("d")
            lista.append(saveX)
            lista.append(y)
            sequencias.append(lista)

        if(operacao == 4): #Fatorial
            x = random.randint(1, 6)
            x = x - 1
            saveX = x
            lista = []
            for i in range(3):
                lista.append(fatorial(x))
                x = x + 1   
            lista.append("e")
            lista.append(saveX)
            lista.append(saveX + 1)
            sequencias.append(lista)

        if(operacao == 5): #Div Chão
            x = 0
            y = 1
            while(x < y):
                x = random.randint(0, 100)
                y = random.randint(1, 100)
            lista = []
            saveY = y
            for i in range(3):
                lista.append(div_chao(x, y))
                y = y + 1  
            lista.append("f")
            lista.append(x)
            lista.append(saveY)
            sequencias.append(lista)

        if(operacao == 6): #Div Teto
            x = 0
            y = 1
            while(x < y):
                x = random.randint(0, 100)
                y = random.randint(1, 100)
            lista = []
            saveY = y
            for i in range(3):
                lista.append(div_teto(x, y))
                y = y + 1
            lista.append("g")
            lista.append(x)
            lista.append(saveY)
            sequencias.append(lista)

        if(operacao == 7): #Percentual
            x = random.randint(0, 100)
            y = random.randint(0, 100)
            lista = []
            saveY = y
            lista.append(x)
            for i in range(2):
                lista.append(percentual(x, y))
                y = random.randint(0, 100)
            lista.append("h")
            lista.append(x)
            lista.append(saveY)
            sequencias.append(lista)

        if(operacao == 8): #Resto
            x = 0
            y = 1
            while(x < y):
                x = random.randint(0, 100)
                y = random.randint(1, 100)
            lista = []
            saveY = y
            for i in range(3):
                lista.append(resto(x, y))
                y = y + 1
            lista.append("i")
            lista.append(x)
            lista.append(saveY)
            sequencias.append(lista)

    return sequencias

def exibir_sequencias(sequencias):
    limpar_terminal()
    print("\n ***** SEQUÊNCIAS DA PARTIDA *****\n")
    for elemento in sequencias:
        if elemento[3] == 'a':
            resposta = 'Soma'
        elif elemento[3] == 'b':
            resposta = 'Subtração'
        elif elemento[3] == 'c':
            resposta = 'multiplicação'
        elif elemento[3] == 'd':
            resposta = 'Potencia'
        elif elemento[3] == 'e':
            resposta = 'Fatorial'
        elif elemento[3] == 'f':
            resposta = 'Div Chão'
        elif elemento[3] == 'g':
            resposta = 'Div Teto'
        elif elemento[3] == 'h':
            resposta = 'Percentual'
        else:
            resposta = 'Resto'
        print(f" {elemento[0]} -> {elemento[1]} -> {elemento[2]} - Resposta: {resposta} - {elemento[4]} e {elemento[5]}")
    input()

def questoes(sequencias, player):
    for elemento in sequencias:
        limpar_terminal()
        print(f"\n DICA: {elemento[4]} e {elemento[5]}\n\n")
        print(f" Elementos: {elemento[0]} - {elemento[1]} - {elemento[2]}")
        print(respostas)
        resposta = input("\n\n Qual a operação geradora: ")
        if resposta == elemento[3]:
            player.setPontos()
    limpar_terminal()
    input("\n\n                                                                       Pressione enter para continuar")

def rank(player1, player2, player3 = None):
    limpar_terminal()
    senhor = []
    print("\n ***** RANKING *****\n")

    if player3 == None:

        if player1.pontos >= player2.pontos:
            print(player1)
            print(player2)
            senhor.append(player1)
            senhor.append(player2)
        else:
            print(player2)
            print(player1)
            senhor.append(player2)
            senhor.append(player1)
    else:
        
        if player1.pontos >= player2.pontos and player1.pontos >= player3.pontos:
            print(player1)
            senhor.append(player1)
            if player2.pontos >= player3.pontos:
                print(player2)
                print(player3)
                senhor.append(player2)
                senhor.append(player3)
            else:
                print(player3)
                print(player2)
                senhor.append(player3)
                senhor.append(player2)

        elif player2.pontos >= player1.pontos and player2.pontos >= player3.pontos:
            print(player2)
            senhor.append(player2)
            if player1.pontos >= player3.pontos:
                print(player1)
                print(player3)
                senhor.append(player1)
                senhor.append(player3)
            else:
                print(player3)
                print(player1)
                senhor.append(player3)
                senhor.append(player1)
        else:
            print(player3)
            senhor.append(player3)
            if player1.pontos >= player2.pontos:
                print(player1)
                print(player2)
                senhor.append(player1)
                senhor.append(player2)
            else:
                print(player2)
                print(player1)
                senhor.append(player2)
                senhor.append(player1)
    input()
    limpar_terminal()
    if senhor[0].pontos > senhor[1].pontos and senhor[0].pontos >= 3:
        print(f"\n\n                                                  Parabéns {senhor[0].nome} você se provou digno do título de ...")
        print("\n                                                                      SENHOR DAS SEQUÊNCIAS")
    elif senhor[0].pontos > senhor[1].pontos:
        print(f"\n\n                                                  Parabéns pela vitória {senhor[0].nome} no entanto você não é digno do título de ...")
        print("\n                                                                               SENHOR DAS SEQUÊNCIAS")
    else:
        print("\n\n                                                      Infelizmente tivemos um empate, será necessária uma nova partida")
    
    input()

def start(player1, player2, sequencias, player3 = None):
    print("\n\n                                                                                  START ")
    input("")
    limpar_terminal()
    if player3 == None:
        questoes(sequencias, player1)
        questoes(sequencias, player2)
    else:
        print(player3)
        questoes(sequencias, player1)
        questoes(sequencias, player2)
        questoes(sequencias, player3)
    limpar_terminal()