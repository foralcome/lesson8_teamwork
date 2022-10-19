import company_client as mod_client
import os.path

def save_company_clients_to_file_csv(file_name='clients.csv', separator=';'):
    with open(file_name, 'w') as file_data:
        clients = mod_client.get_clients()
        if clients is not None:
            for client in clients:
                file_data.write(separator.join(client.values()) + '\n')
    return True


def load_company_clients_from_file_csv(file_name='clients.csv', separator=';'):
    if not os.path.exists(file_name):
        return False

    clients = []
    with open(file_name, 'r') as file_data:
        for line_data in file_data:
            client_data = line_data.rstrip().split(separator)
            if len(client_data) != len(mod_client.client_data_columns):
                continue
            clients.append(dict(zip(mod_client.client_data_columns, client_data)))
        mod_client.init(clients)
    return True
