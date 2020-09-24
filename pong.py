import pygame

pygame.init()

windsize = windwidth, windheight = 960, 540
screen = pygame.display.set_mode(windsize)
pygame.display.set_caption('Pong')

white = (255, 255, 255)

scoreA = 0
scoreB = 0
clock = pygame.time.Clock()
fps = 60


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, white)
    screen.blit(text, (240,30))
    text = font.render(str(scoreB), 1, white)
    screen.blit(text, (720,30))
    clock.tick(fps)
    pygame.display.update()
    
pygame.quit()
