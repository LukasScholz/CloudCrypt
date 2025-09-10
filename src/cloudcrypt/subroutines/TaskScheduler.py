import os
import re
from Exceptions import InvalidArgumentException


class WindowsScheduler:
    ## all functions must be run as administrator

    def __init__(self):
        self.intervals = ("MINUTE", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "ONSTART", "ONLOGON", "ONIDLE")
        self.time_regex = r"^([01]\d|2[0-3]):[0-5]\d$"

    def create_task(self, name: str, path: str):        #,interval: str, time):
        #if interval not in self.intervals:
        #    raise InvalidArgumentException("Unknown Interval!")
        interval = "WEEKLY"
        if not os.path.exists(path):
            raise InvalidArgumentException("Path not Found!")
        #if re.search(self.time_regex, time) is None:
         #   raise InvalidArgumentException("Enter valid Time!")
        time = "00:00"

        #TODO: add alternatives from only sunday midnight

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
        if not os.path.exists(path):
            raise InvalidArgumentException("Path not Found!")
        croncmd = path # Todo add output routing?
        cronline = f"0 0 * * 0  {croncmd}" # Todo: add alternatives from only sunday midnight
        os.system(f'( crontab -l | grep -v -F {croncmd} ; echo {cronline} ) | crontab -')

    def remove_crontab(self, path):
        croncmd = path # Todo add output routing?
        os.system(f'(crontab - l | grep - v - F {croncmd}) | crontab -')
