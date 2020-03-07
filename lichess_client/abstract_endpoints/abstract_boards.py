from abc import ABC, abstractmethod


class AbstractBoards(ABC):
    """An abstract class for Bots API Endpoint"""

    @abstractmethod
    def stream_incoming_events(self):
        """
        Stream the events reaching a lichess user in real time.
        """
        pass

    @abstractmethod
    def create_a_seek(self,
                      time: int,
                      increment: int,
                      variant: 'VariantTypes',
                      color: 'ColorType',
                      rated: bool,
                      rating_range):
        """
        Create a public seek, to start a game with a random player.
        """
        pass

    @abstractmethod
    def stream_game_state(self, game_id: str):
        """
        Stream the state of a game being played with the Board API
        """
        pass
