import argparse
import sys

import CloudCrypt.subroutines.ConfigManager
from __version__ import __version__


class MainInterface:

    def __init__(self, args):
        self.arguments = args
        self.config = None  # value set during runtime

    def run(self):
        if self.arguments.version:
            self.display_version()
        self.config = CloudCrypt.subroutines.ConfigManager.Config(self.arguments.config)

    def display_version(self):
        print("CloudCrypt version " + __version__)
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
    parser.add_argument("--config", "-c", help="Path of the config file")

    # optional arguments
    parser.add_argument("--version", "-v", action="store_true", help="prints version info and exit")
    args = parser.parse_args()
    interface = MainInterface(args)
    interface.run()


if __name__ == "__main__":
    argparse()
