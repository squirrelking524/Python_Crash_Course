import sys
import pygame
from settings import Settings


class SideShooter:
    """Manage game assest and behavior"""

    def __init__(self):
        """Init game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Side Shooter")

    def run_game(self):
        while True:
            self._check_events()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        pygame.display.flip()

if __name__ == '__main__':
        ss = SideShooter()
        ss.run_game()