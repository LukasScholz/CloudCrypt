from cryptography.fernet import Fernet, MultiFernet
import os.path


class Encryption:

    def __init__(self, keyfile):
        self.keyring = keyfile
        self._init_key(keyfile)

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
        with open(destination+".cyacrypt", 'wb') as data:
            data.write(encrypted)

    def decrypt(self, file, destination):
        fernet = self._get_keys()
        with open(file, 'rb') as data:
            encrypted = data.read()
        decrypted = fernet.decrypt(encrypted)
        with open(destination[0:-9], 'wb') as data:
            data.write(decrypted)

