from typing import Any, TYPE_CHECKING

from asyncio import get_event_loop
from aiohttp import ClientSession

from lichees_client.utils.enums import RequestMethods
from lichees_client.utils.constants import LICHEES_ACCOUNT_URL

if TYPE_CHECKING:
    from aiohttp.client_reqrep import ClientResponse


class BaseClient:
    """
    ASYNC BaseClient class for handling secure connections with Lichees API via token usage.

    Parameters
    ----------
    token: str, required
        String with token provided from Lichees.org account site.

    loop: asyncio event loop, optional
        Asyncio event loop for async mode operations
    """
    def __init__(self, token: str, *, loop=None) -> None:
        self.loop = loop or get_event_loop()
        self._token = token
        self._headers = {'Authorization': f"Bearer {self._token}"}
        self.session = ClientSession(headers=self._headers, loop=self.loop)

    async def request(self, method: 'RequestMethods', url: str, **kwargs: Any) -> 'ClientResponse':
        """
        Request async method.

        Parameters
        ----------
        method: RequestMethods, required
            One of REST method, please refer to lichees_client.utils.enums.RequestMethods

        url: str, required
            URL string for REST API endpoint

        Returns
        -------
        aiohttp.client_reqrep.ClientResponse with response details
        """
        async with self.session.request(method=method.value, url=url, **kwargs) as resp:
            return await resp.json()

    async def is_authorized(self) -> bool:
        response = await self.request(method=RequestMethods.GET, url=LICHEES_ACCOUNT_URL)
        if "error" in str(response):
            return False
        else:
            return True
