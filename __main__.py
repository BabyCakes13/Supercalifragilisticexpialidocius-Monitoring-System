"""Main module, this starts the application"""

from initialise.initialise_configuration import initialise
from metrics import collect_metrics, packets_send

initialise()
packets_send.PacketHandler()
