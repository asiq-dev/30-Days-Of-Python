#imports code
import pygame
from collections import namedtuple
from random import randint



# set color for individual elements
Colour = namedtuple("Colour",['red', 'green', 'blue'])

background_color = Colour(red = 36, green = 188, blue = 168)
ball_color = Colour(red=255, green=253, blue=65)
ball_radius = 20

pygame.init()


#screen setings
pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])


def main():
    ball_position = [(screen.get_width() // 2), (screen.get_height() // 2)]
    ball_velocity = [randint(-5, 5), randint(-5, 5)]


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
    
                return
            

        screen.fill(background_color)
        pygame.draw.circle(screen, ball_color, ball_position, ball_radius)
        pygame.display.update()

        if ball_position[0] - ball_radius < 0:
            ball_velocity[0] = -ball_velocity[0]
        elif ball_position[0] + ball_radius > screen.get_width():
            ball_velocity[0] = -ball_velocity[0]

        # Check for top and bottom collisions
        if ball_position[1] - ball_radius < 0:
            ball_velocity[1] = -ball_velocity[1]
        elif ball_position[1] + ball_radius > screen.get_height():
            ball_velocity[1] = -ball_velocity[1]


        ball_position[0] += ball_velocity[0]
        ball_position[1] += ball_velocity[1]

        clock.tick(60)    
main()