from .base import BaseModel

'''
This file contains the class that defines how a pre-existing model can be wrapped to fit the
format of the tool.
'''


class WrappedModel(BaseModel):
   
    # it takes the original model, its predetermined depth, and the specific encrypted
    # forward pass function (which is compatible with homomorphic operations).
    def __init__(self, model, depth, encrypted_forward_fn):
        self.model = model
        self._depth = depth
        self._encrypted_forward_fn = encrypted_forward_fn

    def forward_plain(self, x):
        return self.model(x)

    def forward_encrypted(self, x_enc):
        return self._encrypted_forward_fn(x_enc)
    
    def __call__(self, x):  
        if hasattr(x, "dot"):
            return self.forward_encrypted(x) 
        return self.forward_plain(x)

    @property
    def multiplicative_depth(self):
        return self._depth
