
from bigPrimesGenerator import BigPrimesGenerator
from BBS import BBS


if __name__ == '__main__':
    print(BigPrimesGenerator.test_miller_rabin(717897987691852588770249, 10))
    print(BigPrimesGenerator.test_miller_rabin(42682483, 100))
    print(BigPrimesGenerator.test_miller_rabin(10900741, 3))
    print(BigPrimesGenerator.test_miller_rabin(9, 3))
    print(BigPrimesGenerator.test_miller_rabin(11, 3))
    print(BigPrimesGenerator.test_miller_rabin(15, 3))
    print(BigPrimesGenerator.test_miller_rabin(17, 3))
    print(BigPrimesGenerator.test_miller_rabin(19, 3))
    print(BigPrimesGenerator.test_miller_rabin(21, 3))
    print(BigPrimesGenerator.test_miller_rabin(25, 3))

