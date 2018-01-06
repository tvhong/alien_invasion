from collections import namedtuple

ScreenSize = namedtuple('ScreenSize', ['width', 'height'])

class Settings():
    '''A class to store game settings.'''

    def __init__(self):
        self.screen_size = ScreenSize(1200, 800)
        self.bg_color = (230, 230, 230)
