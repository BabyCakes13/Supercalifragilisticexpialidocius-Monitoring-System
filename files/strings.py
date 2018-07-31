"""Module which contains strings used in the project"""


def get_configuration_file_form():
    """Contains the structure of the configuration file used by the client to choose the metrics"""

    return "DISK_USAGE=TRUE" \
        "\nCPU_PERCENT=TRUE" \
        "\nMEMORY_INFO=TRUE" \
        "\nCPU_STATS=TRUE" \
        "\nSEND_TIME=5"


def get_configuration_file_re():
    """Contain the regex expression to check the validity of the configuration file"""

    return r"DISK_USAGE=(TRUE|FALSE)" \
        r"\nCPU_PERCENT=(TRUE|FALSE)" \
        r"\nMEMORY_INFO=(TRUE|FALSE)" \
        r"\nCPU_STATS=(TRUE|FALSE)" \
        r"\nSEND_TIME=5"
