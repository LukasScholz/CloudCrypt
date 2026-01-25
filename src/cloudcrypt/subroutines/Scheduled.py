# This script is only called by the scheduled tasks
import pathlib

from cloudcrypt.subroutines import loader
from cloudcrypt.subroutines import ConfigManager
from cloudcrypt.subroutines.Backup_Creator import BackupCreator

def get_configpath():
    return pathlib.Path(__file__).parent.resolve() / "etc" / "config.csv"


class Scheduled:

    def __init__(self):
        configpath = get_configpath()
        self.loader = loader.Loader(configpath)
        self.config = ConfigManager.Config(configpath)
        self.backup_creator = BackupCreator(configpath)

    def main(self):
        # Mirror Storage
        if self.config.MirrorStorage:
            self.loader.create_storage()
        # Create Backups
        if self.config.CreateBackups:
            self.backup_creator.create_local_backup_cloud()




if __name__ == "__main__":
    scheduler = Scheduled()
    scheduler.main()
