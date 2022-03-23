import json
import socket

from db_manager import *


class Server:

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8000

    def __init__(self):
        server_config = (self.host, self.port)
        self.socket.bind(server_config)
        self.socket.listen(5)
        print(f"Server is listening on port {self.port}")

        self.connection, self.address = self.socket.accept()
        print(f"Connected to {self.address}")

    def send(self, message):
        self.connection.send(message.encode())

    def receive(self):
        '''Receiving connection from the client'''
        try:
            while True:
                data = self.connection.recv(1024).decode()
                return data
        except Exception as ex:
            print("The below error have occured please checkout")
            print(ex)

        return self.connection.recv(1024).decode('utf-8')

    def close(self):
        self.connection.close()


if __name__ == "__main__":

    server = Server()
    while True:
        data = server.receive()

        if data == 'get_products':
            products = get_all_products()
            server.send(json.dumps(products))

        elif data:
            data = json.loads(data)
            add_product(data)
            server.send(f"Product {data['brand']} {data['model']} has been added to the database")

        else:
            break

    server.close()
