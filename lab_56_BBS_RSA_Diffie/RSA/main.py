
from bigPrimesGenerator import BigPrimesGenerator
from RSA import RSA

if __name__ == '__main__':
    p, q = BigPrimesGenerator(2, 4).primes_list
    print('Found prime numbers:', p, q)
    rsa = RSA(p, q)
    message_to_test = 'Oto wiadomosc zlozona z 50 znakow w celu przetestowania RSA.'

    enc = rsa.encrypt(message_to_test)
    print(enc)

    print(rsa.decrypt(enc))
