"""Creates the unique id which will represent the machine in the sent packet"""
import uuid
import os
import re
from files.strings import get_id_re


def create_unique_id():
    """Generates an unique id for one machine"""

    return uuid.uuid4()


def add_id_to_file():
    """Adds the machine ID to file. If it gets changed,
    it will be overwritten."""

    root_path = os.path.dirname(os.path.abspath(__file__))[:-14]
    id_path = os.path.join(root_path, "files\\id.txt")

    with open(id_path, "w+") as f_id:

        if re.search(get_id_re(), f_id.read()) is None:

            f_id.write(str(create_unique_id()))
