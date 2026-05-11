import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a single star in the starfield"""

    def __init__(self, star_game):
        """Initialize the star and set its starting position"""
        super().__init__()
        self.screen = star_game.screen
        
        # Load the star image and set its rect attribute
        self.image = pygame.image.load('/home/david-smith/repos/Python/Python_Crash_Course/PyGame/Star/images/star.bmp')
        
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.rect = self.image.get_rect()

        # Start each new star at the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

       



