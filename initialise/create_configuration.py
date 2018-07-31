import os
import re
from files.strings import get_configuration_file_form, get_configuration_file_re


class CreateConfiguration:
    """Class which handles the creation and validity of the configuration file."""

    def __init__(self):

        self.root_path = os.path.dirname(os.path.abspath(__file__))[:-11]
        self.config_path = os.path.join(self.root_path, "files\config.txt")

        if self.check_configuration() is False:
            self.setup_configuration_file()

    def setup_configuration_file(self):
        """Creates the config.txt file, which contains the metrics which are possible to monitor.
        In order to deactivate one metric, write FALSE instead of TRUE"""

        with open(self.config_path, "w+") as f_config:

            f_config.write(get_configuration_file_form())

    def validate_configuration_file(self):
        """Checks whether the structure of the configuration file is correct"""

        f_config = open(self.config_path, "r")

        if re.search(get_configuration_file_re(), f_config.read()) is None:
            return False
        else:
            return True

    def check_configuration(self):
        """Checks to see if the configuration file already exists and it's valid, and creates another if it doesn't"""

        if os.path.isfile(self.config_path) and self.validate_configuration_file() is True:
            return True

        return False
