import os
import unittest
from pathlib import Path

from CloudCrypt.subroutines.ConfigManager import Config
from CloudCrypt.subroutines.cryptor import Encryption
from CloudCrypt.subroutines.loader import Loader
from CloudCrypt.subroutines.Backup_Creator import BackupCreator

# constants
CONFIGPATH = "Test/testconfig.csv"


class MyTestCase(unittest.TestCase):
    def test_create_storage(self):
        config = Config(CONFIGPATH)
        loader = Loader(CONFIGPATH)
        loader.create_storage()
        dirs = os.listdir(config.CloudStorage)
        self.assertNotEqual(len(dirs), 0)


if __name__ == '__main__':
    unittest.main()
