class GameStats:
    """Track statistics for alien invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score and high level should never be reset.
        high_score_file = 'high_score.json'
        high_level_file = 'high_level.json'
        with open(high_score_file, 'r') as file_content:
            high_score_str = file_content.read()
        self.high_score = int(high_score_str)

        with open(high_level_file, 'r') as file_content:
            high_level_str = file_content.read()
        self.high_level = int(high_level_str)

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
