import argparse
import shutil
import sys
import pathlib

from cloudcrypt import __version__
from cloudcrypt.subroutines import ConfigManager
from cloudcrypt.subroutines import cryptor

class MainInterface:

    def __init__(self, args):
        self.arguments = args
        self.config = None  # value set during runtime

    '''
    Main Program Execution
    '''
    def run(self):
        if self.arguments.version:
            self.display_version()
        if self.arguments.config:
            self.display_configpath()
        configpath = pathlib.Path(__file__).parent.resolve() / "etc" / "config.csv"
        self.config = ConfigManager.Config(configpath)
        if self.arguments.addkey:
            self.addkey()
        if self.arguments.loadkeys is not None:
            self.loadkeys(self.arguments.loadkeys)

    def display_version(self):
        print("CloudCrypt version " + __version__)
        exit(0)

    def display_configpath(self):
        print(pathlib.Path(__file__).parent.resolve() / "etc" / "config.csv")
        exit(0)

    def addkey(self):
        encryptor = cryptor.Encryption(self.config)
        encryptor.add_key()

    def loadkeys(self, newkeys):
        keyfile = self.config.KeyFile
        shutil.copyfile(newkeys, keyfile)


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f'Error: {message}\n\n\n')
        self.print_help()
        sys.exit(1)


def argparse():
    parser = CustomArgumentParser(description="Encrypted Backup-creator, mainly for Cloud usage")

    # arguments without value
    parser.add_argument("--addkey", "-a", action="store_true", help="Generate a new key File")
    parser.add_argument("----verifysetup", action="store_true", help="Verify Setup of Config File")
    parser.add_argument("--config", "-c", action="store_true", help="Get config file path")

    # arguments with value
    parser.add_argument("--loadkeys", "-l", help="Load keys from existing Keyfile")

    # optional arguments
    parser.add_argument("--version", "-v", action="store_true", help="prints version info and exit")
    args = parser.parse_args()
    interface = MainInterface(args)
    interface.run()


if __name__ == "__main__":
    argparse()
