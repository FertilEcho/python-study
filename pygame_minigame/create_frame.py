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

#이벤트루프
running = True 
while running:
    for event in pygame.event.get(): #check event
        if event.type == pygame.QUIT: #when window closed
            running = False



# 종료
pygame.quit()
