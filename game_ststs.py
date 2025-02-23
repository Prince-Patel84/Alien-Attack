class GameStats:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.ai_game = ai_game
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.high_score = int(self.ai_game.path.read_text())
        self.level = 1