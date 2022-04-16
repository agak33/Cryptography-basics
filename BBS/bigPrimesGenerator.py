
from random import randint
from typing import List
from utils import *


class BigPrimesGenerator(object):
    def __init__(self,
                 primes_num: int,
                 lower_threshold: int,
                 upper_threshold: int,
                 accuracy: int = 10) -> None:

        self._primes_num: int = primes_num
        self._lower_threshold: int = lower_threshold
        self._upper_threshold: int = upper_threshold
        self._accuracy: int = accuracy
        self._primes_list: List[int] = []

    def __get_odd_num(self) -> int:
        """
        Gets random, odd number from interval <self._lower_threshold, self._upper_threshold>
        """
        result = None
        while result in self._primes_list or result is None:
            result = randint(self._lower_threshold, self._upper_threshold)
            if result % 2 == 0:
                result = result + 1 if result < self._upper_threshold - 1 else result - 1
        return result

    @property
    def primes_list(self) -> List[int]:
        """
        Calculates and returns prime list from given interval
        """
        self._primes_list = []

        for _ in range(self._primes_num):
            while True:
                candidate: int = self.__get_odd_num()
                if candidate not in self._primes_list:
                    if self.test_miller_rabin(candidate, self._accuracy):
                        self._primes_list.append(candidate)
                        break

        return self._primes_list

    @staticmethod
    def __get_max_power(potential_prime: int) -> int:
        """
        Calculates the maximal power of 2, which can divide potential_prime-1
        """
        potential_prime -= 1
        power = 0
        while not potential_prime % 2:
            power += 1
            potential_prime /= 2
        return power

    @staticmethod
    def test_miller_rabin(potential_prime: int, accuracy: int) -> bool:
        """
        Perform Miller Rabin prime test for given number.
        :param potential_prime: number to test
        :param accuracy: number of iterations
        :return: True, if potential_prime is probably a prime, False otherwise
        """
        if potential_prime == 2:
            return True
        if potential_prime % 2 == 0:
            return False

        s = BigPrimesGenerator.__get_max_power(potential_prime)
        d = potential_prime // (2 ** s)

        numbers_to_test: List[int] = []

        for _ in range(accuracy):
            rand = randint(1, potential_prime - 1)
            while rand in numbers_to_test:
                rand = randint(1, potential_prime - 1)
            numbers_to_test.append(rand)

        for number in numbers_to_test:
            if modular_exp(number, d, potential_prime) != 1:
                for r in range(0, s):
                    if modular_exp(number, 2**r * d, potential_prime) == potential_prime - 1:
                        break

                    if r == s - 1:
                        return False
        return True
