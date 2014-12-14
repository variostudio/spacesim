import random
from math import sin, cos, hypot
from flyobj import FlyObject


class AsteroidGenerator:
    centerX, centerY = 0.0, 0.0
    radiusMin, radiusMax = 0, 0
    asteroidNumber = 0
    spaceColor = "black"
    surfaceColor = "white"

    speed_range_from = -5
    speed_range_to = 5

    rotation = 0.0

    def __init__(self, centerX, centerY, radiusMin, radiusMax, number, surfaceColor, spaceColor, rotation=0.0):
        random.seed()
        self.centerX = centerX
        self.centerY = centerY
        self.radiusMin = radiusMin
        self.radiusMax = radiusMax
        self.asteroidNumber = number
        self.spaceColor = spaceColor
        self.surfaceColor = surfaceColor
        self.rotation = rotation

    def generate(self, system):
        for i in range(self.asteroidNumber):
            angle = random.randint(0, 360)
            radius = random.randint(self.radiusMin, self.radiusMax)
            x = self.centerX + int(radius * sin(angle))
            y = self.centerY + int(radius * cos(angle))

            dx = self.centerX - x
            dy = self.centerY - y

            rotation_x = -dy / hypot(dx, dy) * self.rotation
            rotation_y = dx / hypot(dx, dy) * self.rotation

            obj = FlyObject("Asteroid {0}".format(i), 100, x, y,
                            random.uniform(self.speed_range_from, self.speed_range_to) + rotation_x,
                            random.uniform(self.speed_range_from, self.speed_range_to) + rotation_y)

            obj.initSurface(2, self.surfaceColor, self.spaceColor)

            system.append(obj)


