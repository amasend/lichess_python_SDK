from abc import ABC, abstractmethod


class AbstractTournaments(ABC):
    """An abstract class for Tournaments API Endpoint"""

    @abstractmethod
    def get_current_tournaments(self):
        pass

    @abstractmethod
    def create_a_new_tournament(self):
        pass

    @abstractmethod
    def export_games_of_a_tournament(self):
        pass

    @abstractmethod
    def get_results_of_a_tournament(self):
        pass

    @abstractmethod
    def get_tournaments_created_by_a_user(self):
        pass
