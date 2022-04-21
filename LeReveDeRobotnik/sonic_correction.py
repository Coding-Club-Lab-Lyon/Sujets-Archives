import pygame

def handleParallax(window, background, pos_x, speed):
    window.blit(background, (pos_x, 0))
    window.blit(background, (pos_x + 1200, 0))
    if (pos_x <= -1200):
        pos_x = 0
    pos_x -= speed
    return pos_x

def loop_game(window):
    end = False
    bg_1 = pygame.image.load("resources/background_front.png")
    bg_1_pos_x = 0
    bg_2 = pygame.image.load("resources/background_middle.png")
    bg_2_pos_x = 0
    bg_3 = pygame.image.load("resources/background_fix.png")

    sonic = pygame.image.load("resources/sonic.png")
    rect = pygame.Rect(1050, 0, 175, 175)
    speed = 0
    position = 14

    while (end == False):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = True
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            if position < 14:
                rect.left += 175
                if rect.left > 700:
                    rect.left = 0
                speed = 1
                position += 1
            elif (position < 25):
                rect.top = 350
                rect.left += 175
                if rect.left > 525:
                    rect.left = 0
                speed = 3
            else:
                rect.top = 525
                rect.left += 175
                if rect.left > 525:
                    rect.left = 0   
                speed = 3
            if key_pressed[pygame.K_a]:
                speed *= 2
                position = 25
            elif (position >= 14):
                position = 14
        else:
            rect.top = 0
            rect.left += 175
            if rect.left > 525:
                rect.left = 0   
            speed = 1
        window.blit(bg_3, (0, 0))
        bg_2_pos_x = handleParallax(window, bg_2, bg_2_pos_x, 4 * speed)
        window.blit(sonic, (350, 410), rect)
        bg_1_pos_x = handleParallax(window, bg_1, bg_1_pos_x, 8 * speed)
        pygame.display.update()
        window.fill((0, 0, 0))
        pygame.time.Clock().tick(90)

def setup_window():
    window = pygame.display.set_mode((1200, 600))
    pygame.display.set_caption("Le Rêve de Robotnik")
    return (window)

def main():
    pygame.init()
    window = setup_window()
    loop_game(window)

if __name__ == "__main__":
    main()