import os
import random
import pygame
# (0)필수요소
pygame.init() 
# a.게임 스크린 크기 설정
screen_width = 450 
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
#b.게임 이름
pygame.display.set_caption("shootgame")
# fps
clock = pygame.time.Clock()
###########################

# (1) 사용자 게임 설정 - 배경화면 , 게임 안 이미지들 , 좌표 , 속도, 폰트 등
current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path, "images")

background = pygame.image.load(os.path.join(image_path, "background.jpg"))

stage = pygame.image.load(os.path.join(image_path, "stage.jpg"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]

character = pygame.image.load(os.path.join(image_path, "character.jpg"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
character_to_x = 0
character_speed = 5

enemy = pygame.image.load(os.path.join(image_path, "enemy.jpg"))
enemy_size = character.get_rect().size
enemy_width = character_size[0]
enemy_height = character_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 10
enemy_to_remove = -1

weapons = []
weapon = pygame.image.load(os.path.join(image_path, "weapon.jpg"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
weapon_speed = 10
weapon_to_remove = -1
weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
weapon_y_pos = character_y_pos

game_font = pygame.font.Font(None, 40)
start_ticks = pygame.time.get_ticks()
game_result = "game over"

run = True

while run:
    dt = clock.tick(60) #현재 프레임 결정
    #print ("fps:", str(clock.get_fps()))
    #(2)) 게임 캐릭터들 위치 선정 
    character_x_pos += character_to_x

    if character_x_pos < 0 :
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width :
        character_x_pos = screen_width - character_width
    
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons]

    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0]

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enmey_x_pos = random.randint(0, screen_width-enemy_width)
    
    # (4) 이벤트 처리(키보드 입력, 게임 실행 등)
    for event in pygame.event.get():
            if event.type == pygame.QUIT: # x 버튼으로 나갔을 때 끝내기
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_KP_4:
                     character_to_x -= character_speed
                elif event.type == pygame.K_KP_8:
                    character_to_x += character_speed
                elif event.type == pygame.K_SPACE:
                    weapon_x_pos = character_x_pos + (character_width / 2) - (weapon_width / 2)
                    weapon_y_pos = character_y_pos
                    weapons.append([weapon_x_pos, weapon_y_pos])
           
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_KP_4 or event.key == pygame.K_KP_8:
                    character_to_x = 0
             #(3)) 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    weapon_rect = weapon.get_rect()
    weapon_rect.left = weapon_x_pos
    weapon_rect.top = weapon_y_pos

    if character_rect.colliderect(enemy_rect):
        game_result = "game over"
        run = False
        break
    
    for weapon_idx, weapon_val in enumerate(weapons):
        weapon_pos_x = weapon_val[0]
        weapon_pos_y = weapon_val[1]

    if weapon_rect.colliderect(enemy_rect):
        weapon_to_remove = weapon_idx
        enemy_to_remove = -1
        break
            
    # (5)화면에 출력하기
    
    screen.blit(background,(0,0))
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapons,(weapon_x_pos, weapon_y_pos))
    screen.blit(stage , (0, screen_height - stage_height))
    screen.blit(character,(character_x_pos, character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    time = (pygame.time.get_ticks()) / 1000
    timer = game_font.render("time: {}".format(time), True,(255,255,255) ),
    screen.blit(timer, (10,10))
    
    pygame.display.update()# 없으면 화면이 출력 안됌

msg = game.font.render(game_result,True, (255,255,0))
msg_rect = msg.get_rect(center=(int(screen_width/ 2), int(screen_height / 2)))
screen.blit(msg,msg_rect)
pygame.display.update()
pygame.time.delay (2000)

pygame.quit() #나가기 함수 호출