from abc import ABC, abstractmethod


class AbstractBroadcast(ABC):
    """An abstract class for Broadcast API Endpoint"""

    @abstractmethod
    def create_a_broadcast(self):
        pass

    @abstractmethod
    def get_your_broadcast(self):
        pass

    @abstractmethod
    def update_your_broadcast(self):
        pass

    @abstractmethod
    def push_pgn_to_your_broadcast(self):
        pass
