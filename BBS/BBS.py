import matplotlib.pyplot as plt
import numpy as np
from random import randint
from math import floor, sqrt


class BBS:
    def __init__(self,
                 p: int,
                 q: int) -> None:
        """
        Creates an object to generate random binary string
        :param p: big prime
        :param q: big prime, p != q
        """
        self._p: int = p
        self._q: int = q
        self._bloom_number: int = p * q

    def __get_init_value(self) -> int:
        """
        Search for random coprime with the bloom number.
        :return: coprime with the bloom number
        """
        rand = randint(2, self._bloom_number - 1)
        while rand % self._p == 0 or rand % self._q == 0:
            rand = randint(2, self._bloom_number - 1)
        return rand

    def generate_bits(self, length: int) -> str:
        """
        Runs BBS algorithm
        :param length: number of bits to generate
        :return: string with bits (contains '0b' prefix)
        """
        init_value = self.__get_init_value() ** 2 % self._bloom_number
        result = '0b' + str(init_value % 2)
        
        for _ in range(length - 1):
            x = init_value ** 2 % self._bloom_number
            result += str(x % 2)
            init_value = x
        return result

    @staticmethod
    def visualize(bits: str) -> None:
        """
        Shows plot for string of bits
        :param bits: string with 0 and 1 (can contain '0b' prefix)
        """
        bits = bits[2:] if bits[1] == 'b' else bits
        num_rows = floor(sqrt(len(bits)))

        matrix = np.array(
            [
                [int(el) for el in bits[i: i + num_rows]] for i in range(0, num_rows ** 2, num_rows)
            ]
        )

        plt.imshow(matrix, cmap='binary')
        plt.xticks([])
        plt.yticks([])
        plt.colorbar(ticks=[0, 1])
        plt.show()
        plt.close()
