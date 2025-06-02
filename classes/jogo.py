import pygame 
import pygame_gui
from classes.cobra import Cobra
from classes.comida import Comida

class JogoCobrinha:
    def __init__(self):
        pygame.init()
        self.largura = 800
        self.altura = 800
        self.tamanho_bloco = 30
        self.tela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Jogo da Cobrinha")

        self.cor_fundo = (93, 101, 209)
        self.clock = pygame.time.Clock()
        self.fonte = pygame.font.SysFont(None, 36)

        self.gerente = pygame_gui.UIManager((self.largura, self.altura), "theme.json")
        self.estado = "inicio"
        self.rodando = True

        self.pontuacao = 0

        self.botao_iniciar = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(((self.largura - 200) // 2, (self.altura - 60) // 2), (200, 60)),
            text="Start Game",
            manager=self.gerente,
            object_id="#botao_start"
        )

        self.reiniciar()

    def reiniciar(self):
        x = self.largura // 2 - self.tamanho_bloco // 2
        y = self.altura // 2  - self.tamanho_bloco // 2
        self.cobra = Cobra(x, y, self.tamanho_bloco)
        self.comida = Comida(self.largura, self.altura, self.tamanho_bloco)
        self.pontuacao = 0

    def desenhar_pontuacao(self):
        texto = self.fonte.render(f"Pontuação: {self.pontuacao}", True, (255, 255, 255))
        self.tela.blit(texto, (10, 10))

    def processar_eventos(self):
        for evento in pygame.event.get():
            self.gerente.process_events(evento)

            if evento.type == pygame.QUIT:
                self.rodando = False

            elif evento.type == pygame_gui.UI_BUTTON_PRESSED:
                if evento.ui_element == self.botao_iniciar:
                    self.estado = "jogando"
                    self.reiniciar()

            elif evento.type == pygame.KEYDOWN and self.estado == "jogando":
                self.cobra.mudar_direcao(evento.key)

    def atualizar(self, delta):
        if self.estado == "jogando":
            self.cobra.mover()

            cabeca = pygame.Rect(
                self.cobra.corpo[0][0], self.cobra.corpo[0][1],
                self.tamanho_bloco, self.tamanho_bloco
            )
            comida_rect = pygame.Rect(
                self.comida.posicao[0], self.comida.posicao[1],
                self.tamanho_bloco, self.tamanho_bloco
            )
            
            # Verifica colisão com a comida
            if cabeca.colliderect(comida_rect):
                self.cobra.crescer()
                self.comida.gerar_nova()
                self.pontuacao += 1

            # Verifica colisão com parede ou si mesma
            if self.cobra.colidiu_com_parede(self.largura, self.altura) or self.cobra.colidiu_com_si_mesma():
                self.estado = "inicio"

        self.gerente.update(delta)

    def desenhar(self):
        self.tela.fill(self.cor_fundo)

        if self.estado == "inicio":
            self.gerente.draw_ui(self.tela)
        elif self.estado == "jogando":
            self.cobra.desenhar(self.tela)
            self.comida.desenhar(self.tela)
            self.desenhar_pontuacao()

        pygame.display.flip()

    def executar(self):
        while self.rodando:
            delta = self.clock.tick(10) / 1000.0
            self.processar_eventos()
            self.atualizar(delta)
            self.desenhar()

        pygame.quit()
