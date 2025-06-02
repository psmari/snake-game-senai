import pygame
import random

class Comida:
    def __init__(self, largura, altura, tamanho_bloco):
        self.largura = largura
        self.altura = altura
        self.tamanho_bloco = tamanho_bloco
        self.cor = (255, 0, 0)
        self.posicao = (0, 0)
        self.gerar_nova()

    def gerar_nova(self):
        colunas = self.largura // self.tamanho_bloco
        linhas = self.altura // self.tamanho_bloco
        self.posicao = (
            random.randint(0, colunas - 1) * self.tamanho_bloco,
            random.randint(0, linhas - 1) * self.tamanho_bloco
        )

    def desenhar(self, superficie):
        pygame.draw.rect(superficie, self.cor, (self.posicao[0], self.posicao[1], self.tamanho_bloco, self.tamanho_bloco))

