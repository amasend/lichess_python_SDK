from typing import TYPE_CHECKING

from lichess_client.abstract_endpoints.abstract_studies import AbstractStudies

if TYPE_CHECKING:
    from lichess_client.clients.base_client import BaseClient


class Studies(AbstractStudies):
    """Class for Studies API Endpoint"""

    def __init__(self, client: 'BaseClient') -> None:
        self._client = client

    async def export_one_study_chapter(self):
        pass

    async def export_all_chapters(self):
        pass
