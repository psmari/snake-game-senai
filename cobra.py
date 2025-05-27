import pygame 

class Cobra:
    # construtor
    def __init__(self, coordenada_x, coordenada_y, altura, largura):
        self.altura = altura
        self.largura = largura
        self.x = coordenada_x
        self.y = coordenada_y
        # cor no pygame é no padrão RGB
        self.cor = (0, 255, 0)
    
    # métodos
    def movimentar(self, tecla):
        # verifica se clicou na tecla seta para esquerda
        if tecla == pygame.K_LEFT:
            # diminuindo o valor em 30 da variavel x
            self.x = self.x - 30
        # verifica se clicou na tecla seta para direita
        if tecla == pygame.K_RIGHT:
            # aumentando o valor em 30 da variavel x
            self.x = self.x + 30
        # verificando se clicou na tecla para cima
        if tecla == pygame.K_UP:
            # diminuindo 30 o valor da variavel y
            self.y = self.y - 30
        # verificando se a tecla para baixo foi clicada
        if tecla == pygame.K_DOWN:
            # aumentando 30 o valor da variavel y 
            self.y = self.y + 30
    
    def aparecer():
        ...