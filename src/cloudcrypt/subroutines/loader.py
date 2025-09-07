import os
from pathlib import Path
from cloudcrypt.subroutines.ConfigManager import Config
from cloudcrypt.subroutines.cryptor import Encryption

class Loader:

    def __init__(self, configpath):
        self.config = Config(configpath)
        self.cryptor = Encryption(self.config.KeyFile)

    def create_storage(self):
        cloud = Path(self.config.CloudStorage)
        client = Path(self.config.LocalStorage)

        for root, _, files in os.walk(client):
            if root.endswith("Backups"):
                continue
            for filename in files:  # loop through files in the current directory
                self.cryptor.encrypt(os.path.join(root, filename), str(cloud) +
                                     os.path.join(root, encrypt_filename(self.cryptor, filename))[len(str(client)):])

    def load_storage(self):
        cloud = Path(self.config.CloudStorage)
        client = Path(self.config.LocalStorage)

        for root, _, files in os.walk(cloud):
            for filename in files:  # loop through files in the current directory
                self.cryptor.decrypt(os.path.join(root, filename), str(client) +
                                     os.path.join(root, decrypt_filename(self.cryptor, filename))[len(str(cloud)):])


def encrypt_filename(cryptor: Encryption, filename):
    return (cryptor.encrypt_string(str.encode(filename))).decode()


def decrypt_filename(cryptor: Encryption, filename):
    return (cryptor.decrypt_string(str.encode(filename))).decode()
