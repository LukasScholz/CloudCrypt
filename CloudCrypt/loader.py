from pathlib import Path

import cryptor
import os


class Loader:

    def __init__(self, config):
        config = open(config, 'r').readlines()
        for line in config:
            if line.startswith("CloudStorage"):
                self.cloud = line.split("=")[-1]
            if line.startswith("LocalStorage"):
                self.local = line.split("=")[-1]
            if line.startswith("KeyFile"):
                self.keyfile = line.split("=")[-1]

        self.cryptor = cryptor.Encryption(self.keyfile)

    def create_backup(self):
        cloud = Path(self.cloud[:-1])
        client = Path(self.local[:-1])

        for root, _, files in os.walk(client):
            for filename in files:  # loop through files in the current directory
                self.cryptor.encrypt(os.path.join(root, filename),
                                     str(cloud) + os.path.join(root, self._FileNameCrypter.encrypt(filename))[len(str(client)):])

    def load_backup(self):
        cloud = Path(self.cloud[:-1])
        client = Path(self.local[:-1])

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
