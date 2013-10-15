import pygame
import random
from flyobj import *
from config import *

CRASH_DIST = 7
OUT_DIST = 1000

def main():
    cfg = Config()

    r_min = 9999.0
    r_max = 0.0

    #PyGame init
    pygame.init() 
    screen = pygame.display.set_mode(cfg.getDisplay()) 
    pygame.display.set_caption("Solar Mechanics") 
#    pygame.display.toggle_fullscreen()
    
    #Space init
    bg = Surface(cfg.getDisplay()) 
    bg.fill(Color(cfg.getSpaceColor()))  
    #Draw fixed stars   
    for i in range(cfg.getStarNumber()):
        draw.circle (bg, Color(random.sample(cfg.getStarColors(), 1)[0]), 
            (random.randrange(cfg.getWidth()), 
             random.randrange(cfg.getHeight())), 
            0)
                    
    #Timer init                     
    timer = pygame.time.Clock()

    #Solar system init
    system = cfg.getSystem()

    
    done = False
    paused = False
    while not done: 
        timer.tick(60)
        for e in pygame.event.get(): 
            if e.type == QUIT:
                done = True
                break        
            if e.type == KEYDOWN:
                if e.key == K_q or e.key == K_ESCAPE:
                    done = True
                    break        
                if e.key == K_p or e.key == K_SPACE:
                    paused = not paused
                if e.key == K_f:
                    pygame.display.toggle_fullscreen()

        if not paused:
            for i in system:
                for j in system:
                    if (i != j):
                        dist = i.dist(j)
                        i.calcAccelTo(j)
                        r_min = min (r_min, dist)
                        r_max = max (r_min, dist)
   

            for i in system:
                i.update()

            #Put space to screen
            screen.blit(bg, (0, 0))      

            #Put each object to screen
            for i in system:
                i.draw(screen)

            #update screen
            pygame.display.update()     

            if r_min < CRASH_DIST:
                done = True
                print("Collision detected")
                break
            if r_max > OUT_DIST:
                done = True
                print("Out of system")
                break

    #Farewell
    print (":-)")


if __name__ == "__main__":
    main()

