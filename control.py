import pygame
import os
from pygame import *
from flyobj import *

CRASH_DIST = .5
OUT_DIST = 10000

STEPS = 5

R_MIN_MAX = 99999.0

KEY_MOVE_PX = 20


class Control:
    timer = ""
    cfg = ""
    screen = ""
    bg = ""
    screen_number = 0

    def __init__(self, timer, screen, background, cfg):
        self.timer = timer
        self.cfg = cfg
        self.screen = screen
        self.bg = background
        self.save = False
        self.video_folder = "video"

    def run(self):
        r_min = R_MIN_MAX
        r_max = 0.0

        offset_x = 0
        offset_y = 0

        collapsed_object1 = ""
        collapsed_object2 = ""

        #Solar system init
        system = self.cfg.getSystem()

        done = False
        paused = False
        while not done:
            self.timer.tick(60)
            for e in pygame.event.get():
                if e.type == QUIT:
                    done = True
                    break
                if e.type == KEYDOWN:
                    if e.key == K_s:
                        self.save = not self.save
                    if e.key == K_q or e.key == K_ESCAPE:
                        done = True
                        break
                    if e.key == K_p or e.key == K_SPACE:
                        paused = not paused
                    if e.key == K_f:
                        pygame.display.toggle_fullscreen()
                    if e.key == K_UP:
                        offset_y += KEY_MOVE_PX
                    if e.key == K_DOWN:
                        offset_y -= KEY_MOVE_PX
                    if e.key == K_LEFT:
                        offset_x += KEY_MOVE_PX
                    if e.key == K_RIGHT:
                        offset_x -= KEY_MOVE_PX

            if not paused:
                for st in range(STEPS):
                    for i in system:
                        for j in system:
                            if i.name != j.name:
                                dist = i.dist(j)
                                dist -= (i.radius + j.radius)
                                i.calcAccelTo(j)
                                r_max = max(r_min, dist)

                                if dist < r_min:
                                    r_min = dist
                                    collapsed_object1 = i
                                    collapsed_object2 = j

                    #Join, crash or stop!
                    if r_min < CRASH_DIST:
                        if self.cfg.onCollision == "stop":
                            done = True
                            print("Collision detected")
                        elif self.cfg.onCollision == "remove":
                            print("Collision detected {0}, {1}".format(collapsed_object1.name, collapsed_object2.name))
                            system.remove(collapsed_object1)
                            system.remove(collapsed_object2)
                            r_min = R_MIN_MAX
                        elif self.cfg.onCollision == "join":
                            print("Join detected {0}, {1}".format(collapsed_object1.name, collapsed_object2.name))
                            system.remove(collapsed_object1)
                            system.remove(collapsed_object2)
                            system.append(join(collapsed_object1, collapsed_object2))
                            r_min = R_MIN_MAX

                    for i in system:
                        i.update()

                #Put space to screen
                self.screen.blit(self.bg, (0, 0))

                #Put each object to screen
                for i in system:
                    i.draw(self.screen, offset_x, offset_y)

                #update screen
                pygame.display.update()

                if self.save:
                    if not os.path.exists(self.video_folder):
                        os.makedirs(self.video_folder)

                    pygame.image.save(self.screen, "{0}/screenshot{1}.jpeg".format(self.video_folder, self.screen_number))
                    self.screen_number += 1

                if r_max > OUT_DIST:
                    print("Out of system")
                    done = True
                    break