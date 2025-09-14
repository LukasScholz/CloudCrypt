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
        sys.exit(2)


def argparse():
    parser = CustomArgumentParser(description="Encrypted Backup-creator, mainly for Cloud usage")

    # required arguments
    parser.add_argument("--source", "-s", help="Path of local directory")
    parser.add_argument("--target", "-t", help="Path of mounted cloud directory")
    parser.add_argument("--config", "-c", help="Get config file path") # Todo add modifiable steam

    # optional arguments
    parser.add_argument("--version", "-v", action="store_true", help="prints version info and exit")
    args = parser.parse_args()
    interface = MainInterface(args)
    interface.run()


if __name__ == "__main__":
    argparse()
