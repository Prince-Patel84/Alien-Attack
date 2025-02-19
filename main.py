import sys
from settings import Settings
import pygame


class AlienAttack:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(self.settings.GameSize)
        pygame.display.set_caption(self.settings.WindowName)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienAttack()
    ai.run_game()