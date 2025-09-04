import unittest

from src.CloudCrypt.subroutines.ConfigManager import Config

# constants
CONFIGPATH = "Test/testconfig.csv"


class TestSubroutines(unittest.TestCase):

    def test_config(self):
        config = Config(CONFIGPATH)
        self.assertNotEqual(len(config._data), 0)


if __name__ == '__main__':
    unittest.main()
