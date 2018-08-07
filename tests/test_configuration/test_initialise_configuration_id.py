"""Unit tests for the initialise_configuration module."""
import unittest
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import call
from configuration import initialise_configuration


class TestInitialise(unittest.TestCase):
    """Tests the correct functioning of the initialise_configuration module."""

    @classmethod
    def setUpClass(cls):
        """Initialises the Mock object for testing."""

        cls.manager = Mock()

    @patch('configuration.initialise_configuration.Configuration')
    @patch('configuration.create_unique_id.UniqueID.setup_id_file')
    def test_ici(self, setup_id_file, configuration):
        """Tests if the initialise_configuration_id function
        calls the correct functions in the correct order."""

        self.manager.attach_mock(configuration, 'Configuration')
        self.manager.attach_mock(setup_id_file, 'setup_id_file')

        initialise_configuration.initialise_configuration_id()

        expected_calls = [call.Configuration(), call.setup_id_file()]

        self.assertEqual(self.manager.mock_calls, expected_calls)
