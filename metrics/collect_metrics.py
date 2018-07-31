from files.read_configuration_data import ConfigurationFileReader
import psutil
import os


class Metrics:
    """Class which handles the metrics"""

    def __init__(self):
        """Reads the options for each metric. Creates array of metric functions."""

        reader = ConfigurationFileReader()

        self.metrics = reader.get_metrics()
        self.send_time = reader.get_send_time
        self.metric_types = {}
        self.metric_functions = [self.get_disk_usage,
                                 self.get_cpu_percent,
                                 self.get_memory_info,
                                 self.get_cpu_stats]

        for index in range(len(self.metric_functions)):
            self.metric_functions[index]()

        print(self.metric_types)

    def get_disk_usage(self):
        """Gets the disk usage information"""
        self.metric_types['disk_usage'] = psutil.disk_usage(os.path.abspath(os.sep))

    def get_cpu_percent(self):
        """Gets the cou percent information"""
        self.metric_types['cpu_percent'] = psutil.cpu_percent(interval=1, percpu=True)

    def get_memory_info(self):
        """Gets the memory information"""
        self.metric_types['memory_info'] = psutil.virtual_memory()

    def get_cpu_stats(self):
        """Gets cpu status information"""
        self.metric_types['cpu_stats'] = psutil.cpu_stats()
