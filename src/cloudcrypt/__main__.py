import argparse
import os.path
import shutil
import sys
import pathlib

from cloudcrypt import __version__
from cloudcrypt.subroutines import ConfigManager
from cloudcrypt.subroutines import cryptor
from cloudcrypt.subroutines import TaskScheduler


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
        if self.arguments.verifysetup:
            self.verify_setup()
        configpath = pathlib.Path(__file__).parent.resolve() / "etc" / "config"
        self.config = ConfigManager.Config(configpath)
        if self.arguments.addkey:
            self.addkey()
        if self.arguments.loadkeys is not None:
            self.loadkeys(self.arguments.loadkeys)
        if self.arguments.schedule:
            self.add_scheduler()
        if self.arguments.removeschedule:
            self.remove_scheduler()

    def display_version(self):
        print("CloudCrypt version " + __version__)
        exit(0)

    def display_configpath(self):
        print(pathlib.Path(__file__).parent.resolve() / "etc" / "config")
        exit(0)

    def addkey(self):
        encryptor = cryptor.Encryption(self.config)
        encryptor.add_key()

    def loadkeys(self, newkeys):
        keyfile = self.config.KeyFile
        shutil.copyfile(newkeys, keyfile)

    def add_scheduler(self):
        scheduler = TaskScheduler.LinuxScheduler()  # Todo add check for Windows
        scheduler.create_task()

    def remove_scheduler(self):
        scheduler = TaskScheduler.LinuxScheduler()  # Todo add check for Windows
        scheduler.remove_task()

    def verify_setup(self):
        # Checks for valid setup
        # See if config exists
        configpath = pathlib.Path(__file__).parent.resolve() / "etc" / "config"
        result = configpath.exists()
        print(f"Config exists: {result}")
        if not result:
            exit(1)
        # See if keys are added
        config = ConfigManager.Config(configpath)
        keyfile = config.KeyFile
        result = pathlib.Path(keyfile).exists()
        print(f"Keyfile exists: {result}")
        if not result:
            exit(1)
        result = os.path.getsize(keyfile) != 0
        print(f"Keys are added: {result}")
        if not result:
            exit(1)
        # See if scheduler is added and active
        scheduler = TaskScheduler.LinuxScheduler()  # Todo add check for Windows
        result = scheduler.check_task()
        print(f"Scheduler is added: {result}")
        if not result:
            exit(1)
        result = scheduler.check_enabled()
        print(f"Scheduler is enabled: {result}")
        if not result:
            exit(1)
        result = scheduler.check_active()
        print(f"Scheduler is running: {result}")
        if not result:
            exit(1)
        exit(0)


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        print(f'Error: {message}\n\n\n')
        self.print_help()
        sys.exit(1)


def argparse():
    parser = CustomArgumentParser(description="Encrypted Backup-creator, mainly for Cloud usage")

    # arguments without value
    parser.add_argument("--addkey", "-a", action="store_true", help="Generate a new key File")
    parser.add_argument("--verifysetup", action="store_true", help="Verify Setup of Config File")
    parser.add_argument("--config", "-c", action="store_true", help="Get config file path")
    parser.add_argument("--schedule", "-s", action="store_true", help="schedule a recurring task")
    parser.add_argument("--removeschedule", "-r", action="store_true", help="remove the scheduled task")

    # arguments with value
    parser.add_argument("--loadkeys", "-l", help="Load keys from existing Keyfile")

    # optional arguments
    parser.add_argument("--version", "-v", action="store_true", help="prints version info and exit")
    args = parser.parse_args()
    interface = MainInterface(args)
    interface.run()


if __name__ == "__main__":
    argparse()
