import unittest
import asyncio

from lichess_client import APIClient
from lichess_client.clients.base_client import BaseClient
from lichess_client.endpoints.account import Account
from lichess_client.endpoints.broadcast import Broadcast
from lichess_client.endpoints.challenges import Challenges
from lichess_client.endpoints.chess_bot import ChessBot
from lichess_client.endpoints.games import Games
from lichess_client.endpoints.messaging import Messaging
from lichess_client.endpoints.relations import Relations
from lichess_client.endpoints.simulations import Simulations
from lichess_client.endpoints.studies import Studies
from lichess_client.endpoints.teams import Teams
from lichess_client.endpoints.tournaments import Tournaments
from lichess_client.endpoints.users import Users
from lichess_client.endpoints.bots import Bots
from lichess_client.endpoints.boards import Boards
from tests.utils import async_test, get_token_from_config


class TestClient(unittest.TestCase):
    client: 'APIClient' = None
    token = get_token_from_config(section='amasend')

    @async_test
    def test__01__initialize__setup_APIClient__all_parameters_set_correctly(self) -> None:
        TestClient.client = APIClient(token=self.token, loop=asyncio.get_event_loop())

        self.assertIsInstance(self.client._client, BaseClient, msg="BaseClient incorrectly set.")
        self.assertIsInstance(self.client.account, Account, msg="Account incorrectly set.")
        self.assertIsInstance(self.client.broadcast, Broadcast, msg="Broadcast incorrectly set.")
        self.assertIsInstance(self.client.challenges, Challenges, msg="Challenges incorrectly set.")
        self.assertIsInstance(self.client.chess_bot, ChessBot, msg="ChessBot incorrectly set.")
        self.assertIsInstance(self.client.games, Games, msg="Games incorrectly set.")
        self.assertIsInstance(self.client.messaging, Messaging, msg="Messaging incorrectly set.")
        self.assertIsInstance(self.client.relations, Relations, msg="Relations incorrectly set.")
        self.assertIsInstance(self.client.simulations, Simulations, msg="Simulations incorrectly set.")
        self.assertIsInstance(self.client.studies, Studies, msg="Studies incorrectly set.")
        self.assertIsInstance(self.client.teams, Teams, msg="Teams incorrectly set.")
        self.assertIsInstance(self.client.tournaments, Tournaments, msg="Tournaments incorrectly set.")
        self.assertIsInstance(self.client.users, Users, msg="Users incorrectly set.")
        self.assertIsInstance(self.client.bots, Bots, msg="Bots incorrectly set.")
        self.assertIsInstance(self.client.boards, Boards, msg="Boards incorrectly set.")


if __name__ == '__main__':
    unittest.main()
