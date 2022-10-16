clients = None
client_data_columns = {'id': 'Id', 'soname': 'Фамилия', 'name': 'Имя', 'email': 'E-mail',
                       'date_birthday': 'Дата рождения', 'phone': 'Телефон', 'description': 'Примечание'}


def init(new_clients=None):
    global clients
    if isinstance(new_clients, dict):
        clients = new_clients
    else:
        clients = {}


def create(id, soname, name, post, date_birthday, phone, description=''):
    return {
        'id': id,
        'soname': soname,
        'name': name,
        'post': post,
        'date_birthday': date_birthday,
        'phone': phone,
        'description': description
    }


def get_clients():
    return clients


def add_client(client):
    global clients

    if clients is None:
        clients = []

    clients.append(client)
    return True


def find_client_by(column, value):
    global clients

    if clients is None:
        return None

    for client in clients:
        if client[column] == value:
            return client
    return None


def delete_client_by(column, value):
    global clients

    if clients is None:
        return False

    for i in range(len(clients)):
        if clients[i][column] == value:
            clients.pop(i)
            return True
    return False
