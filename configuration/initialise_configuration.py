"""Calls the creation and verification of the configuration file"""
from configuration.create_configuration import CreateConfiguration
from configuration.create_unique_id import add_id_to_file


def check_configuration():
    """Initialises the configuration file"""

    CreateConfiguration()
    add_id_to_file()
