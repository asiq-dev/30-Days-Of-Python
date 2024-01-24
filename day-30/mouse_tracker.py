#imports code
import pygame
from collections import namedtuple

# set color for individual elements

Colour = namedtuple("Colour",['red', 'green', 'blue'])

background_color = Colour(red = 36, green = 188, blue = 168)
# rectangle_color = Colour(red = 255, green = 255, blue = 255)
circle_color = Colour(red=255, green=253, blue=65)

pygame.init()

#write text in screen
# font = pygame.font.Font(None, 28)
# text  = font.render("Woo! this is first text", True, (0,0,0))

#screen setings
pygame.display.set_caption(" Mouse Tracker")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])
# screen.fill(background_color)
# screen.blit(text, (200,100))
# pygame.draw.rect(screen, rectangle_color, [0, 0, 100, 50])
# pygame.display.update()

def main():
    circle_position = (screen.get_width() // 2), (screen.get_height() // 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
    
                return
            elif event.type == pygame.MOUSEMOTION:
                circle_position = event.__dict__["pos"]
            
        screen.fill(background_color)
        pygame.draw.circle(screen, circle_color, circle_position, 20)
        pygame.display.update()

        clock.tick(60)    
main()