"""Module which holds unit tests for collect_metrics"""
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from unittest.mock import call
from metrics.collect_metrics import Metrics


class TestCollectMetrics(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.collector = Metrics()

    def test_get_disk_usage(self):
        """Tests if the get_disk_usage calls the correct psutil function."""

        with patch('psutil.disk_usage') as mocker:
            self.collector.get_disk_usage()

        mocker.assert_called()

    def test_get_cpu_percent(self):
        """Tests if the get_disk_usage calls the correct psutil function."""

        with patch('psutil.cpu_percent') as mocker:
            self.collector.get_cpu_percent()

        mocker.assert_called()

    def test_get_memory_info(self):
        """Tests if the get_disk_usage calls the correct psutil function."""

        with patch('psutil.virtual_memory') as mocker:
            self.collector.get_memory_info()

        mocker.assert_called()

    def test_get_cpu_stats(self):
        """Tests if the get_disk_usage calls the correct psutil function."""

        with patch('psutil.cpu_stats') as mocker:
            self.collector.get_cpu_stats()

        mocker.assert_called()
