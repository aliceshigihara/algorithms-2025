import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption('Shooting by Alice')

clock = pygame.time.Clock()

x = 396
y = 597

sentidox = 1
sentidoy = 1

shootarray = []

while True:
    for event in pygame.event.get():
        
        PressingKey = pygame.key.get_pressed()
        
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
        #    PressingKey = pygame.key.get_pressed()
            if PressingKey[pygame.K_SPACE]:
            # definir coordenadas do tiro
                ct = (x+1, y-25)
                pygame.draw.line(screen,(255,255,255),(ct[0],ct[1]),(ct[0],ct[1]-30),width= 10)
                shootarray.append(ct)    
                tiro = True
    
        elif event.type == pygame.KEYUP:
         #    PressingKey = pygame.key.get_pressed()
             if PressingKey[pygame.K_SPACE]:                
                tiro = False

    if PressingKey[pygame.K_UP]:
            y -= 4
    if PressingKey[pygame.K_DOWN]:
            y += 4
    if PressingKey[pygame.K_LEFT]:
            x -= 4
    if PressingKey[pygame.K_RIGHT]:
            x += 4

    #player.x = x
    #player.y = y

    screen.fill("black")  

    player = pygame.draw.circle(screen,"red",[x,y],30,width=50)

#-----------------------------------------------------

# arrumar as bordas da tela depois!!!!!!!!!!!!!!!


    #if player.y > 800 or player.y < 0:
    #    sentidox = -1
    #if player.x > 800 or player.x < 0:
    #    sentidoy = -1
    
    #player.x += 3 * sentidox
    #player.y += 3 * sentidoy

#----------------------------------------------------


    # desenhar os tiros

    #percorre o vetor de tiros
    for ct in shootarray:
        # desenha o tiro
        pygame.draw.line(screen,(255,255,255),(ct[0],ct[1]),(ct[0],ct[1]-30),width= 10)
        

    # mover os tiros para cima
    for i in range(len(shootarray)):
        # move tiro para cima
        tmp = list(shootarray[i])
        tmp[1] -= 9
        shootarray[i] = tuple(tmp)

    pygame.display.flip()

    clock.tick(60)
