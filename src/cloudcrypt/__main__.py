import argparse
import sys
import pathlib

from cloudcrypt import __version__
from cloudcrypt.subroutines import ConfigManager


class MainInterface:

    def __init__(self, args):
        self.arguments = args
        self.config = None  # value set during runtime

    def run(self):
        if self.arguments.version:
            self.display_version()
        if self.arguments.config:
            self.display_configpath()
        self.config = ConfigManager.Config(self.arguments.config)

    def display_version(self):
        print("CloudCrypt version " + __version__)
        exit(0)

    def display_configpath(self):
        print(pathlib.Path(__file__).parent.resolve())
        exit(0)


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f'Error: {message}\n\n\n')
        self.print_help()
        sys.exit(1)


def argparse():
    parser = CustomArgumentParser(description="Encrypted Backup-creator, mainly for Cloud usage")

    # required arguments
    parser.add_argument("--initkey", "-k", help="Generate a new key File")
    parser.add_argument("--loadkeys", "-l", help="Load keys from existing Keyfile")
    parser.add_argument("----verifysetup", help="Verify Setup of Config File")

    parser.add_argument("--config", "-c", action="store_true", help="Get config file path")

    # optional arguments
    parser.add_argument("--version", "-v", action="store_true", help="prints version info and exit")
    args = parser.parse_args()
    interface = MainInterface(args)
    interface.run()


if __name__ == "__main__":
    argparse()
