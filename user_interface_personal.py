import id_generator as mod_id
import company_personal as mod_personal
import file_company_personal as mod_file_personal
import user_interface_menu as ui_menu


# СОТРУДНИКИ - 1 Показать кол-во сотрудников
def print_size_company_personal():
    print('\n1) В организации:', mod_personal.get_size_personal(), 'сотрудников')


# СОТРУДНИКИ - 0 Показать сотрудника
def print_company_person(person):
    print('\nСотрудник организации:')
    for person_data_column in mod_personal.person_data_columns:
        print(f'{mod_personal.person_data_columns[person_data_column]}: {person[person_data_column]}')


def print_company_person_mini(person):
    print(f"UUID: {person['id']}")
    print(f"Дожность: {person['post']}")
    print(f"ФИО: {person['soname']} {person['soname']}")
    print(f"Контакты: {person['phone']}, e-mail {person['email']}")


# СОТРУДНИКИ - 1 Показать сотрудников
def print_company_personal():
    print('\n1) Сотрудники организации:')
    if mod_personal.get_size_personal() == 0:
        print('в компании нет сотрудников')
    else:
        for person in mod_personal.get_personal():
            print_company_person_mini(person)


# СОТРУДНИКИ - 2 Добавить сотрудника
def add_company_personal():
    personal = mod_personal.get_personal()

    new_person = {}
    for data_key in mod_personal.person_data_columns:
        if data_key == 'id':
            new_person[data_key] = mod_id.get_uuid_string()
            continue
        new_person[data_key] = input(f'Введите {data_key}:')
    check = input("всё верно? (введите '1' если да или '0' для отмены): ")
    if not check.isdigit() or int(check) != 1:
        return False

    personal.append(new_person)
    mod_personal.size_personal += 1
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


def run_main_menu_personal():
    menu_personal = ui_menu.load_menu_personal()

    select_menu_personal = 1
    while select_menu_personal != 0:
        ui_menu.print_menu('Сотрудники', menu_personal)
        select_menu_personal = ui_menu.get_select_menu(menu_personal)

        # Показать кол-во сотрудников
        if select_menu_personal == 1:
            print_size_company_personal()
        # Показать сотрудников
        elif select_menu_personal == 2:
            print_company_personal()
        # Добавить сотрудника
        elif select_menu_personal == 3:
            add_company_personal()
        # Редактировать сотрудника
        elif select_menu_personal == 4:
            edit_company_personal()
        # Удалить сотрудника
        elif select_menu_personal == 5:
            delete_company_personal()
        # Найти сотрудника
        elif select_menu_personal == 6:
            find_company_personal()
        # Загрузить из файла
        elif select_menu_personal == 7:
            load_company_personal_from_file()
        # Сохранить в файл
        elif select_menu_personal == 8:
            save_company_personal_to_file()
        else:
            break
