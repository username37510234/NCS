from tkinter import Y
import pygame

pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 타이틀
pygame.display.set_caption("오래노게임")

# 배경 불러오기
background = pygame.image.load("C:/NCS/Python/util01/background.png")

# 캐릭터 불러오기
character = pygame.image.load("C:/NCS/Python/util01/character.png")
character_size = character.get_rect().size #이미지 크기 구하기
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width- character_width) / 2 # 화면 가로 중간, 초기 가로 위치
character_y_pos = screen_height - character_height # 화면 세로 아래 , 초기 세로 위치

to_x = 0
to_y = 0

#이벤트 루프
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -=1
            elif event.key == pygame.K_RIGHT:
                to_x +=1
            elif event.key == pygame.K_UP:
                to_y -=1
            elif event.key == pygame.K_DOWN:
                to_y +=1
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    # x축
    character_x_pos += to_x
    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos>screen_width-character_width:
        character_x_pos = screen_width-character_width
        
    # y축
    character_y_pos += to_y
    if character_y_pos<0:
        character_y_pos = 0
    elif character_y_pos>screen_height-character_height:
        character_y_pos = screen_height-character_height
    
    screen.blit(background, (0,0)) # 배경 불러오기
    
    screen.blit(character, (character_x_pos,character_y_pos))
    
    pygame.display.update() # 화면 다시 불러오기
# pygame 종료
pygame.quit()