import shutil
import unittest
import os
from pathlib import Path

from CloudCrypt.subroutines.ConfigManager import Config
from CloudCrypt.subroutines.cryptor import Encryption
from CloudCrypt.subroutines.loader import Loader
from CloudCrypt.subroutines.Backup_Creator import BackupCreator

# constants
CONFIGPATH = "test/testconfig.csv"


class MyTestCase(unittest.TestCase):
    def test_create_local_backup(self):
        config = Config(CONFIGPATH)
        backup_creator = BackupCreator(CONFIGPATH)
        shutil.rmtree(Path(str(config.LocalStorage) + "/Backups"))
        backup_creator.create_local_backup_cloud()
        dirs = os.listdir(Path(str(config.LocalStorage) + "/Backups"))
        self.assertNotEqual(len(dirs), 0)

    def test_load_local_backup(self):
        config = Config(CONFIGPATH)
        backup_creator = BackupCreator(CONFIGPATH)
        backup_creator.create_local_backup_cloud()
        if len(os.listdir(Path(str(config.LocalStorage) + "/Backups"))) == 0:
            self.skipTest("Failed to create the Backup!")
        shutil.move(config.CloudStorage, Path(str(config.CloudStorage) + "/../temp"))
        backup_creator.load_cloud_from_local_backup()
        backup_creator.delete_local_backup()
        self.assertEqual(len(os.listdir(Path(config.CloudStorage))),
                         len(os.listdir(Path(str(config.CloudStorage) + "/../temp"))))
        shutil.rmtree(Path(str(config.CloudStorage) + "/../temp"))


if __name__ == '__main__':
    unittest.main()
