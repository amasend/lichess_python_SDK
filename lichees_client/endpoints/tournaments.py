from typing import TYPE_CHECKING

from lichees_client.abstract_endpoints.abstract_tournaments import AbstractTournaments

if TYPE_CHECKING:
    from lichees_client.clients.base_client import BaseClient


class Tournaments(AbstractTournaments):
    """Class for Tournaments API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def get_current_tournaments(self):
        pass

    async def create_a_new_tournament(self):
        pass

    async def export_games_of_a_tournament(self):
        pass

    async def get_results_of_a_tournament(self):
        pass

    async def get_tournaments_created_by_a_user(self):
        pass
