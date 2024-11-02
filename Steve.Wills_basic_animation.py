# Steve Wills
# Basic Animation
# 11/1/24

import pygame

def main():
    pygame.init()
    
    #display
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Where's The Targaryen's?!")
    
    #entities
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill("papayawhip")
    
    dragon = pygame.image.load("dragon.png")
    dragon = dragon.convert_alpha()
    dragon = pygame.transform.scale(dragon, (100, 100))
    dragon_x = 0
    dragon_y = 240
    
# Action
    #assign
    clock = pygame.time.Clock()
    keepGoing = True
    #loop
    while keepGoing:
        #timer
        clock.tick(30)
        #events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        #modify the box!
        dragon_x += 5
        dragon_y += 5
        #check bounds
        if dragon_x > screen.get_width():
            dragon_x = 0
        if dragon_y > screen.get_height():
            dragon_y = 0
        
        #refresh
        screen.blit(background, (0 ,0))
        screen.blit(dragon, (dragon_x, dragon_y))
        pygame.display.flip()
        
    pygame.quit()
    
    
            
if __name__ == "__main__":
    main()