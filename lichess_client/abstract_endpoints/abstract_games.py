from abc import ABC, abstractmethod


class AbstractGames(ABC):
    """An abstract class for Games API Endpoint"""

    @abstractmethod
    def export_one_game(self, game_id: str):
        """Download one game. Only finished games can be downloaded."""
        pass

    @abstractmethod
    def export_games_of_a_user(self):
        pass

    @abstractmethod
    def export_games_by_ids(self):
        pass

    @abstractmethod
    def stream_current_games(self):
        pass

    @abstractmethod
    def get_ongoing_games(self):
        pass

    @abstractmethod
    def get_current_tv_games(self):
        pass
