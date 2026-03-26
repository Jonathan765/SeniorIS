'''
This file contains the abstract class that defines the machine learning model API used by the tool
'''

class BaseModel:
    def forward_plain(self, x):
        raise NotImplementedError

    def forward_encrypted(self, x_enc):
        raise NotImplementedError

    @property
    def multiplicative_depth(self):
        raise NotImplementedError
