import pygame

pygame.init()

# 화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width,screen_height))

# 타이틀
pygame.display.set_caption("오래노게임")

background = pygame.image.load("C:/NCS/Python/util01/background.png")

#이벤트 루프
running =True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # screen.fill((0,0,255)) # 화면 색으로 채우기
    screen.blit(background, (0,0)) # 배경 불러오기
    
    pygame.display.update() # 화면 다시 불러오기
# pygame 종료
pygame.quit()