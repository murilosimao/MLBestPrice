from threading import Thread
import time
from socket import *
from product import Product
from pyvirtualdisplay import Display


display = Display(visible=0, size=(800, 600))
display.start()

class Server:
    def __init__(self):
        self.server_port = 8080
        self.sock = socket(AF_INET, SOCK_DGRAM)
        self.sock.bind(('', self.server_port))
        self.clients_list = []

    def best(self, prod, client_address):
        product = Product(prod.decode('utf-8'))
        result = product.best_product()
        self.sock.sendto(bytes(str(result), "utf-8"), client_address)
    
    def listen_clients(self):
        while True:
            message , client_address = self.sock.recvfrom(2048)
            t = Thread(target=self.best, args=(message, client_address))
            t.daemon = True
            t.start()

if __name__ == "__main__":
    server = Server()
    server.listen_clients()