from socket import *

# Dados de conexão
HOST = 'localhost'
PORTA = 5000

# Cria o socket
sock = socket(AF_INET, SOCK_DGRAM)

print('Dicionário remoto usando UDP. Entre com a palavra a ser traduzida. Entre com \'fim\' para encerrar.')

while True:
    # Le a mensagem
    msg = input('\nEntre com a palavra a ser traduzida: ')

    if (msg == 'fim'):
        break

    # Envia a mensagem
    sock.sendto(bytes(msg,  encoding='utf-8'), (HOST, PORTA))

    # Recebe a mensagem do passivo
    msg, _ = sock.recvfrom(1024)

    print('Tradução: ' + str(msg,  encoding='utf-8'))

# Fecha o socket
sock.close()
