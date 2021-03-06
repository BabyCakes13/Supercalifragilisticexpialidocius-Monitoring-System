"""Module which handles reading the options
for each metric from the config.txt file,
collecting metrics from the PC and
creating the metric values array"""

import os
import psutil
from configuration.read_configuration_data import ReaderHandler
from files.strings import get_data_names


class Metrics:
    """Class which handles the metrics"""

    def __init__(self):
        """Reads the options for each metric.
        Creates array of metric functions."""

        reader = ReaderHandler()

        self.metrics = reader.get_metrics()
        self.send_time = reader.get_send_time()
        self.metric_values = {}

    def get_metrics_values(self):
        """Gets the disk usage, cpu_percent, memory_info
        and cpu_stats using psutil functions.
        Takes the metrics on the machine for each
        TRUE metric in the configuration file."""

        for index in range(len(self.metrics)):
            if self.metrics[index] == "TRUE":

                self.call_metric_functions(index=index)

        return self.metric_values

    def call_metric_functions(self, index):
        """Calls the right functions for each metric name."""

        if index == 0:
            self.metric_values[get_data_names()[0]] = \
                psutil.disk_usage(os.path.abspath(os.sep))
        elif index == 1:
            self.metric_values[get_data_names()[1]] = \
                psutil.cpu_percent(interval=1, percpu=True)
        elif index == 2:
            self.metric_values[get_data_names()[2]] = \
                psutil.virtual_memory()
        elif index == 3:
            self.metric_values[get_data_names()[3]] = \
                psutil.cpu_stats()
        else:
            print("Wrong value given to the metric name.")
            exit(2)
