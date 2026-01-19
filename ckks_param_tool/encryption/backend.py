from abc import ABC, abstractmethod

class CKKSBackend(ABC):
    @abstractmethod
    def encrypt(self, vector):
        pass

    @abstractmethod
    def decrypt(self, enc_vector):
        pass
