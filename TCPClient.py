from socket import *

# Dados de conexão
HOST = 'localhost'
PORTA = 5000

# Cria o socket
sock = socket(AF_INET, SOCK_STREAM)
sock.connect((HOST, PORTA))

print('Dicionário remoto. Entre com a palavra a ser traduzida. Entre com \'fim\' para encerrar.')

while True:
    # Le a mensagem
    msg = input('\nEntre com a palavra a ser traduzida: ')

    if (msg == 'fim'):
        break

    # Envia a mensagem
    sock.send(bytes(msg,  encoding='utf-8'))

    # Recebe a mensagem do passivo
    msg = sock.recv(1024)

    print('Tradução: ' + str(msg,  encoding='utf-8'))

# Fecha o socket
sock.close()
