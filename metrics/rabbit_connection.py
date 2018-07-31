import pika


class RabbitConnection:
    """Handles the connection to the RabbitMQ server, transmission of packets and closing the channel."""

    def __init__(self, address, port):
        """Creates a connection to the RabbitMQ server using the given port and address and
        opens a queue in which the metrics will be stored for the server to take."""

        connection = pika.BlockingConnection(pika.ConnectionParameters(address, port))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='machine_connection')

    def send_packet(self, packet):
        """Sends given packets to the RabbitMQ queue"""

        self.channel.basic_publish(exchange='',
                                   routing_key='machine_connection',
                                   body=packet)

        print("Packet was sent." + packet)

    def stop_connection(self):
        """Stops the connection to the RabbitMQ server."""

        print("Closed connection.")
        self.channel.close()
