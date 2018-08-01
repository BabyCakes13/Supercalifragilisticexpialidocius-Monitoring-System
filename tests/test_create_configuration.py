"""Contains the tests for the create_configuration module"""
import unittest
import os
from configuration.create_configuration import CreateConfiguration
from files.strings import get_configuration_file_form


class TestCreateConfigurationFile(unittest.TestCase):

    def setUp(self):

        self.root_path = os.path.dirname(os.path.abspath(__file__))[:-5]
        self.config_path = os.path.join(self.root_path, "files\config.txt")

        self.f_config = open(self.config_path, "r+")

        self.test = CreateConfiguration()

    def tearDown(self):

        self.f_config.close()

    def test_validate_structure(self):
        """Tests if the validate_structure() function the file structure is correctly handled."""

        self.f_config.write(get_configuration_file_form())

        self.assertEqual(self.test.validate_configuration_file(), True)
        self.f_config.close()

        self.f_config = open(self.config_path, "w")
        self.f_config.write("This will be bad.")

        self.assertEqual(self.test.validate_configuration_file(), False)

        self.f_config.close()

    def test_check_configuration(self):
        """Tests if the check_configuration() function creates, verifies and writes the file correctly."""

        self.test.check_configuration()

        self.assertEqual(os.path.isfile(self.config_path), 1)

        self.f_config = open(self.config_path, "r+")
        self.assertEqual(self.f_config.read(), get_configuration_file_form())
