from socket import *
from dictionary import *

# Dados de conexão
PORTA = 5000

# Cria o socket
sock = socket(AF_INET, SOCK_DGRAM)

# Associa o socket a porta
sock.bind(('', PORTA))

print("Pronto para receber conexões...")

while True:
    msg_rec, addr = sock.recvfrom(1024)

    if not msg_rec:
        break

    # Converte a mensagem para string
    msg_str = str(msg_rec,  encoding='utf-8')
    print('Mensagem recebida: ' + msg_str)

    # Traduz a mensagem
    msg_trad = translate(msg_str)

    if (msg_trad == None):
        msg_trad = 'Palavra não encontrada'

    # Converte a mensagem para bytes
    msg_send = bytes(msg_trad,  encoding='utf-8')

    # Envia a mensagem de volta
    sock.sendto(msg_send, addr)

# Fecha o socket
sock.close()
