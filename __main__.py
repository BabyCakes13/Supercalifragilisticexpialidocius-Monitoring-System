"""Main module, this starts the application"""

from configuration.initialise_configuration import initialise_configuration_id
from metrics.packets_send import PacketHandler


def initialise():
    """Calls the configuration and checking of config.txt.
    Starts reading metrics and sending them to the RabbitMQ server."""

    initialise_configuration_id()
    PacketHandler()


initialise()
