from cryptography.fernet import Fernet, MultiFernet
import os.path
from cloudcrypt.subroutines.ConfigManager import Config

class Encryption:

    def __init__(self, config: Config):
        self.keyring = config.KeyFile
        self.cryptname = config.CryptName
        self._init_key(self.keyring)

    def _init_key(self, keyfile):
        if os.path.exists(keyfile):
            return
        # create empty binary file
        with open(keyfile, 'wb') as f:
            f.write(b"")

    def _get_keys(self):
        with open(self.keyring, 'rb') as file:
            lines = file.readlines()
        keys = []
        for line in lines:
            keys.append(Fernet(line))
        return MultiFernet(keys)

    def add_key(self):
        new_key = Fernet.generate_key()
        with open(self.keyring, 'ab') as f:
            f.write(new_key)
            f.write(str.encode("\n"))

    def add_key_to_front(self):
        new_key = Fernet.generate_key() + str.encode("\n")
        with open(self.keyring, 'rb') as file:
            lines = file.readlines()
        keys = [new_key]
        for line in lines:
            keys.append(line)
        with open(self.keyring, 'wb') as f:
            for key in keys:
                f.write(key)

    def encrypt(self, file, destination):
        fernet = self._get_keys()
        with open(file, 'rb') as data:
            original = data.read()
        encrypted = fernet.encrypt(original)
        with open(destination+self.cryptname, 'wb') as data:
            data.write(encrypted)

    def decrypt(self, file, destination):
        fernet = self._get_keys()
        with open(file, 'rb') as data:
            encrypted = data.read()
        decrypted = fernet.decrypt(encrypted)
        with open(destination, 'wb') as data:
            data.write(decrypted)

    def encrypt_string(self, string):
        fernet = self._get_keys()
        return fernet.encrypt(string)

    def decrypt_string(self, string):
        fernet = self._get_keys()
        return fernet.decrypt(string[0:-len(self.cryptname)])
