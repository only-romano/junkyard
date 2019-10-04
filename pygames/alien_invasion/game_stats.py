#! Статистика


class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_set):
        """Initialize statistics."""
        self.ai_set = ai_set
        self.reset_stats()
        # Start Alien Invasion in an inactive state.
        self.game_active = False
        # High score should never be reset.
        with open('score.txt', 'r') as score:
            best = score.read()
        self.high_score = int(best)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_set.ship_limit
        self.score = 0
        self.level = 1
