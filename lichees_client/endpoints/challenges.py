from typing import TYPE_CHECKING

from lichees_client.abstract_endpoints.abstract_challenges import AbstractChallenges

if TYPE_CHECKING:
    from lichees_client.clients.base_client import BaseClient


class Challenges(AbstractChallenges):
    """Class for Challenges API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def stream_incoming_events(self):
        pass

    async def create_a_challenge(self):
        pass

    async def accept_a_challenge(self):
        pass

    async def decline_a_challenge(self):
        pass
