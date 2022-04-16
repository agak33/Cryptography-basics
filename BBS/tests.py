from colorama import Fore
from typing import List


def frequency_test(bits: bin, lower_threshold: int, upper_threshold: int) -> bool:
    """
    Perform frequency test
    :param bits: binary string
    :param lower_threshold: lower threshold of '1' count interval (excluded this number)
    :param upper_threshold: upper threshold of '1' count interval (excluded this number)
    :return: True if test was passed, False otherwise
    """
    bits: str = str(bits)[2:]
    result = bits.count('1')
    try:
        assert lower_threshold < result < upper_threshold
        print(Fore.GREEN,
              'Frequency test passed: ',
              round(result / len(bits) * 100, 3), '%',
              Fore.RESET, sep='')
        return True
    except AssertionError:
        print(Fore.RED,
              'Frequency test failed: ', round(result / len(bits) * 100, 3), '%',
              Fore.RESET, sep='')
        return False


def series_test(bits: bin, bit_val: str, intervals: List[List[int]], long_series_threshold: int) -> bool:
    """
    Perform series test
    :param bits: binary string
    :param bit_val: '0', if test is running for '0' sequences, '1' otherwise
    :param intervals: a list containing 2-element lists with interval bounds
    :param long_series_threshold: minimal sequence length, which cause test fail
    :return: True if test was passed, False otherwise
    """
    bits: str = str(bits)[2:]
    counter: list[int] = [0] * len(intervals)
    long_series_passed: bool = True

    curr_seq_len = 0
    for bit in bits:
        if bit == bit_val:
            curr_seq_len += 1

        elif 0 < curr_seq_len < len(intervals):
            counter[curr_seq_len - 1] += 1
            curr_seq_len = 0

        elif curr_seq_len > 0:
            counter[-1] += 1
            if curr_seq_len >= long_series_threshold:
                long_series_passed = False
            curr_seq_len = 0

    for counted, interval in zip(counter, intervals):
        try:
            assert interval[0] <= counted <= interval[1]
        except AssertionError:
            print(Fore.RED,
                  'Series test failed.', sep='')

            if not long_series_passed:
                print('Long series test failed.',
                      Fore.RESET, sep='')
            else:
                print(Fore.GREEN,
                      'Long series test passed.',
                      Fore.RESET, sep='')
            return False

    print(Fore.GREEN, 'Series test passed.', Fore.RESET, sep='')

    if not long_series_passed:
        print(Fore.RED, 'Long series test failed.', sep='')
        return False
    else:
        print(Fore.GREEN, 'Long series test passed.', sep='')
        return True


def pokerTest(bits: bin) -> False:
    """
    Perform poker test for 20 000 length binary string
    :param bits: binary string
    :return: False, if test was passed, True otherwise
    """
    counter = [0] * 16
    bits = str(bits)[2:]
    for i in range(0, len(bits), 4):
        counter[int(bits[i:i + 4], 2)] += 1

    try:
        assert 2.16 <= 16 / 5000 * sum([el * el for el in counter]) - 5000 <= 46.17
        print(Fore.GREEN, 'Poker test passed.', Fore.RESET, sep='')
        return True
    except AssertionError:
        print(Fore.RED, 'Poker test failed.', Fore.RESET, sep='')
        return False
