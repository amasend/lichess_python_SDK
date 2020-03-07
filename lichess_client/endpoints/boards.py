import json
from typing import TYPE_CHECKING, List

from lichess_client.abstract_endpoints.abstract_boards import AbstractBoards
from lichess_client.utils.enums import RequestMethods, VariantTypes, ColorType
from lichess_client.utils.client_errors import RatingRangeError
from lichess_client.utils.hrefs import BOARDS_STREAM_INCOMING_EVENTS, BOARDS_CREATE_A_SEEK, BOARDS_STREAM_GAME_STATE

if TYPE_CHECKING:
    from lichess_client.clients.base_client import BaseClient
    from lichess_client.helpers import Response


__all__ = [
    "Boards"
]


class Boards(AbstractBoards):
    """Class for Boards API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def stream_incoming_events(self) -> 'Response':
        """
        Stream the events reaching a lichess user in real time.

        Returns
        -------
        Response object with response content.

        Example
        -------
        >>> from lichess_client import APIClient
        >>> client = APIClient(token='...')
        >>> async for response in client.boards.stream_incoming_events()
        >>>     print(response)
        """
        headers = {
            'Content-Type': 'application/json'
        }
        async for response in self._client.request_constant_stream(method=RequestMethods.GET,
                                                                   url=BOARDS_STREAM_INCOMING_EVENTS,
                                                                   headers=headers):
            yield response

    async def create_a_seek(self,
                            time: int,
                            increment: int,
                            variant: 'VariantTypes' = VariantTypes.STANDARD,
                            color: 'ColorType' = ColorType.RANDOM,
                            rated: bool = False,
                            rating_range: List[int] = None) -> 'Response':
        """
        Create a public seek, to start a game with a random player.

        Parameters
        ----------
        rated: bool, optional
            Whether the game is rated and impacts players ratings.

        time: int, required
            Clock initial time in minutes.

        increment: int, required
            Clock increment in seconds.

        variant: VariantTypes, optional
             Enum: "standard" "chess960" "crazyhouse" "antichess" "atomic" "horde" "kingOfTheHill"
                "racingKings" "threeCheck"
                The variant of the game.

        color: ColorType, optional
             Enum: "random" "white" "black"
                The color to play. Better left empty to automatically get 50% white

        rating_range: List[int, int], optional
            The rating range of potential opponents. Better left empty. Example: [1500, 1800]

        Returns
        -------
        Response object with response content.

        Example
        -------
        >>> from lichess_client import APIClient
        >>> client = APIClient(token='...')
        >>> response = await client.boards.create_a_seek(time=10, increment=0)
        """

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'rated': json.dumps(rated),
            'time': time,
            'increment': increment,
            'variant': variant.value,
            'color': color.value,
        }
        if rating_range is not None and len(rating_range) != 2:
            raise RatingRangeError('create_a_seek', reason="rating_range should contain only two numbers")

        elif rating_range is not None:
            rating_range = [str(entry) for entry in rating_range]
            data['ratingRange'] = '-'.join(rating_range)

        response = await self._client.request_stream(method=RequestMethods.POST,
                                                     url=BOARDS_CREATE_A_SEEK,
                                                     data=data,
                                                     headers=headers)
        return response

    async def stream_game_state(self, game_id: str) -> 'Response':
        """
        Stream the state of a game being played with the Board API

        Parameters
        ----------
        game_id: str, required
            ID of the current playing game.

        Returns
        -------
        Response object with response content.

        Example
        -------
        >>> from lichess_client import APIClient
        >>> client = APIClient(token='...')
        >>> async for response in client.boards.stream_game_state(game_id='5IrD6Gzz')
        >>>     print(response)
        """
        headers = {
            'Content-Type': 'application/json'
        }
        async for response in self._client.request_constant_stream(method=RequestMethods.GET,
                                                                   url=BOARDS_STREAM_GAME_STATE.format(gameId=game_id),
                                                                   headers=headers):
            yield response
