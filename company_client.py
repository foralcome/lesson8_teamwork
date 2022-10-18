clients = None
count_clients = 0
client_data_columns = {'id': 'Id', 'soname': 'Фамилия', 'name': 'Имя', 'email': 'E-mail',
                       'date_birthday': 'Дата рождения', 'phone': 'Телефон', 'description': 'Примечание'}


def init(new_clients=None):
    global clients
    if isinstance(new_clients, list):
        clients = new_clients
    else:
        clients = []

    global count_clients
    count_clients = len(clients)


def get_count_clients():
    return count_clients


def get_clients():
    return clients


def add_client(client):
    global clients
    global count_clients

    if clients is None:
        clients = []

    clients.append(client)
    count_clients += 1
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
    global count_clients

    if clients is None:
        return False

    for i in range(len(clients)):
        if clients[i][column] == value:
            clients.pop(i)
            count_clients -= 1
            return True
    return False
