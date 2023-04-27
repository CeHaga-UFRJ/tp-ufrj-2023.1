from socket import *

# Dados de conexão
HOST = 'localhost'
PORTA = 5000

# Cria o socket
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORTA))

# Le a mensagem
msg = input()

# Envia a mensagem
sock.send(bytes(msg,  encoding='utf-8'))

# Recebe a mensagem do passivo
msg = sock.recv(1024)

print('Recebido: ' + str(msg,  encoding='utf-8'))

# Fecha o socket
sock.close()
