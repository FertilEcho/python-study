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
character = pygame.image.load("/Users/echo/Desktop/공부/python_workspace/pygame_basic/character.png")
character_size = character.get_rect().size #image size
character_width = character_size[0]
character_height = character_size[1]
character_x_position = screen_width / 2 -35 
character_y_position = screen_height - character_height 

#event loop
running = True 
while running:
    for event in pygame.event.get(): #Check event
        if event.type == pygame.QUIT: #close the window
            running = False


    screen.blit(background, (0,0))
    screen.blit(character, (character_x_position, character_y_position))


    pygame.display.update() 

#exit
pygame.quit()
