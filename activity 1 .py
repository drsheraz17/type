import pygame
#intialize required modules
pygame.init()

#setup window geometry
screen=pygame.display.set_mode((400,500))

#create a loop to run the game till the user quits
done=False

while not done:

    #clear the event queue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

            #make the changes visible
            pygame.display.flip


