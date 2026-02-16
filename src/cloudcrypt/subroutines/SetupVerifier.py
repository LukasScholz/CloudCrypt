import pathlib
import os

from cloudcrypt.subroutines import ConfigManager
from cloudcrypt.subroutines import TaskScheduler


class Verifier:

    def __init__(self):
        pass

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