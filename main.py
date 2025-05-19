import pygame

# inicializando o pygame
pygame.init()

# criação da tela
tela = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Jogo da cobrinha')

tela.fill((93, 101, 209))

rodando = True
# while <condicao>:
while rodando:
    # passando por todos os eventos
    # dentro do event.get()
    for evento in pygame.event.get():
        # verifica se o user clicou no fechar
        if evento.type == pygame.QUIT:
            rodando = False
    
    pygame.draw.circle(tela, (0, 0, 0), (400, 400), 40)
    pygame.draw.rect(tela, (0, 0, 0), [(200, 200), (10, 10)])
    
    # atualizando a tela
    pygame.display.flip()

# fechar o pygame
pygame.quit()