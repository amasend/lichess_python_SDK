import json
from typing import TYPE_CHECKING

from lichess_client.utils.enums import RequestMethods
from lichess_client.abstract_endpoints.abstract_games import AbstractGames
from lichess_client.helpers import Response
from lichess_client.utils.hrefs import GAMES_EXPORT_ONE_URL

if TYPE_CHECKING:
    from lichess_client.clients.base_client import BaseClient


class Games(AbstractGames):
    """Class for Games API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def export_one_game(self, game_id: str) -> 'Response':
        """
        Download one game. Only finished games can be downloaded.

        Parameters
        ----------
        game_id: str, required
            ID of the game.

        Returns
        -------
        Response object with response content.

        Example
        -------
        >>> from lichess_client import APIClient
        >>> client = APIClient(token='...')
        >>> response = client.users.export_one_game(game_id='q7zvsdUF')
        # TODO: add more examples
        """
        headers = {
            'Content-Type': 'application/json'
        }
        parameters = {
            'moves': 'true',
            'pgnInJson': 'false',
            'tags': 'true',
            'clocks': 'true',
            'evals': 'true',
            'opening': 'true',
            'literate': 'true'
        }
        response = await self._client.request(method=RequestMethods.GET,
                                              url=GAMES_EXPORT_ONE_URL.format(gameId=game_id),
                                              headers=headers,
                                              params=parameters)
        return response

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
