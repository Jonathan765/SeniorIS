from abc import ABC, abstractmethod

class ParameterSelector(ABC):
    @abstractmethod
    def select(self):
        """Return ranked (params, result, score) tuples"""
        pass
