
from colorama import Fore
from typing import List


def frequencyTest(bits: bin, lowerThreshold: int, upperThreshold: int) -> None:
    bits = str(bits)[2:]
    try:
        result = bits.count('1')
        assert lowerThreshold < result < upperThreshold
        print(Fore.GREEN, 
              'Frequency test passed: ', 
              round(result/len(bits)*100, 3), '%', 
              Fore.RESET, sep='')
    except AssertionError:
        print(Fore.RED, 
              'Frequency test failed: ', round(result/len(bits)*100, 3), '%',
              Fore.RESET, sep='')


def serieTest(bits: bin, bitVal: str, intervals: List[List[int]], longSerieThreshold: int) -> None:
    bits = str(bits)[2:]
    counter = [0] * len(intervals)
    longSeriePassed: bool = True

    currSeqLen = 0
    for bit in bits:
        if bit == bitVal:
            currSeqLen += 1

        elif currSeqLen > 0 and currSeqLen < len(intervals):
                counter[currSeqLen - 1] += 1
                currSeqLen = 0

        elif currSeqLen > 0:
            counter[-1] += 1
            if currSeqLen >= longSerieThreshold:
                longSeriePassed = False
            currSeqLen = 0
    
    for counted, interval in zip(counter, intervals):
        try:
            assert interval[0] <= counted <= interval[1]
        except AssertionError:
            print(Fore.RED,
                  'Serie test failed.', sep='')
            
            if not longSeriePassed:
                print('Long serie test failed.', 
                      Fore.RESET, sep='')
            else:
                print(Fore.GREEN,
                      'Long serie test passed.', 
                      Fore.RESET, sep='')
            return
    
    if not longSeriePassed:
        print(Fore.RED, 'Long serie test failed.', sep='')
    else:
        print(Fore.GREEN, 'Long serie test passed.', sep='')
    print(Fore.GREEN,
          'Serie test passed.', 
          Fore.RESET, sep='')


def pokerTest(bits: bin) -> None:
    counter = [0] * 16
    bits    = str(bits)[2:]
    for i in range(0, len(bits), 4):
        counter[ int(bits[i:i+4], 2) ] += 1
    
    try:
        assert 2.16 <= 16/5000 * sum([el*el for el in counter]) - 5000 <= 46,17
        print(Fore.GREEN, 'Poker test passed.', Fore.RESET, sep='')
    except AssertionError:
        print(Fore.RED, 'Poker test failed.', Fore.RESET, sep='')