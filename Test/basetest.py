import unittest

from CloudCrypt.subroutines.ConfigManager import Config
from CloudCrypt.subroutines.cryptor import Encryption
from CloudCrypt.subroutines.loader import Loader
from CloudCrypt.subroutines.Backup_Creator import BackupCreator

# constants
CONFIGPATH = "testconfig.csv"


class TestSubroutines(unittest.TestCase):

    def test_config(self):
        config = Config(CONFIGPATH)
        self.assertNotEqual(len(config._data), 0)


if __name__ == '__main__':
    unittest.main()
