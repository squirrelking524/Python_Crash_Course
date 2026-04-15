class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize games settings"""
        # Screen settings
        # Changed width and height from 1200 and 800
        self.screen_width = 800 
        self.screen_height = 600
        self.bg_color = (20, 20, 50)

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
