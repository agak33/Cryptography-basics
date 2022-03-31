import imp
from utils import *


class BBS:
    def __init__(self,
                 p: int,
                 q: int) -> None:
        self.p:           int = p
        self.q:           int = q
        self.bloomNumber: int = p * q

    def generateBits(self, length: int) -> str:
        initValue = generateInitValue(self.p, self.q) ** 2 % self.bloomNumber
        string = '0b' + str(initValue % 2)
        
        for _ in range(length - 1):
            x = initValue ** 2 % self.bloomNumber
            string += str(x % 2)
            initValue = x
        return string