from datetime import datetime
from pathlib import Path

import os
from src.subroutines.ConfigManager import Config
import shutil


class BackupCreator:

    def __init__(self, config_path):
        self.config = Config(config_path)

    def create_local_backup_cloud(self):
        cloud = Path(self.config.CloudStorage)
        client = Path(self.config.LocalStorage)
        backups = Path(str(client) + "/Backups")
        timestamp = datetime.today().strftime("%Y%m%d%H%M%S")

        if not os.path.exists(backups):
            os.makedirs(backups)
        shutil.make_archive(str(backups)+"/"+timestamp, "zip", cloud)

    def load_cloud_from_local_backup(self, timestamp=None):
        cloud = Path(self.config.CloudStorage)
        client = Path(self.config.LocalStorage)
        backups = Path(str(client) + "/Backups")
        if timestamp is None:
            to_load = Path(str(backups) + "/" + os.listdir(backups)[-1])
        else:
            to_load = Path(str(backups) + "/" + str(timestamp) + ".zip")
        shutil.unpack_archive(to_load, cloud, "zip")

    def delete_local_backup(self, timestamp=None):
        client = Path(self.config.LocalStorage)
        backups = Path(str(client) + "/Backups")
        if timestamp is None:
            to_delete = Path(str(backups) + "/" + os.listdir(backups)[-1])
        else:
            to_delete = Path(str(backups) + "/" + str(timestamp) + ".zip")
        os.remove(to_delete)
