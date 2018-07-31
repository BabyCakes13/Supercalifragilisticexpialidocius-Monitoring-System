import pika
import json
import sys
from threading import Timer
from socket import gaierror
from metrics.rabbit_connection import RabbitConnection
from metrics.collect_metrics import Metrics
from files.read_configuration_data import ConfigurationFileReader
from initialise.create_unique_id import create_unique_id


class PacketHandler:

    def __init__(self):

        self.packet = {}

        metrics = Metrics()
        self.metrics = metrics.get_metrics_dictionary()
        self.reader = ConfigurationFileReader()
        self.metrics = {}
        self.send_time = self.reader.get_send_time()
        self.address = self.reader.get_address()
        self.port = self.reader.get_port()
        self.unique_id = create_unique_id()

        try:
            self.connection = RabbitConnection(address=self.address,
                                               port=self.port)
        except(gaierror, AttributeError):
            print("Wrong shit")

        self.start_packet_loop()

    def start_packet_loop(self):

        self.add_metrics_to_packet(self.metrics, self.send_time)

    def add_metrics_to_packet(self, metrics, send_time):

        reader = ConfigurationFileReader()
        metrics = Metrics()

        self.send_time = reader.get_send_time()
        self.metrics = metrics.get_metrics_dictionary()
        self.metrics['unique_id'] = str(self.unique_id)
        self.connection.send_packet(json.dumps(self.metrics, indent=1))

        pid = Timer(int(send_time),
                    self.add_metrics_to_packet,
                    args=(metrics, send_time,))

        pid.start()
