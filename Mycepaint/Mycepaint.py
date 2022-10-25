import pygame, time

pygame.init()

WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
RED = [255, 0, 0] 
GREEN = [0, 255, 0]
BLUE = [0, 0, 255]

window = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Myce Paint")
leave = False
window.fill(WHITE)

def color():
    

while not leave:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            leave = True
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_ESCAPE:
                leave = True
    if pygame.mouse.get_pressed()[0]:
        pos_x, pos_y = pygame.mouse.get_pos()
        pygame.draw.aaline(window, BLACK, [pos_x - 1, pos_y - 1], [pos_x, pos_y])
    pygame.display.update()

pygame.quit()
quit