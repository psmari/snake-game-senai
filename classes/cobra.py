import pygame

class Cobra:
    def __init__(self, x, y, tamanho_bloco):
        self.tamanho_bloco = tamanho_bloco
        self.cor = (0, 0, 0)
        self.corpo = [(x, y)]
        self.direcao = (0, 0)

    def mover(self):
        if self.direcao == (0, 0):
            return

        novo_x = self.corpo[0][0] + self.direcao[0] * self.tamanho_bloco
        novo_y = self.corpo[0][1] + self.direcao[1] * self.tamanho_bloco
        novo_cabeca = (novo_x, novo_y)

        self.corpo = [novo_cabeca] + self.corpo[:-1]

    def crescer(self):
        self.corpo.append(self.corpo[-1])

    def desenhar(self, superficie):
        for segmento in self.corpo:
            pygame.draw.rect(superficie, self.cor, (segmento[0], segmento[1], self.tamanho_bloco, self.tamanho_bloco))

    def mudar_direcao(self, tecla):
        if tecla == pygame.K_LEFT and self.direcao != (1, 0):
            self.direcao = (-1, 0)
        elif tecla == pygame.K_RIGHT and self.direcao != (-1, 0):
            self.direcao = (1, 0)
        elif tecla == pygame.K_UP and self.direcao != (0, 1):
            self.direcao = (0, -1)
        elif tecla == pygame.K_DOWN and self.direcao != (0, -1):
            self.direcao = (0, 1)

    def colidiu_com_si_mesma(self):
        if len(self.corpo) < 6:
            return False  # só verifica se for grande o suficiente para se morder
        return self.corpo[0] in self.corpo[1:]

    def colidiu_com_parede(self, largura, altura):
        x, y = self.corpo[0]
        return not (0 <= x <= largura and 0 <= y <= altura)
