"""Module which handles the creation and transmission of packets.
Packets are formed of metric values collected from the PC, changing based on
the send time set in config.txt file, the unique id representing the machine
and the time at which each packet was sent."""
import json
from threading import Timer
from datetime import datetime
from files.strings import get_sent_time_format, get_data_names
from metrics.rabbit_connection import RabbitConnection
from metrics.collect_metrics import Metrics
from configuration.read_configuration_data import ConfigurationFileReader
from configuration.create_unique_id import UniqueID


class PacketHandler:
    """Handles the sending of the packets formed from
    metric values and id to the rabbit mq server,
    based on the configured send time."""

    def __init__(self):
        """Creates the dictionary containing the collected metrics,
        unique id and the time when the object was sent.
        Uses the given port and address to connect to the rabbit queue
        and sends the metrics dictionary."""

        self.reader = ConfigurationFileReader()
        self.packet = {}
        self.rabbit_connection = False
        self.address = self.reader.get_address()
        self.port = self.reader.get_port()

        unique_id = UniqueID()
        self.packet[get_data_names()[4]] = str(unique_id.read_id())

        self.set_packet_data()

    def set_packet_data(self):
        """Stores data which is not changing in the class attributes.
        Adds the id of the machine to the sent packet."""

        try:
            self.rabbit_connection = \
                RabbitConnection(address=self.address, port=self.port)
        except(AttributeError, ConnectionError):
            print("Connection Error.")

        self.send_packets()

    def send_packets(self):
        """Updates the send time and metrics. Calls itself in a loop based on
        the given send_time from config.txt.
        Adds the time when the package was sent and updates it.
        Send the packed formed of the metrics and id to the rabbit mq queue"""

        metrics = Metrics()
        sent_time = str(datetime.now().strftime(get_sent_time_format()))

        self.packet.update(metrics.get_metrics_values())
        self.packet[get_data_names()[5]] = sent_time

        self.rabbit_connection.send_packet(json.dumps(self.packet, indent=1))

        lopper = Timer(int(self.reader.get_send_time()), self.send_packets)
        lopper.start()
