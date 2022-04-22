
from random import randint
from typing import List
from utils import *


class BigPrimesGenerator(object):
    def __init__(self,
                 primes_num: int,
                 digits_number: int,
                 accuracy: int = 10) -> None:

        self._primes_num: int = primes_num
        self._digits_number: int = digits_number
        self._accuracy: int = accuracy
        self._small_primes: List[int] = []
        self._primes_list: List[int] = []

        self._lower = 10 ** (self._digits_number - 1)
        self._upper = int('9' * self._digits_number)

        self.__get_small_primes(2000)

    def __get_small_primes(self, max_val: int):
        """
        Finds all primes from interval <1; max_val>
        """
        sieve = [1] * max_val
        for i in range(1, max_val):
            if sieve[i]:
                self._small_primes.append(i + 1)
                for j in range((i+1)**2 - 1, max_val, i + 1):
                    sieve[j] = 0

    def __get_odd_num(self) -> int:
        """
        Gets random, odd number
        """
        while True:
            rand = randint(self._lower, self._upper) | 1
            for i in range(len(self._small_primes)):
                if rand % self._small_primes[i] == 0:
                    break
                if i == len(self._small_primes) - 1:
                    return rand

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
        Performs Miller Rabin prime test for given number
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
