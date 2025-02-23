import sys
from time import sleep

import pygame

from settings import Settings
from game_ststs import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

class AlienAttack:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.GameSize)
        pygame.display.set_caption(self.settings.WindowName)

        self.stats = GameStats(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.game_active = False

        self.play_button = Button(self,"Play")

    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update(self)
                self._update_bullets()
                self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_F11:
            if self.settings.GameSize == self.settings.SmallGameSize:
                self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                self.settings.GameSize = (self.screen.get_rect().width,self.screen.get_rect().height)
                self.ship.rect.midbottom = (self.ship.rect.x,self.settings.GameSize[1])
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_active = True

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme(self)
        self.aliens.draw(self.screen)

        if not self.game_active:
            self.play_button._draw_button()

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
        self._check_alien_bullet_collistions()
        

    def _check_alien_bullet_collistions(self):
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

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

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollide(self.ship, self.aliens, False):
            self._ship_hit()
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1

            self.aliens.empty()
            self.bullets.empty()

            self._create_fleet()
            self.ship.center_ship()
        else:
            self.game_active = False
        sleep(0.5)

    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.GameSize[1]:
                self._ship_hit()
                break

if __name__ == '__main__':
    ai = AlienAttack()
    ai.run_game()