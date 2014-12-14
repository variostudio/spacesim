from pygame import *
import math

# Simulation precision.
# Lower value is better precision but lower simulation speed
T = 0.1


class FlyObject:
    mass = 0.0
    x, y, vx, vy, ax, ay = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    radius = 0.0
    surfaceColor = "black"
    spaceColor = "black"
    others = []
    image = ""
    name = ''

    # Creates new flying object like planet or star
    def __init__(self, name, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.name = name
        self.others = []

        print("{0}, ({1}, {2}) v=({3}, {4}), mass={5}".format(name, x, y, vx, vy, mass))

    def initSurface(self, R, surfaceColor, spaceColor):
        self.radius = R
        self.spaceColor = spaceColor
        self.surfaceColor = surfaceColor
        self.image = Surface((R * 2, R * 2))
        self.image.fill(Color(spaceColor))
        draw.circle(self.image, Color(surfaceColor), (R, R), R)

    # Distance to other F.O.
    def dist(self, other):
        return math.hypot((self.x - other.x),
                          (self.y - other.y))

    # Calculates acceleration to other object
    def calcAccelTo(self, other):
        self.others.append((other.mass, other.x, other.y))

    def fx(self, local_x):
        a = 0
        for (mass, x, y) in self.others:
            r = math.hypot(x - local_x, y - self.y)
            a += mass * (x - local_x) / r ** 3

        return a

    def fy(self, local_y):
        a = 0
        for (mass, x, y) in self.others:
            r = math.hypot(x - self.x, y - local_y)
            a += mass * (y - local_y) / r ** 3

        return a

    def calcX(self):
        k1 = T * self.fx(self.x)
        q1 = T * self.vx

        k2 = T * self.fx(self.x + q1 / 2)
        q2 = T * (self.vx + k1 / 2)

        k3 = T * self.fx(self.x + q2 / 2)
        q3 = T * (self.vx + k2 / 2)

        k4 = T * self.fx(self.x + q3)
        q4 = T * (self.vx + k3)

        self.vx += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        self.x += (q1 + 2 * q2 + 2 * q3 + q4) / 6

    def calcY(self):
        k1 = T * self.fy(self.y)
        q1 = T * self.vy

        k2 = T * self.fy(self.y + q1 / 2)
        q2 = T * (self.vy + k1 / 2)

        k3 = T * self.fy(self.y + q2 / 2)
        q3 = T * (self.vy + k2 / 2)

        k4 = T * self.fy(self.y + q3)
        q4 = T * (self.vy + k3)

        self.vy += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        self.y += (q1 + 2 * q2 + 2 * q3 + q4) / 6

    def update(self):
        self.calcX()
        self.calcY()
        self.others.clear()

    # Draw to screen
    def draw(self, screen, offset_x=0, offset_y=0):
        screen.blit(self.image, (int(self.x - self.radius) + offset_x, int(self.y - self.radius) + offset_y))


def join(object1, object2):
    name = object1.name + " " + object2.name
    mass = object1.mass + object2.mass

    x = (object1.x * object1.mass + object2.x * object2.mass) / mass
    y = (object1.y * object1.mass + object2.y * object2.mass) / mass

    vx = (object1.vx * object1.mass + object2.vx * object2.mass) / mass
    vy = (object1.vy * object1.mass + object2.vy * object2.mass) / mass

    new_color = object1.surfaceColor
    if object2.mass >= object1.mass:
        new_color = object2.surfaceColor

    object3 = FlyObject(name, mass, x, y, vx, vy)
    radius = int((mass ** (1 / 3.0)) / 2)
    object3.initSurface(radius, new_color, object1.spaceColor)

    return object3