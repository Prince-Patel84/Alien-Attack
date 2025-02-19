import sys

import pygame

#Game Variables
GameSize = (1066,600)
WindowName = "Alien Attack"

class AlienAttack:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode(GameSize)
        pygame.display.set_caption("Alien Attack")
        self.clock = pygame.time.Clock()
        self.bg_color = (230,230,230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = AlienAttack()
    ai.run_game()