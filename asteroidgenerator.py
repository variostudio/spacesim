import random
from math import sin, cos
from flyobj import FlyObject


class AsteroidGenerator:
    centerX, centerY = 0.0, 0.0
    radiusMin, radiusMax = 0, 0
    asteroidNumber = 0
    spaceColor = "black"
    surfaceColor = "white"

    speed_range_from = -5
    speed_range_to = 5

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
            angle = random.randint(0, 360)
            radius = random.randint(self.radiusMin, self.radiusMax)
            x = self.centerX + int(radius * sin(angle))
            y = self.centerY + int(radius * cos(angle))

            obj = FlyObject("Asteroid {0}".format(i), 100, x, y,
                            random.uniform(self.speed_range_from, self.speed_range_to),
                            random.uniform(self.speed_range_from, self.speed_range_to))

            obj.initSurface(2, self.surfaceColor, self.spaceColor)

            system.append(obj)


