from abc import ABC, abstractmethod


class System(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def update(self, component):
        pass
