from abc import ABC, abstractmethod

'''
This file contains the abstract parameter selection class that handles searching and evaluating
'''

class ParameterSelector(ABC):
    @abstractmethod
    def select(self):
        pass
