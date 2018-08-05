"""Calls the creation and verification of the configuration file and ID file"""
from configuration.create_configuration import Configuration
from configuration.create_unique_id import UniqueID


def initialise_configuration_id():
    """Initialises the configuration file and ID file."""

    Configuration()
    unique_id = UniqueID()
    unique_id.setup_id_file()
