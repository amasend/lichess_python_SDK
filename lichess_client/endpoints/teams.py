from typing import TYPE_CHECKING

from lichess_client.abstract_endpoints.abstract_teams import AbstractTeams

if TYPE_CHECKING:
    from lichess_client.clients.base_client import BaseClient


class Teams(AbstractTeams):
    """Class for Teams API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def get_members_of_a_team(self):
        pass

    async def join_a_team(self):
        pass

    async def leave_a_team(self):
        pass

    async def kick_a_user_from_your_team(self):
        pass
