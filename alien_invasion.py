import sys

import pygame

from settings import Settings


def run_game():
    pygame.init()
    pygame.display.set_caption('Alien Invasion')

    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)

    while True:
        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(settings.bg_color)

        # Make the most recently draw screen visible
        pygame.display.flip()


if __name__ == '__main__':
    run_game()
