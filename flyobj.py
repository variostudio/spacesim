from pygame import *
import math

T = 1.0

class FlyObject:
    mass = 0.0
    x, y, vx, vy, ax, ay = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
    raduis = 0
    surfaceColor = "black"

    #Creates new flying object like planet or star
    def __init__(self, name, mass, x, y, vx, vy):
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

        self.ax_new = 0.0
        self.ay_new = 0.0

        print("{0}, ({1}, {2}) v=({3}, {4}), mass={5}"
             .format(name, x, y, vx, vy, mass))

    def initSurface(self, R, surfaceColor, spaceColor):
       self.radius = R
       self.image = Surface((R*2, R*2))
       self.image.fill(Color(spaceColor))
       draw.circle (self.image, Color(surfaceColor), (R, R), R)

    #Distance to other F.O.
    def dist(self, other):
        return math.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2 )

    #Caluculates acceleration to other object
    def calcAccelTo(self, other):
        r = self.dist(other)
        self.ax_new += other.mass * (other.x - self.x) / r**3
        self.ay_new += other.mass * (other.y - self.y) / r**3

    def update(self):
        self.vx += self.ax_new
        self.vy += self.ay_new

        self.x += self.vx
        self.y += self.vy

        self.ax = self.ax_new
        self.ay = self.ay_new

        self.ax_new = 0.0
        self.ay_new = 0.0

    #Draw to screen
    def draw(self, screen):
        screen.blit(self.image, (int(self.x - self.radius), int(self.y - self.radius)))
