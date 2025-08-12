import os
from pathlib import Path

import CloudCrypt.subroutines.ConfigManager
import CloudCrypt.subroutines.cryptor


class Loader:

    def __init__(self, config):
        self.config = CloudCrypt.subroutines.ConfigManager.Config(config)
        self.cryptor = CloudCrypt.subroutines.cryptor.Encryption(self.config.KeyFile)

    def create_backup(self):
        cloud = Path(self.config.CloudStorage[:-1])
        client = Path(self.config.LocalStorage[:-1])

        for root, _, files in os.walk(client):
            for filename in files:  # loop through files in the current directory
                self.cryptor.encrypt(os.path.join(root, filename),
                                     str(cloud) + os.path.join(root, self._FileNameCrypter.encrypt(filename))[len(str(client)):])

    def load_backup(self):
        cloud = Path(self.config.CloudStorage[:-1])
        client = Path(self.config.LocalStorage[:-1])

        for root, _, files in os.walk(cloud):
            for filename in files:  # loop through files in the current directory
                self.cryptor.decrypt(os.path.join(root, filename),
                                     str(client) + os.path.join(root, self._FileNameCrypter.decrypt(filename))[len(str(cloud)):])

    class _FileNameCrypter:

        def encrypt(filename):
            result = []
            for c in filename:
                result.append(chr(ord(c)*2-7))
            return "".join(result)

        def decrypt(filename):
            result = []
            for c in filename:
                result.append(chr((ord(c) + 7)//2))
            return "".join(result)
