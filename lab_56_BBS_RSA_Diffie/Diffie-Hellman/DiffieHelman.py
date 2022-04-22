
from utils import *


def check_if_primitive(number: int, big_prime: int) -> bool:
    """
    Checks if the number is a primitive root modulo big_prime
    """
    remainder = 1 << (big_prime - 1)
    curr_pow: int = 1
    for k in range(1, big_prime):
        curr_pow *= number
        curr_bit = 1 << (curr_pow % big_prime - 1)
        if remainder & curr_bit:
            return False
        remainder |= curr_bit
    return True


def get_value_to_send(secret_value: int,
                      primitive_root: int,
                      big_prime: int) -> int:
    return modular_exp(primitive_root, secret_value, big_prime)


def get_session_key(received_value: int,
                    secret_value: int,
                    big_prime: int) -> int:
    return modular_exp(received_value, secret_value, big_prime)
