from abc import ABC, abstractmethod


class AbstractChallenges(ABC):
    """An abstract class for Challenges API Endpoint"""

    @abstractmethod
    def stream_incoming_events(self):
        pass

    @abstractmethod
    def create_a_challenge(self):
        pass

    @abstractmethod
    def accept_a_challenge(self):
        pass

    @abstractmethod
    def decline_a_challenge(self):
        pass
