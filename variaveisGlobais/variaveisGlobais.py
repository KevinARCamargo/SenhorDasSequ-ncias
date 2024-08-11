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

 PERCENTUAL: O primeiro elemento  é gerado aleatóriamente, o segundo e terceiro são resultantes de um percentual de X gerado aleatóriamente,
 (A parte fracionária não será exibida, somente a inteira)
 Ex: (X = 100) 100 -> 40 (40% de 100) -> 65 (65% de 100)
 Ex: (X = 101) 101 -> 10 (10% de 101) -> 10 (não 10,1)

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
 h) Percentual (Parte Inteira)
 i) Resto de Divisão
"""