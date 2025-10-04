import os
import random
import string
import unittest
import platform
import sys
from timeit import default_timer as timer


from cloudcrypt.subroutines.ConfigManager import Config
from cloudcrypt.subroutines.loader import Loader

# constants
TESTTYPE = "Encryption"
CONFIGPATH = "Test/testconfig.csv"
RESULTSPATH = "Test/testresults.csv"
REPEATS = 10 # TODO: Readjust!
FILEAMOUNT = 10   # 1KB per File
FILESIZE = 10 # 1GB in total
OS = platform.system()
VERSION = platform.python_version()


def generate_big_random_file(filename, size):
    chars = ''.join([random.choice(string.ascii_letters) for i in range(size)])
    with open(filename, 'w') as f:
        f.write(chars)


class MyTestCase(unittest.TestCase):
    def test_storage_performance(self):
        testtime_sum = 0
        for _ in range(REPEATS):
            config = Config(CONFIGPATH)
            loader = Loader(CONFIGPATH)
            for i in range(FILEAMOUNT):
                generate_big_random_file(config.LocalStorage + "/tempfile_"+str(i), FILESIZE)
            start = timer()
            loader.create_storage()
            end = timer()
            testtime_sum += (end - start)
            for i in range(FILEAMOUNT):
                os.remove(config.LocalStorage + "/tempfile_" + str(i))
        testtime = REPEATS / testtime_sum
        result = (f"{TESTTYPE},{OS},{VERSION},{FILEAMOUNT},{FILESIZE},{str(testtime / (FILEAMOUNT*FILESIZE))},"
                  f"{str(testtime/FILEAMOUNT)},{str(testtime)} GB/s")
        print(result)

if __name__ == '__main__':
    unittest.main()
