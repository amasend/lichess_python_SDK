from typing import TYPE_CHECKING

from lichees_client.abstract_endpoints.abstract_games import AbstractGames

if TYPE_CHECKING:
    from lichees_client.clients.base_client import BaseClient


class Games(AbstractGames):
    """Class for Games API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def export_one_game(self):
        pass

    async def export_games_of_a_user(self):
        pass

    async def export_games_by_ids(self):
        pass

    async def stream_current_games(self):
        pass

    async def get_ongoing_games(self):
        pass

    async def get_current_tv_games(self):
        pass
