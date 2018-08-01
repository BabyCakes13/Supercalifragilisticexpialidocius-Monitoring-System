import json
from threading import Timer
from socket import gaierror
from datetime import datetime
from metrics.rabbit_connection import RabbitConnection
from metrics.collect_metrics import Metrics
from configuration.read_configuration_data import ConfigurationFileReader
from configuration.create_unique_id import create_unique_id
from configuration.create_configuration import CreateConfiguration


class PacketHandler:
    """Handles the sending of the packets formed from metric values and id to the rabbit mq server,
    based on the configured send time."""

    def __init__(self):
        """Creates the dictionary containing the collected metrics, unique id and the time when the object was sent.
        Uses the given port and address to connect to the rabbit queue and sends the metrics dictionary."""

        self.metrics = Metrics()
        self.config_checker = CreateConfiguration()
        self.reader = ConfigurationFileReader()

        self.metrics_values = self.metrics.get_metrics_dictionary()
        self.send_time = self.reader.get_send_time()
        self.address = self.reader.get_address()
        self.port = self.reader.get_port()
        self.unique_id = create_unique_id()
        self.metrics_values['unique_id'] = str(self.unique_id)

        try:
            self.connection = RabbitConnection(address=self.address,
                                               port=self.port)
        except(gaierror, AttributeError, ConnectionError):
            print("Wrong IP")

        self.add_metrics_to_packet()

    def add_metrics_to_packet(self):
        """Updates the send time and metrics. Calls itself in a loop based on the given send_time from config.txt.
        Adds the time when the package was sent and updates it.
        Send the packed formed of the metrics and id to the rabbit mq queue"""

        self.config_checker = CreateConfiguration()
        self.send_time = self.reader.get_send_time()
        self.metrics_values = self.metrics.get_metrics_dictionary()

        sent_time = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.metrics_values['send_time'] = str(sent_time)

        self.connection.send_packet(json.dumps(self.metrics_values, indent=1))

        pid = Timer(int(self.send_time),
                    self.add_metrics_to_packet)

        pid.start()
