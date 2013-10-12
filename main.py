import pygame
import random
from flyobj import *

WIN_WIDTH = 800 
WIN_HEIGHT = 640 
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) 
SPACE_COLOR = "#000022"
SUN_COLOR = "yellow"

R=5
STAR_NUM = 400
STAR_COLORS = ["blue", "brown", "grey", "magenta"]

#Stop conditions
CRASH_DIST = 10
OUT_DIST = 1000

def main():
#    sun = FlyObject("Sun", 2000, 500, 320, -0.0, -0.0)
#    earth = FlyObject("Earth", 200, 300.0, 320.0, 0.0, 2.0)
#    mars = FlyObject("Mars", 200, 700.0, 320.0, 0.0, -2.0)

    sun = FlyObject("Sun", 4000, 500, 320, -0.0, -0.0)
    earth = FlyObject("Earth", 50, 100.0, 320.0, 0.1, 1.5)
    mars = FlyObject("Mars", 30, 300.0, 320.0, 0.0, 1.9)


#    sun = FlyObject("Sun", 4000, 400, 320, -0.0, -0.0)
#    earth = FlyObject("Earth", 1, 100.0, 290.0, 0.1, 1.5)

#    sun = FlyObject("Sun", 2000, 500, 320, -0.0, -1.0)
#    earth = FlyObject("Earth", 2000, 300.0, 320.0, 0.0, 1.0)

#    sun = FlyObject("Sun", 3000, 500, 320, -0.0, -2.7)
#    earth = FlyObject("Earth", 3000, 300.0, 320.0, 0.0, 2.7)

#    sun = FlyObject("Sun", 10000, 500, 320, -0.0, -0.0)
#    earth = FlyObject("Earth", 500, 300.0, 320.0, 0.0, 2.7)

#    sun = FlyObject("Sun", 10000, 500, 320, -0.0, -0.0)
#    earth = FlyObject("Earth", 500, 300.0, 320.0, 0.0, 4.7)

#    sun = FlyObject("Sun", 1000, 500, 320, -0.0, -0.2)
#    earth = FlyObject("Earth", 500, 300.0, 320.0, 0.0, 1.7)


    #PyGame init
    pygame.init() 
    screen = pygame.display.set_mode(DISPLAY) 
    pygame.display.set_caption("Space Dynamics") 
    
    #Space init
    bg = Surface((WIN_WIDTH,WIN_HEIGHT)) 
    bg.fill(Color(SPACE_COLOR))  
    #Draw fixed stars   
    for i in range(STAR_NUM):
        draw.circle (bg, Color(random.sample(STAR_COLORS, 1)[0]), 
            (random.randrange(WIN_WIDTH), random.randrange(WIN_HEIGHT)), 
            0)
                    
    #Timer init                     
    timer = pygame.time.Clock()
    
    #Planet init
    earth.initSurface(R, "blue", SPACE_COLOR)
    mars.initSurface(R, "red", SPACE_COLOR)

    #Sun init
    sun.initSurface(R*2, SUN_COLOR, SPACE_COLOR)

    done = False
    while not done: 
        timer.tick(60)
        for e in pygame.event.get(): 
            if e.type == QUIT:
                done = True
                break        
        
        r1 = sun.dist(earth)
        r2 = sun.dist(mars)
        r3 = earth.dist(mars)

        #Caluculate acceleration between objects
        sun.calcAccelTo(earth)
        sun.calcAccelTo(mars)
        earth.calcAccelTo(sun)
        earth.calcAccelTo(mars)
        mars.calcAccelTo(sun)
        mars.calcAccelTo(earth)

        #Update object position
        sun.update()
        earth.update()
        mars.update()

        #Put space to screen
        screen.blit(bg, (0, 0))      

        #Put each object to screen
        sun.draw(screen)
        earth.draw(screen)
        mars.draw(screen)
      
        #update screen
        pygame.display.update()     

        if r1 < CRASH_DIST or r2 < CRASH_DIST:
#        if r1 < CRASH_DIST or r2 < CRASH_DIST or r3 < CRASH_DIST:
            done = True
            print("Crashed")
            break
        if r1 > OUT_DIST or r2 > OUT_DIST:
            done = True
            print("Out of system")
            break

    #Farewell
    print (":-)")


if __name__ == "__main__":
    main()

