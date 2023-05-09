from socket import *
from dictionary import *

# Dados de conexão
HOST = ''
PORTA = 5000

# Cria o socket
sock = socket(AF_INET, SOCK_STREAM)

# Associa o socket a porta
sock.bind((HOST, PORTA))

# Aguarda conexões
sock.listen(5)
print("Pronto para receber conexões...")

# Aceita a conexão
novoSock, endereco = sock.accept()
print('Conectado com: ', endereco)

while True:

    # Recebe a mensagem do ativo
    msg_rec = novoSock.recv(1024)

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
    novoSock.send(msg_send)

# Fecha os sockets de dados
novoSock.close()
sock.close()
