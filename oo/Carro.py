class Motor:
    def __init__(self, velocidade = 0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade < 2:
            self.velocidade = 0
        else:
            self.velocidade -= 2

class Direcao:
    def __init__(self, direcao:str):
        self.direcao = direcao

    def girar_a_direita(self):
        if self.direcao == 'norte':
            self.direcao = 'leste'
        elif self.direcao == 'leste':
            self.direcao = 'sul'
        elif self.direcao == 'sul':
            self.direcao = 'oeste'
        else:
            self.direcao = 'norte'

    def girar_a_esquerda(self):
        if self.direcao == 'norte':
            self.direcao = 'oeste'
        elif self.direcao == 'oeste':
            self.direcao = 'sul'
        elif self.direcao == 'sul':
            self.direcao = 'leste'
        else:
            self.direcao = 'norte'

class Carro:
    def __init__(self, cardeal, velocidade = 0):
        self.motor = Motor(velocidade)
        self.direcao = Direcao(cardeal)

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_velocidade(self):
        return self.motor.velocidade

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

    def calcular_direcao(self):
        return self.direcao.direcao

if __name__ == '__main__':
    carro = Carro('leste')
    for _ in range(86):
        carro.acelerar()
        carro.girar_a_direita()
    print(carro.calcular_direcao())
    print(carro.calcular_velocidade())





