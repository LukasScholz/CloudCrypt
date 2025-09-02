import os
import re
from src.CloudCrypt.subroutines.Exceptions import InvalidArgumentException


class WindowsScheduler:
    ## all functions must be run as administrator

    def __init__(self):
        self.intervals = ("MINUTE", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "ONSTART", "ONLOGON", "ONIDLE")
        self.time_regex = r"^([01]\d|2[0-3]):[0-5]\d$"

    def create_task(self, name: str, interval: str, path: str, time):
        if interval not in self.intervals:
            raise InvalidArgumentException("Unknown Interval!")
        if not os.path.exists(path):
            raise InvalidArgumentException("Path not Found!")
        if re.search(self.time_regex, time) is None:
            raise InvalidArgumentException("Enter valid Time!")

        # All arguments are valid!
        os.system(f'SchTasks /Create /SC {interval} /TN {name} /TR {path} /ST {time}')

    def remove_task(self, name: str):
        # assume that the name is associated with an existing task
        os.system(f'SchTasks /DELETE /TN {name}')

class LinuxScheduler:
    ## uses crontab for scheduling

    # Cron line specifics
    #   * * * * * "command to be executed"
    #   - - - - -
    #   | | | | |
    #   | | | | ----- Day of week (0 - 7) (Sunday=0 or 7)
    #   | | | ------- Month (1 - 12)
    #   | | --------- Day of month (1 - 31)
    #   | ----------- Hour (0 - 23)
    #   ------------- Minute (0 - 59)

    def __init__(self):
        pass

    def create_crontab(self, path):
        croncmd = path # Todo add output routing?
        cronline = f"* * * * * {croncmd}" # Todo: add arguments to fix * placeholders
        os.system(f'( crontab -l | grep -v -F {croncmd} ; echo {cronline} ) | crontab -')
        # Todo: check Arguments!

    def remove_crontab(self, path):
        croncmd = path # Todo add output routing?
        os.system(f'(crontab - l | grep - v - F {croncmd}) | crontab -')
