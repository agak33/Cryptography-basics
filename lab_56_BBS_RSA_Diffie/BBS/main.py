
from bigPrimesGenerator import BigPrimesGenerator
from BBS import BBS
from tests import *

if __name__ == '__main__':
    p, q = BigPrimesGenerator(2, 20).primes_list
    print('Primes for BBS algorithm:', p, q)

    bbs = BBS(p, q)
    bits = bbs.generate_bits(20000)
    bbs.visualize(bits)

    # tests
    frequency_test(
        bits,
        lower_threshold=9725, upper_threshold=10275
    )

    series_test(
        bits, '0',
        [
            [2315, 2685],
            [1114, 1386],
            [ 527,  723],
            [ 240,  384],
            [ 103,  209],
            [ 103,  209]
        ], long_series_threshold=26
    )
    series_test(
        bits, '1',
        [
            [2315, 2685],
            [1114, 1386],
            [527, 723],
            [240, 384],
            [103, 209],
            [103, 209]
        ], long_series_threshold=26
    )

    pokerTest(bits)
