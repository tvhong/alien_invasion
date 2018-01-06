import sys

import pygame

from settings import Settings
from ship import Ship


def check_events():
    '''Watch for keyboard and mouse events.'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def draw_screen(settings, screen, ship):
    '''Update images on the screen and flip to the new screen.'''
    screen.fill(settings.bg_color)
    ship.blitme()

    # Make the most recently draw screen visible
    pygame.display.flip()


def run_game():
    pygame.init()
    pygame.display.set_caption('Alien Invasion')

    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    ship = Ship(screen)

    while True:
        check_events()
        draw_screen(settings, screen, ship)


if __name__ == '__main__':
    run_game()
