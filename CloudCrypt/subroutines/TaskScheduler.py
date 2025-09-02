import os
import re
from CloudCrypt.subroutines.Exceptions import InvalidArgumentException


class WindowsScheduler:

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
