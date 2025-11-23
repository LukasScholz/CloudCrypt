# This script is only called by the scheduled tasks
import pathlib

from cloudcrypt.subroutines import loader


def get_configpath():
    return pathlib.Path(__file__).parent.resolve() / "etc" / "config.csv"


class Scheduled:

    def __init__(self):
        self.loader = None

    def main(self):
        configpath = get_configpath()
        self.loader = loader.Loader(configpath)
        self.loader.create_storage()


if __name__ == "__main__":
    scheduler = Scheduled()
    scheduler.main()
