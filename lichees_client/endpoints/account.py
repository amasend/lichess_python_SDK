from typing import TYPE_CHECKING

from lichees_client.abstract_endpoints.abstract_account import AbstractAccount

if TYPE_CHECKING:
    from lichees_client.clients.base_client import BaseClient


class Account(AbstractAccount):
    """Class for Account API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def get_my_profile(self):
        pass

    async def get_my_email_address(self):
        pass

    async def get_my_preferences(self):
        pass

    async def get_my_kid_mode_status(self):
        pass

    async def set_my_kid_mode_status(self):
        pass
