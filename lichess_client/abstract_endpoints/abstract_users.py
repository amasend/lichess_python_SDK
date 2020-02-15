from abc import ABC, abstractmethod


class AbstractUsers(ABC):
    """An abstract class for Users API Endpoint"""

    @abstractmethod
    def get_real_time_users_status(self):
        pass

    @abstractmethod
    def get_all_top_10(self):
        pass

    @abstractmethod
    def get_one_leaderboard(self):
        pass

    @abstractmethod
    def get_user_public_data(self):
        pass

    @abstractmethod
    def get_rating_history_of_a_user(self):
        pass

    @abstractmethod
    def get_user_activity(self):
        pass

    @abstractmethod
    def get_your_puzzle_activity(self):
        pass

    @abstractmethod
    def get_users_by_id(self):
        pass

    @abstractmethod
    def get_members_of_a_team(self):
        pass

    @abstractmethod
    def get_live_streamers(self):
        pass
