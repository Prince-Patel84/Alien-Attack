class Settings:
    def __init__(self):
        self.SmallGameSize = (1066,600)
        self.GameSize = self.SmallGameSize
        self.WindowName = "Alien Attack"
        self.bg_color = (230,230,230)


        self.Ship_Speed = 2
        self.ship_limit = 1
        
        
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        
        
        self.alien_speed = 1.0
        self.fleet_direction = 1
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.alien_points = 50

        self._initialize_dynamic_settings()

    def _initialize_dynamic_settings(self):
        self.Ship_Speed = 2
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.Ship_Speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
