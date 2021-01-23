import pygame

pygame.init() #to reset pygame

#frame size
screen_width = 720 
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

#title
pygame.display.set_caption("mage")

#background image
background = pygame.image.load("/Users/echo/Desktop/공부/python_workspace/pygame_basic/background.png")

#character
character = pygame.image.load("/Users/echo/Desktop/공부/python_workspace/pygame_basic/character.jpg")
character_size = character.get_rect().size #image size
character_width = character_size[0]
character_height = character_size[1]
character_x_position = screen_width / 2 -35 #화면 가로의 절반 나눈 곳에 위치
character_y_position = screen_height - character_height # 화면 세로 크기 아래 해당하는 위치


#moving 
to_x = 0
to_y = 0

#event loop
running = True 
while running:
    for event in pygame.event.get(): #check event
        if event.type == pygame.QUIT: #window close
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= 5 
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygane.K_DOWN:
                to_y += 5
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
    
    character_x_position += to_x
    character_y_position += to_y


    screen.blit(background, (0,0))
    screen.blit(character, (character_x_position, character_y_position))


    pygame.display.update() 

#exit
pygame.quit()
