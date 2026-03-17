import sys
import pygame
from ship import Ship

class Rocket:

    def __init__(self):
        pygame.init()
    
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket")

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()

            pygame.display.flip()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                elif event.key == pygame.K_DOWN:
                    self.ship.moving_down = False
                elif event.key == pygame.K_UP:
                    self.ship.moving_up = False


if __name__ == '__main__':
    rocket = Rocket()
    rocket.run_game()