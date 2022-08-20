import os,pygame,sys
import player
import wall,walllister
#######
pygame.display.set_caption("z")
pygame.init()
run = True
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")
size = width, height = 500, 500
screen = pygame.display.set_mode(size)
background = pygame.image.load(os.path.join(image_path, "background.png"))
player1 = player.Player(width, height)
wallist = walllister.wall()
for x in range(3):
    wall1 = wall.wall(50*x,120*x)
    wallist.appender(wall1)
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
            player1.block()
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
    screen.blit(background, (0, 0))
    for wall1 in wallist.list:
        player1.blocker(player_rect,wall1.rect)
    # if player1.a.colliderect(ball_rect):
    #         if player_rect.left == ball_rect.right-2:
    #             player1.positionx+=2
    #         elif player_rect.right == ball_rect.left+1:
    #             player1.positionx-=1
    #         elif player_rect.bottom == ball_rect.top+1:
    #             player1.positiony-=1
    #         elif player_rect.top == ball_rect.bottom-2:
    #             player1.positiony+=2  
    for wall1 in wallist.list:
        screen.blit(wall1.wall, (wall1.x,  wall1.y))
    player1.positionx += player1.positiontox
    player1.positiony += player1.positiontoy
    player1.positionx += player1.positiontox1
    player1.positiony += player1.positiontoy1
    screen.blit(player1.texterure,(player1.positionx,player1.positiony)) 
    player1.block()
    pygame.display.update()
    
    