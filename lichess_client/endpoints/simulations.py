from typing import TYPE_CHECKING

from lichess_client.abstract_endpoints.abstract_simulations import AbstractSimulations

if TYPE_CHECKING:
    from lichess_client.clients.base_client import BaseClient


class Simulations(AbstractSimulations):
    """Class for Simulations API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def get_current_simuls(self):
        pass
