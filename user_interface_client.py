import id_generator as mod_id
import company_client as mod_client
import file_company_client as mod_file_client

import user_interface_menu as ui_menu


# КЛИЕНТЫ - 0 Показать клиента
def print_company_client(client):
    print('\nКлиент организации:')
    for client_data_column in mod_client.client_data_columns:
        print(f'{mod_client.client_data_columns[client_data_column]}: {client[client_data_column]}')


def print_company_client_mini(client):
    print(f"UUID: {client['id']}")
    print(f"ФИО: {client['soname']} {client['soname']}")
    print(f"Контакты: {client['phone']}, e-mail {client['email']}")


# КЛИЕНТЫ - 1 Показать кол-во клиентов
def print_count_company_clients():
    print('\n1) В организации:', mod_client.get_count_clients(), 'клиентов')


# КЛИЕНТЫ - 2 Показать клиентов
def print_company_clients():
    print('\n2) Клиенты организации:')
    if mod_client.get_count_clients() == 0:
        print('в компании нет клиентов')
    else:
        for client in mod_client.get_clients():
            print_company_client(client)


# КЛИЕНТЫ - 3 Добавить клиента
def add_company_client():
    print('\n3) Добавление клиента:')
    clients = mod_client.get_clients()

    new_client = {}
    for data_key in mod_client.client_data_columns:
        if data_key == 'id':
            new_client[data_key] = mod_id.get_uuid_string()
            continue
        new_client[data_key] = input(f'Введите {data_key}:')
    check = input("всё верно? (введите '1' если да или '0' для отмены): ")
    if not check.isdigit() or int(check) != 1:
        return False

    clients.append(new_client)
    mod_client.count_clients += 1
    return True


# КЛИЕНТЫ - 4 Редактировать клиента
def edit_company_client():
    return False


# КЛИЕНТЫ - 5 Удалить клиента
def delete_company_client():
    print('\n5) Удаление клиента:')
    ui_menu.print_menu('Способ удаления', mod_client.client_data_columns)
    find_column = ui_menu.get_select_menu(mod_client.client_data_columns)
    find_str = input(f'Введите {mod_client.client_data_columns[find_column]} клиента:')

    if mod_client.find_client_by(find_column, find_str):
        mod_client.delete_client_by(find_column, find_str)
    else:
        print(f'Сотрудника с {find_column} = {find_str} не найден!')
        return False
    return True


# КЛИЕНТЫ - 6 Найти клиента
def find_company_client():
    print('\n6) Найти клиента:')
    ui_menu.print_menu('Поле для поиска', mod_personal.person_data_columns)
    find_column = ui_menu.get_select_menu(mod_personal.person_data_columns)
    find_str = input(f'Введите {mod_personal.person_data_columns[find_column]} клиента:')

    find_client = mod_client.find_client_by(find_column, find_str)
    if find_client is not None:
        print_company_client(find_client)
    else:
        print('Клиент не найден!')


# КЛИЕНТЫ - 7 Загрузить из файла
def load_company_client_from_file():
    print('\n7) Загрузка из файла:')
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_client.load_company_clients_from_file_csv()
    else:
        print('Unknown format file')


# КЛИЕНТЫ - 8 Сохранить в файл
def save_company_client_to_file():
    print('\n8) Сохранение в файл:')
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_client.save_company_clients_to_file_csv()
    else:
        print('Unknown format file')


def run_main_menu_clients():
    menu_clients = ui_menu.load_menu_client()

    select_menu_clients = 1
    while select_menu_clients != 0:
        ui_menu.print_menu('Клиенты', menu_clients)
        select_menu_clients = ui_menu.get_select_menu(menu_clients)

        # Показать кол-во клиентов
        if select_menu_clients == 1:
            print_count_company_clients()
        # Показать клиентов
        elif select_menu_clients == 2:
            print_company_clients()
        # Добавить клиента
        elif select_menu_clients == 3:
            add_company_client()
        # Редактировать клиента
        elif select_menu_clients == 4:
            edit_company_client()
        # Удалить клиента
        elif select_menu_clients == 5:
            delete_company_client()
        # Найти клиента
        elif select_menu_clients == 6:
            find_company_client()
        # Загрузить из файла
        elif select_menu_clients == 7:
            load_company_client_from_file()
        # Сохранить в файл
        elif select_menu_clients == 8:
            save_company_client_to_file()
        else:
            break
