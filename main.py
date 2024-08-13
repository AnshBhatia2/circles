import pygame, sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Circles")
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
purple = (255,0,255)

screen.fill("white")
pygame.display.update()

while True:
    class Circle():
        def __init__(self,color,position,radius,width):
            self.circle_surf = screen
            self.circle_color = color
            self.circle_radius = radius
            self.circle_position = position
            self.circle_width = width

        def draw(self):
            self.Draw_Circle = pygame.draw.circle(self.circle_surf, self.circle_color, self.circle_position ,self.circle_radius, self.circle_width)

    yellowCircle = Circle(yellow,((50,20),100,10))
    redCircle = Circle(red,((150,200),150,10))
    purpleCircle = Circle(purple,((300,400),200,10))

    yellowCircle.draw()
    redCircle.draw()
    purpleCircle.draw()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()