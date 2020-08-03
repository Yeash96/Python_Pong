
import pygetwindow as gw


print(" () ()")
print("<('w')>")

# Yo



import pygame

from modules import Player


def main():
    pygame.init()
    p1 = Player(0, boardDim=(960,540))
    p2 = Player(1, boardDim=(960,540))



    gameLoop = True
    fps = 60
    p_Speed = 12

    clock = pygame.time.Clock()

    
    pygame.display.set_caption( "Player Test" ) 
    win_W, win_H = 960, 540 
    window = pygame.display.set_mode( (win_W, win_H) )
    
    player_Group = pygame.sprite.Group()
    player_Group.add(p1)
    player_Group.add(p2)

    while gameLoop:
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            p1.move(-p_Speed)
        elif pressed[pygame.K_s]:
            p1.move(p_Speed)
        if pressed[pygame.K_UP]:
            p2.move(-p_Speed)
        elif pressed[pygame.K_DOWN]:
            p2.move(p_Speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT : 
                gameLoop = False
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_w:
            #         p1.move(-10)
            #     if event.key == pygame.K_s:
            #         p1.move(10)
            #     if event.key == pygame.K_UP:
            #         p2.move(-10)
            #     if event.key == pygame.K_DOWN:
            #         p2.move(10)
        
        
        player_Group.draw(window)
        pygame.display.update()
        window.fill(pygame.Color(0,0,0))

        clock.tick(fps)

        
    pygame.quit




if __name__ == '__main__':
    main()