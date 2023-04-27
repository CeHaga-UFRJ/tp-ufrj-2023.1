data = {}


def populate_data():
    data['Redes de Computadores'] = 'Computer Networks'
    data['Enlace'] = 'Link'
    data['Conexão'] = 'Connection'
    data['Pacote'] = 'Packet'
    data['Roteador'] = 'Router'
    data['Mensagem'] = 'Message'
    data['Porta'] = 'Port'
    data['Protocolo'] = 'Protocol'
    data['Servidor'] = 'Server'
    data['Cliente'] = 'Client'


def translate(word):
    if (data == {}):
        populate_data()

    if (word in data):
        return data[word]
    else:
        return None
