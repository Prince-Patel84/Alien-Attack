import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load("images/ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False

    def update(self, ai_game):
        if self.moving_right and self.rect.right < ai_game.settings.GameSize[0]:
            self.rect.x += self.settings.Ship_Speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.Ship_Speed

    def blitme(self, ai_game):
        if self.rect.right > ai_game.settings.GameSize[0]:
            self.rect.right = ai_game.settings.GameSize[0]-1
        elif self.rect.left < 0:
            self.rect.left = 0
        self.screen.blit(self.image, self.rect)