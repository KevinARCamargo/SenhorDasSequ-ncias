class Usuario:
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos

    def __str__(self):
        return f" Nome: {self.nome} - Pontos: {self.pontos}"
    
    def setPontos(self):
        self.pontos = self.pontos + 1