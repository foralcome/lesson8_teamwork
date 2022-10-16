import company as mod_company
import company_personal as mod_personal
import company_client as mod_client
import file_company as mod_file_company
import file_company_personal as mod_file_personal
import file_company_client as mod_file_client

import user_interface_menu as ui_menu


# КОМПАНИЯ - 1 Создать компанию
def create_company():
    title = input('введите название компании: ')
    city = input('введите город нахождения: ')
    c = mod_company.create(title, city)


# КОМПАНИЯ - 2 Показать информацию о компании
def print_company():
    title = input('введите название компании: ')
    city = input('введите город нахождения: ')
    c = mod_company.get_company()
    print(f"компания {c['title']} ({c['city']})")


# КОМПАНИЯ - 3 Загрузить из файла
def load_company_from_file():
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_company.load_company_from_file_csv()
    else:
        print('Unknown format file')

# КОМПАНИЯ - Сохранить в файл
def save_company_to_file():
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_company.save_company_to_file_csv()
    else:
        print('Unknown format file')

# СОТРУДНИКИ - 0 Показать сотрудника
def print_company_person(person):
    print(f"{person['post']}: {person['soname']} {person['name']} (тел. {person['phone']}, e-mail {person['email']})")


# СОТРУДНИКИ - 1 Показать сотрудников
def print_company_personal():
    personal = mod_personal.get_personal()
    for person in personal:
        print(f"{person['post']}: {person['soname']} {person['name']} (тел. {person['phone']}, e-mail {person['email']})")

# СОТРУДНИКИ - 2 Добавить сотрудника
def add_company_personal():
    personal = mod_personal.get_personal()

    new_person = {}
    for data_key in mod_personal.person_data_columns:
        new_person[data_key] = input(f'Введите {data_key}:')
    check = input("всё верно? (введите '1' если да или '0' для отмены): ")
    if not check.isdigit() or int(check) != 1:
        return False

    personal.append(new_person)
    return True


# СОТРУДНИКИ - 3 Редактировать сотрудника
def edit_company_personal():
    return False


# СОТРУДНИКИ - 4 Удалить сотрудника
def delete_company_personal():
    ui_menu.print_menu('Удалить по значению', mod_personal.person_data_columns)
    find_column = ui_menu.get_select_menu(mod_personal.person_data_columns)
    find_str = input(f'Введите {mod_personal.person_data_columns[find_column]} сотрудника:')

    if mod_personal.find_person_by(find_column, find_str):
        mod_personal.delete_person_by(find_column, find_str)
    else:
        print(f'Сотрудника с {find_column} = {find_str} не найден!')
        return False
    return True


# СОТРУДНИКИ - 5 Найти сотрудника
def find_company_personal():
    ui_menu.print_menu('Поле для поиска', mod_personal.person_data_columns)
    find_column = ui_menu.get_select_menu(mod_personal.person_data_columns)
    find_str = input(f'Введите {mod_personal.person_data_columns[find_column]} сотрудника:')

    find_person = mod_personal.find_person_by(find_column, find_str)
    if find_person is not None:
        print_company_person(find_person)
    else:
        print('Сотрудник не найден!')


# СОТРУДНИКИ - 6 Загрузить из файла
def load_company_personal_from_file():
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_personal.load_company_personal_from_file_csv()
    else:
        print('Unknown format file')


# СОТРУДНИКИ - 7 Сохранить в файл
def save_company_personal_to_file():
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_personal.save_company_personal_to_file_csv()
    else:
        print('Unknown format file')


# КЛИЕНТЫ - 0 Показать клиента
def print_company_client(client):
    print(f"{client['soname']} {client['name']}, тел.{client['phone']} // {client['description']}")

# КЛИЕНТЫ - 1 Показать клиентов
def print_company_clients():
    clients = mod_client.get_clients()
    for client in clients:
        print(client)


# КЛИЕНТЫ - 2 Добавить клиента
def add_company_client():
    clients = mod_client.get_clients()

    new_client = {}
    for data_key in mod_client.client_data_columns:
        new_client[data_key] = input(f'Введите {data_key}:')
    check = input("всё верно? (введите '1' если да или '0' для отмены): ")
    if not check.isdigit() or int(check) != 1:
        return False

    clients.append(new_client)
    return True


# КЛИЕНТЫ - 3 Редактировать клиента
def edit_company_client():
    return False


# КЛИЕНТЫ - 4 Удалить клиента
def delete_company_client():
    ui_menu.print_menu('Удалить по значению', mod_client.client_data_columns)
    find_column = ui_menu.get_select_menu(mod_client.client_data_columns)
    find_str = input(f'Введите {mod_client.client_data_columns[find_column]} клиента:')

    if mod_client.find_client_by(find_column, find_str):
        mod_client.delete_client_by(find_column, find_str)
    else:
        print(f'Сотрудника с {find_column} = {find_str} не найден!')
        return False
    return True


# КЛИЕНТЫ - 5 Найти клиента
def find_company_client():
    ui_menu.print_menu('Поле для поиска', mod_personal.person_data_columns)
    find_column = ui_menu.get_select_menu(mod_personal.person_data_columns)
    find_str = input(f'Введите {mod_personal.person_data_columns[find_column]} клиента:')

    find_client = mod_client.find_client_by(find_column, find_str)
    if find_client is not None:
        print_company_client(find_client)
    else:
        print('Клиент не найден!')


# КЛИЕНТЫ - 6 Загрузить из файла
def load_company_client_from_file():
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_client.load_company_clients_from_file_csv()
    else:
        print('Unknown format file')


# КЛИЕНТЫ - 7 Сохранить в файл
def save_company_client_to_file():
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_client.save_company_clients_to_file_csv()
    else:
        print('Unknown format file')


def run_main_menu_company():
    menu_company = ui_menu.load_menu_company()

    select_menu_company = 1
    while select_menu_company != 0:
        ui_menu.print_menu('Компания', menu_company)
        select_menu_company = ui_menu.get_select_menu(menu_company)

        # Создать компанию
        if select_menu_company == 1:
            create_company()
        # Показать информацию о компании
        elif select_menu_company == 2:
            print_company()
        # Загрузить из файла
        elif select_menu_company == 3:
            load_company_from_file()
        # Сохранить в файл
        elif select_menu_company == 4:
            save_company_to_file()
        else:
            break


def run_main_menu_clients():
    menu_clients = ui_menu.load_menu_client()

    select_menu_clients = 1
    while select_menu_clients != 0:
        ui_menu.print_menu('Клиенты', menu_clients)
        select_menu_clients = ui_menu.get_select_menu(menu_clients)

        # Показать клиентов
        if select_menu_clients == 1:
            print_company_clients()
        # Добавить клиента
        elif select_menu_clients == 2:
            add_company_client()
        # Редактировать клиента
        elif select_menu_clients == 3:
            edit_company_client()
        # Удалить клиента
        elif select_menu_clients == 4:
            delete_company_client()
        # Найти клиента
        elif select_menu_clients == 5:
            find_company_client()
        # Загрузить из файла
        elif select_menu_clients == 6:
            load_company_client_from_file()
        # Сохранить в файл
        elif select_menu_clients == 7:
            save_company_client_to_file()
        else:
            break


def run_main_menu_personal():
    menu_personal = ui_menu.load_menu_personal()

    select_menu_personal = 1
    while select_menu_personal != 0:
        ui_menu.print_menu('Сотрудники', menu_personal)
        select_menu_personal = ui_menu.get_select_menu(menu_personal)

        # Показать сотрудников
        if select_menu_personal == 1:
            print_company_personal()
        # Добавить сотрудника
        elif select_menu_personal == 2:
            add_company_personal()
        # Редактировать сотрудника
        elif select_menu_personal == 3:
            edit_company_personal()
        # Удалить сотрудника
        elif select_menu_personal == 4:
            delete_company_personal()
        # Найти сотрудника
        elif select_menu_personal == 5:
            find_company_personal()
        # Загрузить из файла
        elif select_menu_personal == 6:
            load_company_personal_from_file()
        # Сохранить в файл
        elif select_menu_personal == 7:
            save_company_personal_to_file()
        else:
            break


def run_main_menu():
    company = mod_company.get_company()

    main_menu = ui_menu.load_menu_main()
    select_main_menu = 1
    while select_main_menu != 0:
        ui_menu.print_menu('ГЛАВНОЕ МЕНЮ', main_menu)
        select_main_menu = ui_menu.get_select_menu(main_menu)
        if select_main_menu == 0:
            break

        # Компания
        if select_main_menu == 1:
            run_main_menu_company()
        # Сотрудники
        elif select_main_menu == 2:
            run_main_menu_personal()
        # Клиенты
        elif select_main_menu == 3:
            run_main_menu_clients()
        # Заказы
        elif select_main_menu == 4:
            continue
            # run_main_menu_orders()
        # Выход
        else:
            break