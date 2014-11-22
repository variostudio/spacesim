import random
from flyobj import FlyObject


class AsteroidGenerator:
    centerX, centerY = 0.0, 0.0
    radiusMin, radiusMax = 0, 0
    asteroidNumber = 0
    spaceColor = "black"
    surfaceColor = "white"

    def __init__(self, centerX, centerY, radiusMin, radiusMax, number, surfaceColor, spaceColor):
        random.seed()
        self.centerX = centerX
        self.centerY = centerY
        self.radiusMin = radiusMin
        self.radiusMax = radiusMax
        self.asteroidNumber = number
        self.spaceColor = spaceColor
        self.surfaceColor = surfaceColor

    def generate(self, system):
        for i in range(self.asteroidNumber):
            obj = FlyObject("Asteroid {0}".format(i), random.randint(50, 100),
                            random.randint(0, 1000), random.randint(0,1000),
                            random.uniform(-2, 2), random.uniform(-2, 2))
            obj.initSurface(2, self.surfaceColor, self.spaceColor)

            system.append(obj)


