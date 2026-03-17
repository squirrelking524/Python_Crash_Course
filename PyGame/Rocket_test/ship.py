import pygame

class Ship:

    def __init__(self, rocket_game):
        self.screen = rocket_game.screen
        self.screen_rect = rocket_game.screen.get_rect()

        # Load image and get its rect
        self.image = pygame.image.load('Rocket_test/images/onlyrocket.bmp')
        self.rect = self.image.get_rect()

        # Start ship in center
        self.rect.center = self.screen_rect.center

        self.moving_right = False
        self.moving_left = False
        self.moving_down = False
        self.moving_up = False

    def update(self):
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
        elif self.moving_down:
            self.rect.x += 1
        elif self.moving_up:
            self.rect.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
