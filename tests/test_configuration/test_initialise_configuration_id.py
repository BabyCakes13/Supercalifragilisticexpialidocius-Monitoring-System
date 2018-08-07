import unittest
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import call
from configuration import initialise_configuration


class TestInitialise(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        cls.manager = Mock()

    @patch('configuration.initialise_configuration.Configuration')
    @patch('configuration.create_unique_id.UniqueID.setup_id_file')
    def test_initialise_configuration_id(self, setup_id_file, configuration):

        self.manager.attach_mock(configuration, 'Configuration')
        self.manager.attach_mock(setup_id_file, 'setup_id_file')

        initialise_configuration.initialise_configuration_id()

        expected_calls = [call.Configuration(), call.setup_id_file()]

        self.assertEqual(self.manager.mock_calls, expected_calls)







