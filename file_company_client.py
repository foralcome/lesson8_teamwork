import company_client as mod_client


def save_company_clients_to_file_csv(clients, file_name='clients.csv', separator=';'):
    with open(file_name, 'w') as file_data:
        for client in clients:
            file_data.write(separator.join(client.values()) + '\n')
    return True


def load_company_clients_from_file_csv(file_name='clients.csv', separator=';'):
    clients = mod_client.get_clients()
    with open(file_name, 'r') as file_data:
        for line_data in file_data:
            client_data = line_data.rstrip().split(separator, len(mod_client.client_data_columns))
            client = mod_client.create(zip(mod_client.client_data_columns, client_data))
            clients.append(client)
    return True