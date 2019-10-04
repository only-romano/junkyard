# Contains the settings class.


class Settings:
    """Класс для хранения настроек игры Sideways Invasion."""

    def __init__(self):
        """Инициализация игровых настроек."""
        self.screen_width = 1024
        self.screen_height = 600
        # Задаёт цвет в переменную для использования в background window.
        self.bg_color = (167, 223, 237)

        # Ship settings.
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 231, 166, 46
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
