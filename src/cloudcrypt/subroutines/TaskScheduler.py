import os
import pathlib
import shutil

from cloudcrypt.subroutines.Exceptions import InvalidArgumentException


class WindowsScheduler:
    ## all functions must be run as administrator

    def __init__(self):
        self.intervals = ("MINUTE", "HOURLY", "DAILY", "WEEKLY", "MONTHLY", "ONSTART", "ONLOGON", "ONIDLE")
        self.time_regex = r"^([01]\d|2[0-3]):[0-5]\d$"

    def create_task(self, name: str, path: str):  # ,interval: str, time):
        # if interval not in self.intervals:
        #    raise InvalidArgumentException("Unknown Interval!")
        interval = "WEEKLY"
        if not os.path.exists(path):
            raise InvalidArgumentException("Path not Found!")
        # if re.search(self.time_regex, time) is None:
        #   raise InvalidArgumentException("Enter valid Time!")
        time = "00:00"

        # TODO: add alternatives from only sunday midnight

        # All arguments are valid!
        os.system(f'SchTasks /Create /SC {interval} /TN {name} /TR {path} /ST {time}')

    def remove_task(self, name: str):
        # assume that the name is associated with an existing task
        os.system(f'SchTasks /DELETE /TN {name}')


class LinuxScheduler:
    # uses systemctl for scheduling
    # backup every time the system is restarted

    def __init__(self):
        XDG_RUNTIME_DIR = os.environ["XDG_RUNTIME_DIR"]
        self.systemd_unit_search_path = XDG_RUNTIME_DIR + "/systemd/transient/cloudcrypt.service"
        self.servicepath = pathlib.Path(__file__).parent.parent.resolve() / "etc" / "cloudcrypt.service"

    def create_task(self):
        self.servicepath.write_text(self.servicepath.read_text().replace("$ScriptPath",
                                                                         str(pathlib.Path(
                                                                             __file__).parent.resolve() / "Scheduled.py")))
        shutil.copyfile(self.servicepath, self.systemd_unit_search_path)
        print("Please run the following commands to start and enable the task:")
        print("$ systemctl --user start cloudcrypt")
        print("$ systemctl --user enable cloudcrypt")

    def remove_task(self):
        os.remove(self.systemd_unit_search_path)
        print("The following service has been removed: " + self.systemd_unit_search_path)

    def check_task(self):
        return pathlib.Path(self.systemd_unit_search_path).exists()

    def check_active(self):
        return os.system("systemctl --user is-active cloudcrypt.service")

    def check_enabled(self):
        return os.system("systemctl --user is-enabled cloudcrypt.service")

