import pygame

pygame.init() #to reset pygame

#frame size
screen_width = 720 
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

#title
pygame.display.set_caption("MINI GAME")

#background image
background = pygame.image.load("/Users/echo/Desktop/공부/python_workspace/pygame_basic/background.png")

#event loop
running = True 
while running:
    for event in pygame.event.get(): #이벤트 발생 체크
        if event.type == pygame.QUIT: #창이 닫혔을 때
            running = False

    screen.blit(background, (0,0))

    pygame.display.update() #게임화면 다시 그리기


# 종료
pygame.quit()
