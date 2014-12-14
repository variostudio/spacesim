import pygame
from control import Control
from flyobj import *
from config import *


def main():
    cfg = Config()

    # PyGame init
    pygame.init()
    screen = pygame.display.set_mode(cfg.getDisplay())
    pygame.display.set_caption("Solar Mechanics")

    # Space init
    bg = Surface(cfg.getDisplay())
    bg.fill(Color(cfg.getSpaceColor()))
    # Draw fixed stars
    for i in range(cfg.getStarNumber()):
        draw.circle(bg, Color(random.sample(cfg.getStarColors(), 1)[0]),
                    (random.randrange(bg.get_width()),
                     random.randrange(bg.get_height())),
                    0)

    # Timer init
    timer = pygame.time.Clock()

    control = Control(timer, screen, bg, cfg)
    control.run()

    # Farewell
    print(":-)")


if __name__ == "__main__":
    main()

