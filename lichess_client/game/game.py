from typing import List

from lichess_client.game.board import Board
from lichess_client.game.move import Move
from lichess_client.utils.enums import SideTypes, GameStatusTypes


# TODO: Game should be child of chess.Game
class Game:
    def __init__(self, side: 'SideTypes'):
        self.board = Board()
        self.side = side
        self.state = GameStatusTypes.STARTED

    def update(self, game_state: List[Move]):
        pass
