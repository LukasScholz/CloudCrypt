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
FILEAMOUNT = 1000
FILESIZE = 100000
OS = platform.system()
VERSION = platform.python_version()


def generate_big_random_file(filename, size):
    chars = ''.join([random.choice(string.ascii_letters) for i in range(size)])
    with open(filename, 'w') as f:
        f.write(chars)


class MyTestCase(unittest.TestCase):
    def test_storage_performance(self):
        config = Config(CONFIGPATH)
        loader = Loader(CONFIGPATH)
        for i in range(FILEAMOUNT):
            generate_big_random_file(config.LocalStorage + "/tempfile_"+str(i), FILESIZE)

        start = timer()
        loader.create_storage()
        end = timer()
        result = (f"{TESTTYPE},{OS},{VERSION},{FILEAMOUNT},{FILESIZE},{str((end - start) / (FILEAMOUNT*FILESIZE))},"
                  f"{str((end - start)/FILEAMOUNT)},{str(end - start)}")
        #with open(RESULTSPATH, 'a') as f:
        #    f.write(result)
        print(result)

if __name__ == '__main__':
    unittest.main()
