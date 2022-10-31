from cProfile import run
from random import randrange
import pygame

pygame.init()

screen_width = 480
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("오래노똥피하기")

clock = pygame.time.Clock()

background = pygame.image.load("C:/NCS/Python/util01/background.png")

character = pygame.image.load("C:/NCS/Python/util01/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width-character_width) /2
character_y_pos = 538

to_x = 0
to_y = 0

character_speed = 0.5


ddong = pygame.image.load("C:/NCS/Python/util01/ddong.png")
ddong_size = ddong.get_rect().size
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = randrange(ddong_width,screen_width-ddong_width)
ddong_y_pos = 0
ddong_speed = 0.2

ddong2 = pygame.image.load("C:/NCS/Python/util01/ddong.png")
ddong2_size = ddong2.get_rect().size
ddong2_width = ddong2_size[0]
ddong2_height = ddong2_size[1]
ddong2_x_pos = randrange(ddong2_width,screen_width-ddong2_width)
ddong2_y_pos = -200
ddong2_speed = 0.25

ddong3 = pygame.image.load("C:/NCS/Python/util01/ddong.png")
ddong3_size = ddong3.get_rect().size
ddong3_width = ddong3_size[0]
ddong3_height = ddong3_size[1]
ddong3_x_pos = randrange(ddong3_width,screen_width-ddong3_width)
ddong3_y_pos = -1000
ddong3_speed = 0.3

ddong4 = pygame.image.load("C:/NCS/Python/util01/ddong.png")
ddong4_size = ddong4.get_rect().size
ddong4_width = ddong4_size[0]
ddong4_height = ddong4_size[1]
ddong4_x_pos = randrange(ddong4_width,screen_width-ddong4_width)
ddong4_y_pos = -500
ddong4_speed = 0.2

ddong5 = pygame.image.load("C:/NCS/Python/util01/ddong.png")
ddong5_size = ddong5.get_rect().size
ddong5_width = ddong5_size[0]
ddong5_height = ddong5_size[1]
ddong5_x_pos = randrange(ddong5_width,screen_width-ddong5_width)
ddong5_y_pos = -1500
ddong5_speed = 0.25

game_font = pygame.font.Font(None,40)

total_time = 30

start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                
    character_x_pos += to_x * dt
    if character_x_pos<0:
        character_x_pos = 0
    elif character_x_pos>screen_width-character_width:
        character_x_pos = screen_width-character_width
        
    ddong_y_pos += ddong_speed * dt
    if ddong_y_pos>538-ddong_height+character_height:
        ddong_y_pos = 0
        ddong_x_pos = randrange(ddong_width,screen_width-ddong_width)
        
    ddong2_y_pos += ddong2_speed * dt
    if ddong2_y_pos>538-ddong2_height+character_height:
        ddong2_y_pos = 0
        ddong2_x_pos = randrange(ddong2_width,screen_width-ddong2_width)
        
    ddong3_y_pos += ddong3_speed * dt
    if ddong3_y_pos>538-ddong3_height+character_height:
        ddong3_y_pos = 0
        ddong3_x_pos = randrange(ddong3_width,screen_width-ddong3_width)
        
    ddong4_y_pos += ddong4_speed * dt
    if ddong4_y_pos>538-ddong4_height+character_height:
        ddong4_y_pos = 0
        ddong4_x_pos = randrange(ddong4_width,screen_width-ddong4_width)
        
    ddong5_y_pos += ddong5_speed * dt
    if ddong5_y_pos>538-ddong5_height+character_height:
        ddong5_y_pos = 0
        ddong5_x_pos = randrange(ddong5_width,screen_width-ddong5_width)
        
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos
    
    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos
    
    ddong2_rect = ddong2.get_rect()
    ddong2_rect.left = ddong2_x_pos
    ddong2_rect.top = ddong2_y_pos
    
    ddong3_rect = ddong3.get_rect()
    ddong3_rect.left = ddong3_x_pos
    ddong3_rect.top = ddong3_y_pos
    
    ddong4_rect = ddong4.get_rect()
    ddong4_rect.left = ddong4_x_pos
    ddong4_rect.top = ddong4_y_pos
    
    ddong5_rect = ddong5.get_rect()
    ddong5_rect.left = ddong5_x_pos
    ddong5_rect.top = ddong5_y_pos
    
    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False
    
    if character_rect.colliderect(ddong2_rect):
        print("충돌했어요")
        running = False
    
    if character_rect.colliderect(ddong3_rect):
        print("충돌했어요")
        running = False
    
    if character_rect.colliderect(ddong4_rect):
        print("충돌했어요")
        running = False
    
    if character_rect.colliderect(ddong5_rect):
        print("충돌했어요")
        running = False
        
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos,character_y_pos))
    screen.blit(ddong, (ddong_x_pos,ddong_y_pos))
    screen.blit(ddong2, (ddong2_x_pos,ddong2_y_pos))
    screen.blit(ddong3, (ddong3_x_pos,ddong3_y_pos))
    screen.blit(ddong4, (ddong4_x_pos,ddong4_y_pos))
    screen.blit(ddong5, (ddong4_x_pos,ddong5_y_pos))
    
    elapsed_time = (pygame.time.get_ticks() - start_ticks) /1000
    timer = game_font.render(str(int(total_time-elapsed_time)), True, (255,255,255))
    screen.blit(timer, (10,10))
    if timer == 0:
        print("승리했어요")
        running = False 
    pygame.display.update()
    
pygame.quit()