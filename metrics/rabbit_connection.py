import pika


class RabbitConnection:

    def __init__(self, address, port):

        connection = pika.BlockingConnection(pika.ConnectionParameters(address, port))
        self.channel = connection.channel()
        self.channel.queue_declare(queue='machine_connection')

    def send_packet(self, packet):

        self.channel.basic_publish(exchange='',
                                   routing_key='machine_connection',
                                   body=packet)

        print("Packet was sent." + packet)

    def stop_connection(self):

        print("Closed connection.")
        self.channel.close()
