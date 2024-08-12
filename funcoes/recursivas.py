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
    if divisor > dividendo:
        return 0
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
    
def maximo(x, y):
    if subt(x, y) >= 0:
        return x
    else:
        return y

def minimo(x, y):
    if subt(x, y) <= 0:
        return x
    else:
        return y
    
def igual(x, y):
    return subt(x, y) == 0

def diferente(x, y):
    return subt(x, y) != 0

