import pygame


class Ship():
    def __init__(self, screen):
        '''Initialize the ship and set its starting position.'''
        self.screen = screen

        # Load the ship images and load its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Set the new ship at the bottom at the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)
