import pygame.font
from pygame.sprite import Group
from pathlib import Path
from ship import Ship

class Scoreboard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.ai_game = ai_game
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,31)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
    
    def prep_score(self):
        score_str = f"Score: {self.stats.score:,}"
        self.score_image = self.font.render(score_str, True,self.text_color,self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 10
        self.score_rect.top = 10

    def prep_high_score(self):
        high_score_str = f"High Score: {self.stats.high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,self.text_color,self.settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            path = Path("high_score.txt")
            path.write_text(str(self.stats.high_score))
            self.prep_high_score()

    def prep_level(self):
        level_str = f"Level - {self.stats.level}"

        self.level_image = self.font.render(level_str, True, self.text_color, self.settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.top = self.score_rect.bottom + 5
        self.level_rect.right = self.score_rect.right
    
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 15 + ship_number * ship.rect.width * 1.2
            ship.rect.y = 10
            self.ships.add(ship)