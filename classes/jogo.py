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
        self.nome_jogador = ""

        self.botao_iniciar = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(((self.largura - 200) // 2, (self.altura - 60) // 2), (200, 60)),
            text="Start Game",
            manager=self.gerente,
            object_id="#botao_start"
        )

        self.botao_reiniciar = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(((self.largura - 200) // 2, 500), (200, 60)),
            text="Jogar Novamente",
            manager=self.gerente,
            visible=False,
            object_id="#botao_restart"
        )

        self.caixa_nome = pygame_gui.elements.UITextEntryLine(
            relative_rect=pygame.Rect(((self.largura - 300) // 2, 400), (300, 40)),
            manager=self.gerente,
            visible=False
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

    def salvar_pontuacao(self):
        if self.nome_jogador.strip():
            with open("pontuacoes.txt", "a", encoding="utf-8") as f:
                f.write(f"{self.nome_jogador} - {self.pontuacao} pontos\n")

    def obter_melhores_pontuacoes(self):
        try:
            with open("pontuacoes.txt", "r", encoding="utf-8") as f:
                linhas = f.readlines()
            pontuacoes = []
            for linha in linhas:
                partes = linha.strip().rsplit(" - ", 1)
                if len(partes) == 2:
                    nome, pont = partes
                    try:
                        pont_num = int(pont.replace(" pontos", ""))
                        pontuacoes.append((nome, pont_num))
                    except ValueError:
                        continue
            pontuacoes.sort(key=lambda x: x[1], reverse=True)
            return pontuacoes[:5]
        except FileNotFoundError:
            return []

    def mostrar_game_over(self):
        texto = self.fonte.render("FIM DE JOGO! Digite seu nome:", True, (255, 255, 255))
        self.tela.blit(texto, ((self.largura - texto.get_width()) // 2, 350))
        texto_pontuacao = self.fonte.render(f"Pontuação: {self.pontuacao}", True, (255, 255, 255))
        self.tela.blit(texto_pontuacao, ((self.largura - texto_pontuacao.get_width()) // 2, 300))

        melhores = self.obter_melhores_pontuacoes()
        y_base = 100
        titulo = self.fonte.render("Top 5 Pontuações:", True, (255, 255, 255))
        self.tela.blit(titulo, ((self.largura - titulo.get_width()) // 2, y_base))

        for i, (nome, pontos) in enumerate(melhores):
            texto_ranking = self.fonte.render(f"{i+1}. {nome} - {pontos} pontos", True, (255, 255, 255))
            self.tela.blit(texto_ranking, ((self.largura - texto_ranking.get_width()) // 2, y_base + 40 * (i + 1)))

    def processar_eventos(self):
        for evento in pygame.event.get():
            self.gerente.process_events(evento)

            if evento.type == pygame.QUIT:
                self.rodando = False

            elif evento.type == pygame_gui.UI_BUTTON_PRESSED:
                if evento.ui_element == self.botao_iniciar:
                    self.estado = "jogando"
                    self.reiniciar()
                    self.botao_iniciar.hide()

                elif evento.ui_element == self.botao_reiniciar:
                    self.nome_jogador = self.caixa_nome.get_text()
                    self.salvar_pontuacao()
                    self.estado = "jogando"
                    self.reiniciar()
                    self.caixa_nome.hide()
                    self.botao_reiniciar.hide()

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

            if cabeca.colliderect(comida_rect):
                self.cobra.crescer()
                self.comida.gerar_nova()
                self.pontuacao += 1

            if self.cobra.colidiu_com_parede(self.largura, self.altura) or self.cobra.colidiu_com_si_mesma():
                self.estado = "game over"
                self.caixa_nome.show()
                self.botao_reiniciar.show()

        self.gerente.update(delta)

    def desenhar(self):
        self.tela.fill(self.cor_fundo)

        if self.estado == "inicio":
            self.gerente.draw_ui(self.tela)

        elif self.estado == "jogando":
            self.cobra.desenhar(self.tela)
            self.comida.desenhar(self.tela)
            self.desenhar_pontuacao()

        elif self.estado == "game over":
            self.mostrar_game_over()
            self.gerente.draw_ui(self.tela)

        pygame.display.flip()

    def executar(self):
        while self.rodando:
            delta = self.clock.tick(10) / 1000.0
            self.processar_eventos()
            self.atualizar(delta)
            self.desenhar()

        pygame.quit()
