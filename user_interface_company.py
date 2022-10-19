import id_generator as mod_id
import company as mod_company
import company_personal as mod_personal
import company_client as mod_client
import file_company as mod_file_company
import file_company_personal as mod_file_company_personal
import file_company_client as mod_file_company_client

import user_interface_menu as ui_menu


# КОМПАНИЯ - 1 Создать компанию
def create_company():
    print('\n1) Создать компанию:')
    new_company = {}
    for data_key in mod_company.company_data_keys:
        if data_key == 'id':
            new_company[data_key] = mod_id.get_uuid_string()
            continue
        new_company[data_key] = input(f'Введите {data_key}:')
    check = input("всё верно? (введите '1' если да или '0' для отмены): ")
    if not check.isdigit() or int(check) != 1:
        return False

    mod_company.init(new_company)
    mod_personal.init()
    mod_client.init()


# КОМПАНИЯ - 2 Показать информацию о компании
def print_company():
    print('\n2) Информация о компании:')
    c = mod_company.get_company()
    print(f"Название: {c['title']}")
    print(f"Город: {c['city']}")
    print(f"Сотрудников: {mod_personal.get_size_personal()}")
    print(f"Клиентов: {mod_client.get_count_clients()}")


# КОМПАНИЯ - 3 Загрузить из файла
def load_company_from_file():
    print('\n3) Загрузить из файла:')
    menu_file_format = ui_menu.load_menu_file_format()
    #ui_menu.print_menu('Формат файла', menu_file_format)
    #select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    select_menu_file_format = 1
    if select_menu_file_format == 1:
        if mod_file_company.load_company_from_file_csv():
            mod_file_company_personal.load_company_personal_from_file_csv()
            mod_file_company_client.load_company_clients_from_file_csv()
            print('Успешная загрузка из файла!')
        else:
            print('Ошибка загрузки из файла! Проверьте доступность файла и повторите попытку.')
    else:
        print('Unknown format file')


# КОМПАНИЯ - Сохранить в файл
def save_company_to_file():
    print('\n4) Сохранить в файл:')
    menu_file_format = ui_menu.load_menu_file_format()
    ui_menu.print_menu('Формат файла', menu_file_format)
    select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    if select_menu_file_format == 1:
        mod_file_company.save_company_to_file_csv()
        mod_file_company_personal.save_company_personal_to_file_csv()
        mod_file_company_client.save_company_clients_to_file_csv()
    else:
        print('Unknown format file')


def run_main_menu_company():
    menu_company = ui_menu.load_menu_company()

    select_menu_company = 1
    while select_menu_company != 0:
        ui_menu.print_menu('Компания', menu_company)
        select_menu_company = ui_menu.get_select_menu(menu_company)

        is_init_company = False
        if mod_company.get_company() is not None:
            is_init_company = True

        # Создать компанию
        if select_menu_company == 1:
            create_company()
        # Показать информацию о компании
        elif select_menu_company == 2:
            if not is_init_company:
                print('\nКомпания не создана!')
            else:
                print_company()
        # Загрузить из файла
        elif select_menu_company == 3:
            load_company_from_file()
        # Сохранить в файл
        elif select_menu_company == 4:
            if not is_init_company:
                print('\nКомпания не создана!')
            else:
                save_company_to_file()
        else:
            break
