from abc import ABC, abstractmethod

class AbstractCrawler(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def crawl(self):
        pass

    @abstractmethod
    def execute_main(self):
        pass

    @abstractmethod
    def execute_before(self):
        pass

    @abstractmethod
    def execute_after(self):
        pass

    @abstractmethod
    def get_steps(self):
        pass

    @abstractmethod
    def save_data(self):
        pass