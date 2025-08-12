from datetime import datetime
from pathlib import Path

import os
from ConfigManager import Config
import shutil


class BackupCreator:

    def __init__(self, config_path):
        self.config = Config(config_path)

    def create_local_backup_cloud(self):
        cloud = Path(self.config.CloudStorage[:-1])
        client = Path(self.config.LocalStorage[:-1])
        backups = Path(str(client) + "/Backups")
        timestamp = datetime.today().strftime("%Y%m%d%H%M%S")

        if not os.path.exists(backups):
            os.makedirs(backups)
        shutil.make_archive(str(backups)+"/"+timestamp, "zip", cloud)

    def load_cloud_from_local_backup(self):
        pass # Todo