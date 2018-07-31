"""Main module, this starts the application"""

from configuration.initialise_configuration import check_configuration
from metrics.packets_send import PacketHandler


class Main():

    def __init__(self):
        """Starts the checking of the configuration file and starts the sending of the packets."""

        check_configuration()
        PacketHandler()

Main()