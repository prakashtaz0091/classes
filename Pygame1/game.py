# Example file showing a basic pygame "game loop"
import pygame
from game_characters import Circle

# pygame setup
pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True


circle1 = Circle(x_pos=10, y_pos=100)
circle2 = Circle(x_pos=10, y_pos=180, speed=15)
circle3 = Circle(x_pos=10, y_pos=250, speed=20)
circle4 = Circle(x_pos=10, y_pos=350, speed=25)


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    Circle.draw_all_circles_on_screen(screen)

    Circle.move_all_circles_on_screen(SCREEN_WIDTH)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(30)  # limits FPS to 60

pygame.quit()
