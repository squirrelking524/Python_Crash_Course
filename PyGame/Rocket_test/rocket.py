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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    rocket = Rocket()
    rocket.run_game()