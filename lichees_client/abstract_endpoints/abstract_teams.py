from abc import ABC, abstractmethod


class AbstractTeams(ABC):
    """An abstract class for Teams API Endpoint"""

    @abstractmethod
    def get_members_of_a_team(self):
        pass

    @abstractmethod
    def join_a_team(self):
        pass

    @abstractmethod
    def leave_a_team(self):
        pass

    @abstractmethod
    def kick_a_user_from_your_team(self):
        pass
