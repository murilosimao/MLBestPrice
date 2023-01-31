from re import X
from socket import *
import json
from prettytable import PrettyTable


server_name = 'localhost'
server_port = 8080
client_socket = socket(AF_INET, SOCK_DGRAM)

message = input('Digite o produto desejado: ')
client_socket.sendto(bytes(message, "utf-8"),(server_name, server_port))
answer, server_address = client_socket.recvfrom(2048)

product = answer.decode('utf-8')
product = json.loads(product)

detail = PrettyTable()
detail.field_names = ['titulo', 'valor']

detail.add_row([product['titulo'], product['valor']])

print(detail)
print('\n\n', '=' * 10, ' Link ', '=' * 10)
print(product['link'])

client_socket.close()