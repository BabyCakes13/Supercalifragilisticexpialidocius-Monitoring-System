"""Main module, this starts the application"""

from initialise.initialise_configuration import initialise
from metrics.collect_metrics import Metrics

initialise()
Metrics()
