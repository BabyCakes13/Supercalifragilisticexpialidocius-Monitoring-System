import os
import re


class ConfigurationFileReader:
    """Class which handles reading metrics from the configuration file"""

    def __init__(self):
        """Contains the path to the config.txt file."""

        self.config_path = os.path.dirname(os.path.abspath(__file__))[:-5] + "files\config.txt"

    def get_send_time(self):
        """Returns the send_time variable set in configuration file."""

        f_config = open(self.config_path, "r")

        send_time = re.search(r"SEND_TIME=[1-9]", f_config.read()).group()[10:]

        f_config.close()
        return send_time

    def get_metrics(self):
        """Returns the chosen option for the metrics in the configuration file."""

        f_config = open(self.config_path, "r")

        metric_group = re.search(r"DISK_USAGE=(TRUE|FALSE)" +
                                 r"\nCPU_PERCENT=(TRUE|FALSE)" +
                                 r"\nMEMORY_INFO=(TRUE|FALSE)" +
                                 r"\nCPU_STATS=(TRUE|FALSE)", f_config.read())

        metrics = [metric_group.group(1),
                   metric_group.group(2),
                   metric_group.group(3),
                   metric_group.group(4)]

        f_config.close()
        return metrics
