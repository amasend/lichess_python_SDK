from typing import TYPE_CHECKING

from lichees_client.abstract_endpoints.abstract_users import AbstractUsers

if TYPE_CHECKING:
    from lichees_client.clients.base_client import BaseClient


class Users(AbstractUsers):
    """Class for Users API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def get_real_time_users_status(self):
        pass

    async def get_all_top_10(self):
        pass

    async def get_one_leaderboard(self):
        pass

    async def get_user_public_data(self):
        pass

    async def get_rating_history_of_a_user(self):
        pass

    async def get_user_activity(self):
        pass

    async def get_your_puzzle_activity(self):
        pass

    async def get_users_by_id(self):
        pass

    async def get_members_of_a_team(self):
        pass

    async def get_live_streamers(self):
        pass
