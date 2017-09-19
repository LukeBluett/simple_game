import pygame
from sprites import *

# variable declaration

display_width = 600
display_height = 400

title = 'My Alien Game'

game_is_running = True
black = (0, 0, 0)

fps = 60

# function declaration

def draw():
    game_display.fill(black)
    my_alien.draw(game_display)

def set_boundaries():
    if my_alien.get_x_position() > (display_width - 80):
        my_alien.set_x_position(display_width - 80)

    if my_alien.get_x_position() < 0:
        my_alien.set_x_position(0)

    if my_alien.get_y_position() > (display_height - 50):
        my_alien.set_y_position(display_height - 50)

    if my_alien.get_y_position() < 0:
        my_alien.set_y_position(0)
    


def events(my_alien):
    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            my_alien.set_x_change(-5)

        if event.key == pygame.K_d:
            my_alien.set_x_change(5)

        if event.key == pygame.K_w:
            my_alien.set_y_change(-5)

        if event.key == pygame.K_s:
            my_alien.set_y_change(5)

        if event.key == pygame.K_SPACE:
            laser = Laser(my_alien.get_x_position() + 80, my_alien.get_y_position() + 10, 'resource/laser.png')
            laser.draw(game_display)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_a or event.key == pygame.K_d:
            my_alien.set_x_change(0)
            my_alien.set_x_position(my_alien.get_x_position())

        if event.key == pygame.K_w or event.key == pygame.K_s:
            my_alien.set_y_change(0)
            my_alien.set_y_position(my_alien.get_y_position())


# pygame begin

pygame.init()

game_display = pygame.display.set_mode([display_width, display_height])

pygame.display.set_caption(title)

clock = pygame.time.Clock()

my_alien = Alien(100, 100, 'resource/roughspaceship.png')

while game_is_running:
    set_boundaries()
    draw()
    for event in pygame.event.get():
        events(my_alien)

    pygame.display.update()

    clock.tick(fps)
