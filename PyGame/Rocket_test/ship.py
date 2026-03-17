import pygame

class Ship:

    def __init__(self, rocket_game):
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()

        # Load image and get its rect
        self.image = pygame.image.load('images/onlyrocket.bmp')
        self.rect = self.image.get_rect()

        # Start ship in center
        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)
