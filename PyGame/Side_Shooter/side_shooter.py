import sys
import pygame

from settings import Settings
from gun import Gun
from bullets import Bullet

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

        self.gun = Gun(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self.gun.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.gun.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.gun.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.gun.moving_down = False

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.right <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.gun.blitme()

        pygame.display.flip()

if __name__ == '__main__':
        ss = SideShooter()
        ss.run_game()