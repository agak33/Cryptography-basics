from typing import List
from random import randint
from utils import *


class RSA:
    def __init__(self, p: int, q: int) -> None:
        self._p = p
        self._q = q
        self._n = p * q
        self._phi = (p - 1) * (q - 1)
        self._public = None
        self._private = None

        self._get_public_key()
        print('Public key:', self._public)
        self._get_private_key()
        print('Private key:', self._private)

        self.__min_block_size: int = 0
        self.__max_block_size: int = 0
        self.__calculate_block_size()

    def __get_all_divisors(self) -> List[int]:
        """
        Finds all factors of phi
        """
        result: List[int] = []
        phi = self._phi
        for i in range(2, int(self._phi ** 0.5)):
            if phi % i == 0:
                result.append(i)
                while phi % i == 0:
                    phi //= i
        return result

    def __calculate_block_size(self) -> None:
        """
        Calculates the single block size to encrypt and decrypt a message.
        """
        max_power: int = -1
        max_val: int = 1
        while max_val <= self._n:
            max_power += 1
            max_val *= 2

        self.__min_block_size = max_power // 8
        self.__max_block_size = self.__min_block_size + 1
        # print(f'Single block size: {self.__min_block_size}-{self.__max_block_size} bytes')

    def __divide_into_blocks(self, message: bytes, mode: str = 'encrypt') -> list[int]:
        """
        Divides the message to encrypt/decrypt into blocks.
        """
        block_size: int = self.__min_block_size if mode == 'encrypt' else self.__max_block_size
        return [
            int.from_bytes(message[i:min(i + block_size, len(message))], byteorder='big')
            for i in range(0, len(message), block_size)
        ]

    def _get_public_key(self):
        """
        Finds the public key
        """
        phi_factors = self.__get_all_divisors()
        # print(phi_factors)
        while True:
            rand = randint(3, self._phi - 1)
            for i in range(len(phi_factors)):
                if rand % phi_factors[i] == 0:
                    break
                if phi_factors[i] ** 2 >= rand:
                    self._public = rand
                    return

    def _get_private_key(self):
        """
        Finds the private key
        """
        self._private = inverse_under_modulo(self._public, self._phi)
        # while True:
        #     rand = randint(3, self._phi - 1) | 1
        #     if rand != self._public and self._public * rand % self._phi == 1:
        #         self._private = rand
        #         return

    def encrypt(self, message: str) -> str:
        blocks = self.__divide_into_blocks(message.encode(encoding='latin1'))
        return ''.join(
            [
                modular_exp(block, self._public, self._n).to_bytes(
                    self.__max_block_size, byteorder='big').decode(encoding='latin1')
                for block in blocks
            ]
        )

    def decrypt(self, message: str) -> str:
        blocks = self.__divide_into_blocks(message.encode(encoding='latin1'), 'decrypt')
        return ''.join(
            [
                modular_exp(block, self._private, self._n).to_bytes(
                    self.__min_block_size, byteorder='big').decode('latin1')
                for block in blocks
            ]
        )
