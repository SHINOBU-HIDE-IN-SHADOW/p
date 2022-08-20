import os,pygame,sys
import player
import walllister,world
#######
pygame.display.set_caption("z")
pygame.init()
run = True
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
size = width, height = 500, 500
world_now = world.maps()
screen = pygame.display.set_mode(size)
player1 = player.Player(width, height)
while run == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RIGHT,pygame.K_d):      
                player1.positiontox += player1.speed
            elif event.key in (pygame.K_LEFT,pygame.K_a):
                player1.positiontox1 -= player1.speed
            elif event.key in (pygame.K_UP,pygame.K_w):
                player1.positiontoy1 -= player1.speed
            elif event.key in (pygame.K_DOWN,pygame.K_s):
                player1.positiontoy += player1.speed
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_RIGHT,pygame.K_d):
                player1.positiontox = 0
            elif event.key in (pygame.K_LEFT,pygame.K_a):
                player1.positiontox1 = 0
            elif event.key in (pygame.K_DOWN,pygame.K_s):
                player1.positiontoy = 0
            elif event.key in (pygame.K_UP,pygame.K_w):
                player1.positiontoy1 = 0
            player1.updateroff()
    player1.playersprite(0.1)
    #######33
    player_rect = player1.a
    player_rect.left = player1.positionx
    player_rect.top = player1.positiony
    player1.positionx += player1.positiontox
    player1.positiony += player1.positiontoy
    player1.positionx += player1.positiontox1
    player1.positiony += player1.positiontoy1
    player1.block(len(world_now.list))
    if player1.positionx < 0:
        player1.positionx = player1.width-100
        player1.moverx -= 1
        world_now.mapchange(player1.moverx,player1.movery)
    elif player1.positionx+player1.a.width-50 > player1.width+30:
        player1.positionx = 0
        player1.moverx += 1
        world_now.mapchange(player1.moverx,player1.movery)    
    elif player1.positiony < -100:
        player1.positiony = player1.height-200
        player1.movery -= 1
        world_now.mapchange(player1.moverx,player1.movery)    
    elif player1.positiony+player1.a.height-30 > player1.height+30:
        player1.positiony = 0
        player1.movery += 1
        world_now.mapchange(player1.moverx,player1.movery)     
    world_now.updater(player1,player_rect,screen)
    screen.blit(player1.texterure,(player1.positionx,player1.positiony)) 
    pygame.display.update()
    
    