import pygame
import random
from flyobj import *
from config import *

CRASH_DIST = .5
OUT_DIST = 10000

STEPS = 5

R_MIN_MAX = 99999.0

def main():
    cfg = Config()

    r_min = R_MIN_MAX
    r_max = 0.0

    offset_x = 0
    offset_y = 0

    collapsedObject1 = ""
    collapsedObject2 = ""

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
            (random.randrange(bg.get_width()),
             random.randrange(bg.get_height())),
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
                if e.key == K_UP:
                    offset_y += 10
                if e.key == K_DOWN:
                    offset_y -= 10
                if e.key == K_LEFT:
                    offset_x += 10
                if e.key == K_RIGHT:
                    offset_x -= 10


        if not paused:

            for st in range(STEPS):
                for i in system:
                    for j in system:
                        if i.name != j.name:
                            dist = i.dist(j)
                            dist -= (i.radius + j.radius)
                            i.calcAccelTo(j)
                            r_max = max(r_min, dist)

                            if (dist < r_min):
                                r_min = dist
                                collapsedObject1 = i
                                collapsedObject2 = j

                #Join, crash or stop!
                if r_min < CRASH_DIST:
                    if cfg.onCollision == "stop":
                        done = True
                        print("Collision detected")
                    elif cfg.onCollision == "remove":
                        print("Collision detected {0}, {1}".format(collapsedObject1.name, collapsedObject2.name))
                        system.remove(collapsedObject1)
                        system.remove(collapsedObject2)
                        r_min = R_MIN_MAX
                    elif cfg.onCollision == "join":
                        print("Join detected {0}, {1}".format(collapsedObject1.name, collapsedObject2.name))
                        system.remove(collapsedObject1)
                        system.remove(collapsedObject2)
                        system.append(join(collapsedObject1, collapsedObject2))
                        r_min = R_MIN_MAX

                for i in system:
                    i.update()

            #Put space to screen
            screen.blit(bg, (0, 0))

            #Put each object to screen
            for i in system:
                i.draw(screen, offset_x, offset_y)

            #update screen
            pygame.display.update()

            if r_max > OUT_DIST:
                done = True
                print("Out of system")
                break

    #Farewell
    print (":-)")


if __name__ == "__main__":
    main()

