from typing import TYPE_CHECKING

from lichess_client.abstract_endpoints.abstract_relations import AbstractRelations

if TYPE_CHECKING:
    from lichess_client.clients.base_client import BaseClient


class Relations(AbstractRelations):
    """Class for Relations API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def get_users_followed_by_a_user(self):
        pass

    async def get_users_who_follow_a_user(self):
        pass
