"""Creates the unique id which will represent the machine in the sent packet"""
import uuid


def create_unique_id():
    """Generates an unique id for one machine"""

    return uuid.uuid4()
