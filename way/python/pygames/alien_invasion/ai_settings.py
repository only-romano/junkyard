# Contains the settings class.


class Settings:
    """Класс для хранения настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализация игровых настроек."""
        # Настройки экрана.
        self.screen_width = 1024
        self.screen_height = 600
        # Задаёт цвет в переменную для использования в background window.
        self.bg_color = (130, 0, 65)

        # Ship settings.
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 231, 166, 46
        self.bullets_allowed = 5

        # Alien settings
        # The setting fleet_drop_speed controls how quickly the fleet
        # drops down the screen each time an alien reaches either edge.
        # It’s helpful to separate this speed from the aliens horizontal
        # speed so you can adjust the twospeeds independently
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that  change throughoit the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3    # Циклы замедляют игру..
        self.alien_speed_factor = 1

        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
