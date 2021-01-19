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

#character
character = pygame.image.load("/Users/echo/Desktop/공부/python_workspace/pygame_basic/character.jpg")
character_size = character.get_rect().size #image size
character_width = character_size[0]
character_height = character_size[1]
character_x_position = screen_width / 2 -35 #화면 가로의 절반 나눈 곳에 위치
character_y_position = screen_height - character_height # 화면 세로 크기 아래 해당하는 위치

#event loop
running = True 
while running:
    for event in pygame.event.get(): #이벤트 발생 체크
        if event.type == pygame.QUIT: #창이 닫혔을 때
            running = False


    screen.blit(background, (0,0))
    screen.blit(character, (character_x_position, character_y_position))


    pygame.display.update() #게임화면 다시 그리기

# 종료
pygame.quit()
