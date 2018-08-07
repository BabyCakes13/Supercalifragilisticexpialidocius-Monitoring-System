import unittest
import os
from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import call
from metrics.collect_metrics import Metrics


class TestCollectMetrics(unittest.TestCase):

    def setUp(self):
        self.metric_manager = Metrics()
        self.mock_manager = Mock()

    def test_get_metrics_values(self):

        metrics = list(self.metric_manager.get_metrics_values().keys())
        expected_result = ['Disk_Usage', 'Cpu_Percent', 'Memory_Info', 'Cpu_Stats']

        for index in range(len(metrics)):
            self.assertEqual(metrics[index], expected_result[index])

    @patch('psutil.disk_usage')
    def test_call_metric_functions_disk_usage(self, disk_usage):

        self.mock_manager.attach_mock(disk_usage, 'disk_usage')
        expected_value = [call.disk_usage(os.path.abspath(os.sep))]

        self.metric_manager.call_metric_functions(0)
        self.assertEqual(self.mock_manager.mock_calls, expected_value)

    @patch('psutil.cpu_percent')
    def test_call_metric_functions_cpu_percent(self, cpu_percent):

        self.mock_manager.attach_mock(cpu_percent, 'cpu_percent')
        expected_value = [call.cpu_percent(interval=1, percpu=True)]

        self.metric_manager.call_metric_functions(1)
        self.assertEqual(self.mock_manager.mock_calls, expected_value)

    @patch('psutil.virtual_memory')
    def test_call_metric_functions_virtual_memory(self, cpu_percent):
        self.mock_manager.attach_mock(cpu_percent, 'virtual_memory')
        expected_value = [call.virtual_memory()]

        self.metric_manager.call_metric_functions(2)
        self.assertEqual(self.mock_manager.mock_calls, expected_value)

    @patch('psutil.cpu_stats')
    def test_call_metric_functions_virtual_memory(self, cpu_stats):
        self.mock_manager.attach_mock(cpu_stats, 'cpu_stats')
        expected_value = [call.cpu_stats()]

        self.metric_manager.call_metric_functions(3)
        self.assertEqual(self.mock_manager.mock_calls, expected_value)






