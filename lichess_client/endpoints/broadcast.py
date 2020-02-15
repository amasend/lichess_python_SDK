from typing import TYPE_CHECKING

from lichess_client.abstract_endpoints.abstract_broadcast import AbstractBroadcast

if TYPE_CHECKING:
    from lichess_client.clients.base_client import BaseClient


class Broadcast(AbstractBroadcast):
    """Class for Broadcast API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def create_a_broadcast(self):
        pass

    async def get_your_broadcast(self):
        pass

    async def update_your_broadcast(self):
        pass

    async def push_pgn_to_your_broadcast(self):
        pass
