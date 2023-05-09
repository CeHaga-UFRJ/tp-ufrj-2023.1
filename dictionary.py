data = {}


def populate_data():
    data['redes de computadores'] = 'Computer Networks'
    data['enlace'] = 'Link'
    data['conexão'] = 'Connection'
    data['pacote'] = 'Packet'
    data['roteador'] = 'Router'
    data['mensagem'] = 'Message'
    data['porta'] = 'Port'
    data['protocolo'] = 'Protocol'
    data['servidor'] = 'Server'
    data['cliente'] = 'Client'


def translate(word):
    if (data == {}):
        populate_data()

    lower_word = word.lower()

    if (lower_word in data):
        return data[lower_word]
    else:
        return None
