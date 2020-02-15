from abc import ABC, abstractmethod


class AbstractMessaging(ABC):
    """An abstract class for Messaging API Endpoint"""

    @abstractmethod
    def send_a_private_message(self):
        pass
