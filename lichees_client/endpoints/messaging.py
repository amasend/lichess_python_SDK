from typing import TYPE_CHECKING

from lichees_client.abstract_endpoints.abstract_messaging import AbstractMessaging

if TYPE_CHECKING:
    from lichees_client.clients.base_client import BaseClient


class Messaging(AbstractMessaging):
    """Class for Messaging API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def send_a_private_message(self):
        pass
