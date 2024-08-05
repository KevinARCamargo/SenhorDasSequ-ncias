#Imports
import random
import os
import sys


sys.setrecursionlimit(10000000)
execucao = True
#Classes
class Usuario:
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    def __str__(self):
        return f"Nome: {self.nome}, Pontos: {self.pontos}"
    
    def setPontos(self):
        self.pontos = self.pontos + 1

#Variáveis Globais
menu = """\n ***** Senhor das Sequências *****\n\n
 1 - Dois Players
 2 - Três Players
 0 - Sair

"""
regras = """\n\n\n                                                                    ***** REGRAS DO JOGO *****\n
                     Será gerado 10 sequências com 3 elementos, cabe a vocês responderem qual a operação base para a formação da mesma!

                     Dica: Além das sequências você irá receber dois números que são partes fundamentais da operação que compôs a sequência

                    Todos os jogadores receberão as mesmas sequências para pontuar, cada acerto vale um ponto, quem fizer mais pontos será o 
\n                                                                    SENHOR DAS SEQUÊNCIAS!!!
 
"""

regrasSeq = """                                                                 ***** LÓGICA DAS SEQUÊNCIAS *****\n
 
 SOMA: O primeiro elemento é gerado aleatóriamente, o segundo e terceiro são resultantes de uma soma com outro número gerado aleatóriamente
 Ex: (X = 10, Y = 2) 10 -> 12 (10+2) -> 14(12+2)

 SUBTRAÇÂO: O primeiro elemento é gerado aleatóriamente, o segundo e terceiro são resultantes de uma subtração com outro número gerado aleatóriamente
 Ex: (X = 10, Y = 2) 10 -> 8 (10-2) -> 6(8-2)

 MULTIPLICAÇÃO: O primeiro elemento é gerado aleatóriamente, o segundo e terceiro são resultantes de uma multiplicação com outro número gerado aleatóriamente
 Ex: (X = 10, Y = 2) 10 -> 20 (10*2) -> 40(20*2)

 EXPONENCIAÇÃO: O primeiro elemento é gerado aleatóriamente, o segundo e terceiro são resultantes de uma exponenciação com outro número gerado aleatóriamente
 Ex: (X = 2, Y = 2) 2 -> 4 (2^2) -> 16(4^2)

 FATORIAL: A Sequência é gerada a partir de um fatorial gerado aleatóriamente e seus subsequêntes
 Ex: (X = 1) 1 (1!) -> 2 (2!) -> 6(3!)

 DIV CHÃO: O primeiro elemento é a resultante inteira (arredondada para baixo) de um inteiro X dividido por um inteiro Y ambos gerados aleatóriamente,
 o segundo e terceiro são resultantes da divisão de Y+1 e Y+2 
 Ex: (X = 10, Y = 3) 3 (10/3) -> 2 (10/4) -> 2(10/5)

 DIV TETO: O primeiro elemento é a resultante inteira (arredondada para cima) de um inteiro X dividido por um inteiro Y ambos gerados aleatóriamente,
 o segundo e terceiro são resultantes da divisão de Y+1 e Y+2 
 Ex: (X = 10, Y = 3) 4 (10/3) -> 3 (10/4) -> 2(10/5)

 PERCENTUAL: O primeiro elemento é gerado aleatóriamente, o segundo e terceiro são resultantes de um percentual de X gerado aleatóriamente 
 Ex: (X = 100) 100 -> 40 (40% de 100) -> 65 (65% de 100)

 RESTO DE DIVISÂO: O primeiro elemento é a resto da divisão inteira (arredondada para baixo) de um inteiro X dividido por um inteiro Y ambos gerados aleatóriamente,
 o segundo e terceiro são restos da divisão inteira de Y+1 e Y+2 
 Ex: (X = 10, Y = 3) 1 (10/3) -> 2 (10/4) -> 0 (10/5)

"""

respostas = """\n a) Adição
 b) Subtração
 c) Multiplicação
 d) Exponenciação
 e) Fatorial
 f) Div Chão
 g) Div Teto
 h) Percentual
 i) Resto de Divisão
"""

#Funções
def sucessora(n):
    return n + 1

def ant(x):
    if x == 0:
        return 0
    else:
        return x - 1

def soma(x, y):
    if y == 0:
        return x
    else:
        return sucessora(soma(x, y - 1))

def subt(x, y):
    if y == 0:
        return x
    else:
        return ant(subt(x, y - 1))

def mult(x, y):
    if y == 0:
        return 0
    else:
        return soma(x, mult(x, y - 1))
    
def elevado(x, y):
    if y == 0:
        return 1
    else:
        return mult(x, elevado(x, y - 1))

def fatorial(x):
    if x == 0:
        return 1
    else:
        return mult(x, fatorial(x - 1))

def div_chao(dividendo, divisor):
    if dividendo < divisor:
        return 0
    else:
        return 1 + div_chao(subt(dividendo, divisor), divisor)

def div_teto(dividendo, divisor):
    if dividendo < divisor:
        return 1
    else:
        return 1 + div_teto(subt(dividendo, divisor), divisor)

def percentual(x, y):
    produto = mult(x, y)
    return div_chao(produto, 100)

def resto(x, y):
    if x < y:
        return x
    else:
        return resto(subt(x, y), y)
    
#Funções de Uso
def limpar_terminal():
    os.system('cls')

def gerar_sequencias():
    sequencias = []
    for i in range(10):
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
            while(x < 3 * y):
                x = random.randint(0, 100)
                y = random.randint(0, 100)
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
            x = random.randint(0, 5)
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
                y = random.randint(0, 100)
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
                y = random.randint(0, 100)
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
                y = random.randint(0, 100)
            lista = []
            saveY = y
            for i in range(3):
                lista.append(resto(x, y))
                y = y + 1
            lista.append("i")
            lista.append(x)
            lista.append(saveY)
            sequencias.append(lista)
    for elemento in sequencias:
        print(elemento)

    return sequencias

def questoes(sequencias, player):
    for elemento in sequencias:
        limpar_terminal()
        print(f"\n DICA: {elemento[4]} e {elemento[5]}\n\n")
        print(f" Elementos: {elemento[0]} - {elemento[1]} - {elemento[2]}")
        print(respostas)
        resposta = input("\n\n Qual a operação geradora: ")
        if resposta == elemento[3]:
            player.setPontos()
    print(player)
    print("Esta foi sua pontuação! Parabéns (ou não)!")
    input("\n\nPressione enter para continuar")


def start(player1, player2, sequencias):
    print("\n\n START ")
    input("")
    limpar_terminal()
    questoes(sequencias, player1)
    questoes(sequencias, player2)
    if player1.pontos > player2.pontos:
        print(f"Parabéns {player1.nome}! Você é o SENHOR DAS SEQUÊNCIAS")
    elif player1.pontos == player2.pontos:
        print(f"Infelizmente não consegui decidir quem é o SENHOR DAS SEQUÊNCIAS joguem outra partida")
    else:
        print(f"Parabéns {player2.nome}! Você é o SENHOR DAS SEQUÊNCIAS")


#Main
while(execucao == True):
    limpar_terminal()
    print(menu)
    opcao = int(input(" Escolha uma opcao: "))

    if(opcao == 1):
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
        else:
            limpar_terminal()
            opcao = False

    elif(opcao == 2):
        print("3 Players")
    elif(opcao == 0):
        execucao = False