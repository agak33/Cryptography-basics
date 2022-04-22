
from DiffieHelman import *
from bigPrimesGenerator import BigPrimesGenerator
from random import randint

if __name__ == '__main__':
    big_prime = BigPrimesGenerator(1, 5).primes_list[0]
    print('big prime:', big_prime)

    root = randint(2, big_prime - 1)
    while not check_if_primitive(root, big_prime):
        root = randint(2, big_prime - 1)
    print('pierwiastek pierwotny:', root)

    x, y = BigPrimesGenerator(2, 10).primes_list

    A_to_send = get_value_to_send(x, root, big_prime)
    B_to_send = get_value_to_send(y, root, big_prime)

    print('Klucz prywatny osoby A:', x)
    print('Wyslana wartosc do B:', A_to_send)

    print('Klucz prywatny osoby B:', y)
    print('Wyslana wartosc do A:', B_to_send)

    A_key = get_session_key(B_to_send, x, big_prime)
    B_key = get_session_key(A_to_send, y, big_prime)

    print('klucz A:', A_key)
    print('klucz B:', B_key)
