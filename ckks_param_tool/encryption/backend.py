from abc import ABC, abstractmethod

'''
This file contains the abstract encrytion backend class, can be extended to other CKKS 
implementation libraries other than TenSEAL.
'''
class CKKSBackend(ABC):
    @abstractmethod
    def encrypt(self, vector):
        pass

    @abstractmethod
    def decrypt(self, enc_vector):
        pass
