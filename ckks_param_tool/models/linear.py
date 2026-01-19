from .base import BaseModel

class LinearModel(BaseModel):
    def __init__(self, weights, bias):
        self.W = weights
        self.b = bias

    def forward_plain(self, x):
        return x @ self.W + self.b

    def forward_encrypted(self, x_enc):
        return x_enc.dot(self.W) + self.b

    def __call__(self, x):
        if hasattr(x, "dot"):        
            return self.forward_encrypted(x)
        else:                        
            return self.forward_plain(x)

    @property
    def multiplicative_depth(self):
        return 1
