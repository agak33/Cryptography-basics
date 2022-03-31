from BBS import BBS
from utils import *
from tests import *


if __name__ == '__main__':
    bbs = BBS(*generateRandomPair())
    string = bbs.generateBits(length=20000)

    # tests for 20 000 bit string
    frequencyTest(string, 9725, 10275)
    serieTest(string, '1', 
              intervals=[
                    [2315, 2685],
                    [1114, 1386],
                    [ 527,  723],
                    [ 240,  384],
                    [ 103,  209],
                    [ 103,  209]], 
              longSerieThreshold=26)

    serieTest(string, '0', 
              intervals=[
                    [2315, 2685],
                    [1114, 1386],
                    [ 527,  723],
                    [ 240,  384],
                    [ 103,  209],
                    [ 103,  209]], 
              longSerieThreshold=26)
    
    pokerTest(string)

