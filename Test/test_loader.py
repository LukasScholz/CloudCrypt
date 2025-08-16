import os
import unittest

from CloudCrypt.subroutines.ConfigManager import Config
from CloudCrypt.subroutines.loader import Loader

# constants
CONFIGPATH = "Test/testconfig.csv"


class MyTestCase(unittest.TestCase):
    def test_create_storage(self):
        config = Config(CONFIGPATH)
        loader = Loader(CONFIGPATH)
        loader.create_storage()
        dirs = os.listdir(config.CloudStorage)
        self.assertNotEqual(len(dirs), 0)

    def test_load_storage(self):
        config = Config(CONFIGPATH)
        loader = Loader(CONFIGPATH)
        loader.load_storage()
        dirs = os.listdir(config.LocalStorage)
        self.assertNotEqual(len(dirs), 0)

if __name__ == '__main__':
    unittest.main()
