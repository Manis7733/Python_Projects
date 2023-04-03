import pygame
import math
pygame.init()

Width, Height = 800,800
Win = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Planet Sim")

YELLOW = (255, 255, 0)
WHITE = (255,255,255)
BLUE = (100,149,237)
RED = (188,39,50)

class Planet():

    AU = 149.6e6 * 1000
    G = 6.67428e-11
    SCALE = 200 / AU # 1AU = 100 pixel
    TIMESTEP  = 3600 * 24 # 1 Day


    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_val = 0
        self.y_val = 0

    def draw(self,win):
        x = self.x * self.SCALE + Width / 2
        y = self.y * self.SCALE + Height / 2
        pygame.draw.circle(win, self.color, (x,y), self.radius)

def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0,0,30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1*Planet.AU,0,16,BLUE,5.9742 * 10**24)
    mars = Planet(-1.524 * Planet.AU,0,12,RED,6.39 * 10**23)

    planets = [sun,earth,mars]

    while run:

        clock.tick(60)
        Win.fill(WHITE)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.draw(Win)

        pygame.display.update()

    pygame.quit()

main()