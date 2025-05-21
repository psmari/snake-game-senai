import pygame
import pygame_gui

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
largura_cobra = 50
altura_cobra = 50
# centro da tela
x = largura_tela / 2 - largura_cobra / 2
y = altura_tela / 2 - altura_cobra / 2

# criando a cobra na posição inicial
pygame.draw.rect(tela, (0, 0, 0), [(x, y), (largura_cobra, altura_cobra)])
rodando = True

# python_gui elements
start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect([(400, 100), (100, 50)]),
    text='Start Game',
    manager=gerente
)

def criar_cobra():
    pygame.draw.rect(tela, (0, 0, 0), [(x, y), (largura_cobra, altura_cobra)])
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
            print('clicando')
        # verifica se o evento é 'clicar em alguma tecla'
        if evento.type == pygame.KEYDOWN:
            # verifica se clicou na tecla seta para esquerda
            if evento.key == pygame.K_LEFT:
                # diminuindo o valor em 30 da variavel x
                x = x - 30
            # verifica se clicou na tecla seta para direita
            if evento.key == pygame.K_RIGHT:
                # aumentando o valor em 30 da variavel x
                x = x + 30
            # verificando se clicou na tecla para cima
            if evento.key == pygame.K_UP:
                # diminuindo 30 o valor da variavel y
                y = y - 30
            # verificando se a tecla para baixo foi clicada
            if evento.key == pygame.K_DOWN:
                # aumentando 30 o valor da variavel y 
                y = y + 30
            
    # atualizando a tela
    tela.fill(tela_cor)
    
    
    # estou pedindo para atualizar os elementos do pygame_gui
    gerente.update(1 / 60.0)
    gerente.draw_ui(tela)
    
    pygame.display.flip()

# fechar o pygame
pygame.quit()