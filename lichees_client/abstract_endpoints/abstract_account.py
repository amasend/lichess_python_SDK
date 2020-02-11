from abc import ABC, abstractmethod


class AbstractAccount(ABC):
    """An abstract class for Account API Endpoint"""

    @abstractmethod
    def get_my_profile(self):
        pass

    @abstractmethod
    def get_my_email_address(self):
        pass

    @abstractmethod
    def get_my_preferences(self):
        pass

    @abstractmethod
    def get_my_kid_mode_status(self):
        pass

    @abstractmethod
    def set_my_kid_mode_status(self):
        pass
