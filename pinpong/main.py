import sys,pygame
pygame.init()
pygame.display.set_caption("PinPong")
size = width, height = 320, 240
black = 0, 0, 0
font = pygame.font.Font("7_Emulogic.ttf", 25)
mine23 = pygame.image.load('scr/mine.png')
screen = pygame.display.set_mode(size)
pygame.display.set_icon(mine23)
# sound = pygame.mixer.Sound('pinpong/a.wav')
sound = pygame.mixer.Sound('a.wav')
speed = 0.1
movespeedp =0
movespeedm = 0
movespeedp1 =0
movespeedm1 = 0
time = pygame.time.Clock()
mainstart = pygame.USEREVENT
pygame.time.set_timer(mainstart,1200)
ballx,bally = width/2, height/2
ball_speedx= 0.05
ball_speedy= 0.05
scorep1=0
scorep2=0
scorey= height/10
scorex1=width/2- 75
scorex2= width/2+50
move =2
move1 =2
balls = False
startclicked = False
run = True
clicktext = ""
gamenow = "main"
def key():
    starfont = pygame.font.Font("7_Emulogic.ttf", 12)
    keytutor1 = starfont.render("Player1: W,S",0,(255,255,255))
    keytutor2 = starfont.render("Player2: UP KEY, DOWN KEY",0,(255,255,255))
    screen.blit(keytutor1,(0, height/2))
    screen.blit(keytutor2,(0, height/2-15))
def wallmover():
    global move,p1,p2,move1
    if move<0:
        move = 0
    elif move>height-50:
        move=height-50
    if move1<0:
        move1 = 0
    elif move1>height-50:
        move1=height-50
    p1=pygame.draw.rect(screen, (255,255,255), [width/100, move, width/100, height/4])
    p2=pygame.draw.rect(screen, (255,255,255), [width-p1.right, move1, width/100, height/4])
def ball():
    global ballx,bally,ball_speedx,ball_speedy,scorep1,scorep2
    if balls == True:
        ballx +=ball_speedx
        bally += ball_speedy
    ball = pygame.draw.circle(screen, (255,255,255), [ballx,bally], width/70)
    if p1.colliderect(ball) or p2.colliderect(ball):
        if ball.bottom == p1.top+1  or ball.top == p1.bottom-1:
            ball_speedy = -ball_speedy
        if ball.bottom == p2.top+1  or ball.top == p2.bottom-1:
            ball_speedy = -ball_speedy
        if p1.colliderect(ball):
            ballx = p1.right+5
            ball_speedx = -ball_speedx
        elif p2.colliderect(ball):
            ballx = p2.left-5
            ball_speedx = -ball_speedx
        if ball_speedx >0:
            ball_speedx += 0.005
        else:
            ball_speedx -= 0.005
        if ball_speedy>0:
            ball_speedy += 0.005
        else:
            ball_speedx -= 0.005 
        sound.play()
    if bally>height or bally<0:
        ball_speedy = -ball_speedy
    if ballx<0:
        scorep2 += 1 
        reset()
    elif ballx>width:
        scorep1 +=1
        reset()
def score():
    p1s = font.render(str(scorep1),0,(255,255,255))
    p2s = font.render(str(scorep2),0,(255,255,255))
    screen.blit(p1s,(scorex1,scorey))
    screen.blit(p2s,(scorex2,scorey))
    pygame.draw.line(screen, (255,255,255), [width/2, 0], [width/2,height], 1)
def reset():
    global ballx,bally,balls,ball_speedx,ball_speedy
    ballx,bally = width/2, height/2
    balls = False
    ball_speedx= 0.05
    ball_speedy= 0.05
def main_menu():
    global gamenow,clicktext
    mainfont = pygame.font.Font("7_Emulogic.ttf", 40)
    mainfont1 = pygame.font.Font("7_Emulogic.ttf", 15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            gamenow = "game"
        if event.type == mainstart:
            sound.play()
            if clicktext == "":
                clicktext = "CLICK TO START"
            else:
                clicktext = ""


    screen.fill(black)
    a =mainfont.render("PingPong",0,(255,255,255))
    clicks = mainfont1.render(str(clicktext),0,(255,255,255))
    screen.blit(a,(-2,bally/2))
    screen.blit(clicks,(width/5.8,height/2+height/3))
    time.tick(120)
def game():
    global startclicked,balls,move,movespeedp,movespeedm,ball_speedx,ball_speedy,move1,movespeedp1,movespeedm1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w :
                movespeedp -= speed
            elif event.key == pygame.K_s:
                movespeedm += speed
            if event.key == pygame.K_UP:
                movespeedp1 -= speed
            elif event.key == pygame.K_DOWN:
                movespeedm1 += speed
            if balls == False:
                startclicked = True
                balls = True
                ball_speedx = -ball_speedx
                ball_speedy = ball_speedy
            if event.key == pygame.K_r:
                reset()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                movespeedp1 = 0
            if event.key == pygame.K_DOWN:
                movespeedm1 = 0
            if event.key == pygame.K_w:
                movespeedp = 0
            if event.key == pygame.K_s:
                movespeedm = 0
    move+=movespeedp
    move+=movespeedm
    move1+=movespeedp1
    move1+=movespeedm1
    screen.fill(black)
    wallmover()
    ball()
    score()
while run:
    if gamenow == "main":
        main_menu()
    elif gamenow == "game":
        game()
        if startclicked == False:
            key()
    pygame.display.flip()
        