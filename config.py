import configparser
import argparse
import textwrap

from asteroidgenerator import *


class Config:
    width = 0
    height = 0
    starts = 0
    display = (0,0)
    stopOnCollision = True
    star_colors = []
    useAsteroidGenerator = False

    def __init__(self):
        parser = argparse.ArgumentParser(description='Solar mechanics simulator',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''\
                Keys used:
                    q or ESC     = Exit
                    p or SPACE   = Pause
                    f            = Toggle fullscreen (if supported)
            '''))

        parser.add_argument('-f', '--file', 
            dest='file', 
            default='main.ini',
            help='configuration file')

        args = parser.parse_args()

        self.config = configparser.ConfigParser()
        self.config.read(args.file)

        sys = self.config['System']
        self.width = int(sys.get("WIN_WIDTH", 800))
        self.height = int(sys.get("WIN_HEIGHT", 640))
        self.stars = int(sys.get("STAR_NUM", 10))

        self.display = (self.width, self.height)

        colors = sys.get("STAR_COLORS")
        self.star_colors = colors.split(',')

        self.space_color = sys.get("SPACE_COLOR")

        self.onCollision = sys.get("ON_COLLISION", "stop")

        #Asteroids if any
        asteroidNumber = int(sys.get("ASTEROID_BELT_NUMBER", 0))
        asteroidCenterX = int(sys.get("ASTEROID_BELT_X", 0))
        asteroidCenterY = int(sys.get("ASTEROID_BELT_Y", 0))
        asteroidMinRadius = int(sys.get("ASTEROID_BELT_RADIUS_MIN", 0))
        asteroidMaxRadius = int(sys.get("ASTEROID_BELT_RADIUS_MAX", 0))
        asteroidColor = sys.get("ASTEROID_BELT_COLOR", "white")

        if (asteroidNumber > 0):
            self.generator = AsteroidGenerator(asteroidCenterX, asteroidCenterY, asteroidMinRadius, asteroidMaxRadius, asteroidNumber, asteroidColor, self.space_color)
            self.useAsteroidGenerator = True



    def getSystem(self):
        s = []

        for i in self.config.sections():
            if (i != "System"):
                obj = FlyObject(i, 
                    int (self.config[i]["Mass"]), 
                    float (self.config[i]["X"]), 
                    float (self.config[i]["Y"]), 
                    float (self.config[i]["VX"]), 
                    float (self.config[i]["VY"]))
                
                obj.initSurface(int (self.config[i]["R"]), 
                    self.config[i]["color"], 
                    self.space_color)
                
                s.append(obj)
        if (self.useAsteroidGenerator):
            self.generator.generate(s)

        return s

    def getDisplay(self):
        return self.display

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
    
    def getStarNumber(self):
        return self.stars

    def getStarColors(self):
        return self.star_colors

    def getSpaceColor(self):
        return self.space_color

