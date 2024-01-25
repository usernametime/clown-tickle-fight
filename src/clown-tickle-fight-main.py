import random
import pygame
import clown

from pygame.locals import *

joysticks = {}

x = 200
y = 200

b_x = 400
b_y = 400

width  = 20
height = 20

def main():
    # Initialise win
    pygame.init()
    win = pygame.display.set_mode((500, 500))
    screen_rect = pygame.Rect((0, 0), (500, 500))
    pygame.display.set_caption("Clown Tickle Fight")

    # Fill background
    background = pygame.Surface(win.get_size())
    background = background.convert()
    background.fill((0, 0, 0))

    # Initialise players
    global player1
    global player2
    p1_img = "clown1.png"    
    p2_img = "clown1.png"
    player1 = clown.Clown("left", p1_img)
    player2 = clown.Clown("right", p2_img)

    # Initialise sprites
    playersprites = pygame.sprite.RenderPlain((player1, player2))

    pygame.display.flip()

    clock = pygame.time.Clock()
    FPS = 60
    # Event loop
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    player1.moveup(True)
                if event.key == K_a:
                    player1.moveleft(True)
                if event.key == K_s:
                    player1.movedown(True)
                if event.key == K_d:
                    player1.moveright(True)
                if event.key == K_UP:
                    player2.moveup(True)
                if event.key == K_DOWN:
                    player2.movedown(True)
                if event.key == K_LEFT:
                    player2.moveleft(True)
                if event.key == K_RIGHT:
                    player2.moveright(True)
            elif event.type == KEYUP:
                if event.key == K_w:
                    player1.moveup(False)
                if event.key == K_a:
                    player1.moveleft(False)
                if event.key == K_s:
                    player1.movedown(False)
                if event.key == K_d:
                    player1.moveright(False)
                if event.key == K_UP:
                    player2.moveup(False)
                if event.key == K_DOWN:
                    player2.movedown(False)
                if event.key == K_LEFT:
                    player2.moveleft(False)
                if event.key == K_RIGHT:
                    player2.moveright(False)

        player1.rect.clamp_ip(screen_rect)
        player2.rect.clamp_ip(screen_rect)
        win.blit(background, player1.rect, player1.rect)
        win.blit(background, player2.rect, player2.rect)
        playersprites.update()
        playersprites.draw(win)
        pygame.display.flip()
        
    pygame.quit()

# run = True

# while run:
#     pygame.time.delay(10)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT] and x > 0:
#         x -= vel
#     if keys[pygame.K_RIGHT] and x < 500 - width:
#         x += vel        
#     if keys[pygame.K_UP] and  y > 0:
#         y -= vel
#     if keys[pygame.K_DOWN] and y < 500 - height:
#         y+= vel
#     if keys[pygame.K_a] and b_x > 0:
#         b_x -= vel
#     if keys[pygame.K_d] and b_x < 500 - width:
#         b_x += vel        
#     if keys[pygame.K_w] and  b_y > 0:
#         b_y -= vel
#     if keys[pygame.K_s] and b_y < 500 - height:
#         b_y+= vel     
        
        
    # win.fill((0,0,0))
    
    # pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    # pygame.draw.rect(win, (0, 0, 255), (b_x,b_y,width, height))
    # pygame.display.update()

if __name__ == "__main__":
    main()