import unittest

from src.CloudCrypt.subroutines import Encryption
from src.CloudCrypt.subroutines.ConfigManager import Config

# constants
CONFIGPATH = "Test/testconfig.csv"
TEST_BYTESTRING = b"DASISTEINTEST"


class MyTestCase(unittest.TestCase):
    def test_encrypt_string(self):
        config = Config(CONFIGPATH)
        cryptor = Encryption(config.KeyFile)
        encrypted = cryptor.encrypt_string(TEST_BYTESTRING)

        self.assertNotEqual(TEST_BYTESTRING, encrypted)

    def test_decrypt_string(self):
        try:
            self.test_encrypt_string()
        except Exception:
            self.skipTest("Encryption Failed! Cannot Test Decryption without Encryption")

        config = Config(CONFIGPATH)
        cryptor = Encryption(config.KeyFile)
        encrypted = cryptor.encrypt_string(TEST_BYTESTRING)
        result = cryptor.decrypt_string(encrypted + b".cyacrypt")
        self.assertEqual(result, TEST_BYTESTRING)


if __name__ == '__main__':
    unittest.main()
