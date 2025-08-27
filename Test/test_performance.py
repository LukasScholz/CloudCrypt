import random
import string
import unittest
from timeit import default_timer as timer


from CloudCrypt.subroutines.ConfigManager import Config
from CloudCrypt.subroutines.loader import Loader

# constants
CONFIGPATH = "Test/testconfig.csv"
FILEAMOUNT = 300
FILESIZE = 500000

def generate_big_random_file(filename, size):
    chars = ''.join([random.choice(string.ascii_letters) for i in range(size)])
    with open(filename, 'w') as f:
        f.write(chars)

class MyTestCase(unittest.TestCase):
    def test_storage_performance(self):
        config = Config(CONFIGPATH)
        loader = Loader(CONFIGPATH)
        print("Generating Files...")
        for i in range(FILEAMOUNT):
            generate_big_random_file(config.LocalStorage + "/tempfile_"+str(i), FILESIZE)
        print("Creating Storage...")

        start = timer()
        loader.create_storage()
        end = timer()
        print()
        print("---------------------------------")
        print("Time in seconds: "+str(end - start))
        print("Time per File: "+str((end - start)/FILEAMOUNT))
        print("Time per Character: " + str((end - start) / (FILEAMOUNT*FILESIZE)))
        print("---------------------------------")
        print()


if __name__ == '__main__':
    unittest.main()