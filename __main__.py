"""Main module, this starts the application"""

from initialise.initialise_configuration import initialise
from metrics import packets_send

class Main():

    def __init__(self):

        initialise()
        packets_send.PacketHandler()


