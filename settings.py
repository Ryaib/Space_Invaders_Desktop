class Settings():
        def __init__(self):
            # Screen settings
            self.screen_width = 800
            self.screen_height = 600
            self.bg_color = (230, 230, 230)
            # Ship Settings
            self.ship_speed_factor = 2.5
            self.ship_limit = 3
            # Bullet Settings
            self.bullet_speed_factor = 10
            self.bullet_width = 10
            self.bullet_height = 35
            self.bullet_color = 255, 0, 0
            self.bullets_allowed = 7
            # Alien Settings
            self.alien_speed_factor = 1
            self.fleet_drop_speed = 10
            # fleet_direction of 1 represents right; -1 represents left.
            self.fleet_direction = 1
            self.speedup_scale = 1.1
            self.score_scale = 1.5

            self.initialize_dynamic_settings()


        def initialize_dynamic_settings(self):
            self.ship_speed_factor = 1.5
            self.bullet_speed_factor = 3
            self.alien_speed_factor = 1
            self.alien_points = 50

            # fleet direction of 1 is right, -1 is left
            self.fleet_direction = 1

        def increase_speed(self):
            self.ship_speed_factor *= self.speedup_scale
            self.bullet_speed_factor *= self.speedup_scale
            self.alien_speed_factor *= self.speedup_scale
            self.alien_points = int(self.alien_points * self.score_scale)
            print(self.alien_points)