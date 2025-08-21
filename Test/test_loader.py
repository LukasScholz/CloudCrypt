import os
import unittest

from CloudCrypt.subroutines.ConfigManager import Config
from CloudCrypt.subroutines.loader import Loader, encrypt_filename, decrypt_filename

# constants
CONFIGPATH = "Test/testconfig.csv"
TEST_FILENAME = "TESTFILENAME"


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

    def test_encrypt_filename(self):
        loader = Loader(CONFIGPATH)
        result = encrypt_filename(loader.cryptor, TEST_FILENAME)
        self.assertNotEqual(result, TEST_FILENAME)

    def test_decrypt_filename(self):
        try:
            self.test_encrypt_filename()
        except Exception:
            self.skipTest("Encryption Failed! Cannot Test Decryption without Encryption")

        loader = Loader(CONFIGPATH)
        encrypted = encrypt_filename(loader.cryptor, TEST_FILENAME)
        result = decrypt_filename(loader.cryptor, encrypted+".cyacrypt")
        self.assertEqual(result, TEST_FILENAME)


if __name__ == '__main__':
    unittest.main()
