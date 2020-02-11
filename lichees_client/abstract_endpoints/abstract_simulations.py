from abc import ABC, abstractmethod


class AbstractSimulations(ABC):
    """An abstract class for Simulations API Endpoint"""

    @abstractmethod
    def get_current_simuls(self):
        pass
