from abc import ABC, abstractmethod


class AbstractStudies(ABC):
    """An abstract class for Studies API Endpoint"""

    @abstractmethod
    def export_one_study_chapter(self):
        pass

    @abstractmethod
    def export_all_chapters(self):
        pass
