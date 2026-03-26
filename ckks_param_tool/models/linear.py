from .base import BaseModel

'''
This file contains the class for a linear machine learning model that can be used by the tool.
Notably, this function only includes multiplications and addition, and not an approximated 
activation function for simplicity. 
'''
class LinearModel(BaseModel):
    def __init__(self, weights, bias):
        self.W = weights
        self.b = bias

    def forward_plain(self, x):
        return x @ self.W + self.b # @ operation supports plaintext vectors

    def forward_encrypted(self, x_enc):
        return x_enc.dot(self.W) + self.b # .dot operation supports ciphertext vectors

    def __call__(self, x):

        # conditionals to automatically handle if this model is called on plaintext or ciphertext
        if hasattr(x, "dot"):        
            return self.forward_encrypted(x)
        else:                        
            return self.forward_plain(x)

    # since this is a standard linear model, the depth is 1
    @property
    def multiplicative_depth(self):
        return 1
