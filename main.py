import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienAttack:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.GameSize)
        pygame.display.set_caption(self.settings.WindowName)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update(self)
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

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_F11:
            if self.settings.GameSize == self.settings.SmallGameSize:
                self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                self.settings.GameSize = (self.screen.get_rect().width,self.screen.get_rect().height)
                self.ship.rect.midbottom = (self.ship.rect.x,self.settings.GameSize[1])
            else:
                self.settings.GameSize = self.settings.SmallGameSize
                self.screen = pygame.display.set_mode(self.settings.GameSize)
                pygame.display.set_caption(self.settings.WindowName)
                self.ship.rect.midbottom = (self.ship.rect.x,self.settings.SmallGameSize[1])
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme(self)
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <=0:
                self.bullets.remove(bullet)

    def _create_alien(self, curr_x, curr_y):
        new_alien = Alien(self)
        new_alien.x = curr_x
        new_alien.y = curr_y
        new_alien.rect.x = curr_x
        new_alien.rect.y = curr_y
        self.aliens.add(new_alien)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        curr_x, curr_y = alien_width, alien_height

        while curr_y < (self.settings.SmallGameSize[1] - 3*alien_height):
            while curr_x < (self.settings.SmallGameSize[0] - 2*alien_width):
                self._create_alien(curr_x, curr_y)
                curr_x += 2* alien_width
            curr_x = alien_width
            curr_y += 2*alien_height


if __name__ == '__main__':
    ai = AlienAttack()
    ai.run_game()