import pygame
import pygame_gui

from cobra import Cobra

# inicializando o pygame
pygame.init()

# criação da tela
largura_tela = 800
altura_tela = 800
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption('Jogo da cobrinha')

# criando manager para o pygame_gui
gerente = pygame_gui.UIManager((largura_tela, altura_tela), 'theme.json')

# pinta a tela
# Usa o RGB como padrão 
tela_cor = (93, 101, 209)
tela.fill(tela_cor)

# cobrinha
cobra = Cobra(
    largura_tela / 2 - 50 / 2,
    altura_tela / 2 - 50 / 2,
    50,
    50
)

# criando a cobra na posição inicial
pygame.draw.rect(tela, cobra.cor, [(cobra.x, cobra.y), (cobra.largura, cobra.altura)])
rodando = True

# python_gui elements
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect([(350, 100), (100, 50)]),
    text='Start Game',
    manager=gerente
)

def criar_cobra():
    pygame.draw.rect(tela, cobra.cor, [(cobra.x, cobra.y), (cobra.largura, cobra.altura)])
# enum
# inicio, jogando, fim
estado = 'inicio'
# while <condicao>:
while rodando:
    # passando por todos os eventos
    # dentro do event.get()
    for evento in pygame.event.get():
        gerente.process_events(evento)
        # verifica se o user clicou no fechar
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame_gui.UI_BUTTON_PRESSED:
            if evento.ui_element == start_button:
                estado = 'jogando'
        # verifica se o evento é 'clicar em alguma tecla'
        if evento.type == pygame.KEYDOWN:
            cobra.movimentar(evento.key)
            
    # atualizando a tela
    tela.fill(tela_cor)
    
    if estado == 'jogando':
        criar_cobra()
    
    # estou pedindo para atualizar os elementos do pygame_gui
    if estado == 'inicio':
        gerente.update(1 / 60.0)
        gerente.draw_ui(tela)
    
    pygame.display.flip()

# fechar o pygame
pygame.quit()