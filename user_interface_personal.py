import id_generator as mod_id
import company_personal as mod_personal
import file_company_personal as mod_file_personal
import user_interface_menu as ui_menu


# СОТРУДНИКИ - 1 Показать кол-во сотрудников
def print_size_company_personal():
    print('\n1) В организации:', mod_personal.get_size_personal(), 'сотрудников')


# СОТРУДНИКИ - 2 Показать сотрудника
def print_company_person(person):
    print('\n2) Сотрудник организации:')
    for person_data_column in mod_personal.person_data_columns:
        print(f'{mod_personal.person_data_columns[person_data_column]}: {person[person_data_column]}')


def print_company_person_mini(person):
    print(f"UUID: {person['id']}")
    print(f"Дожность: {person['post']}")
    print(f"ФИО: {person['soname']} {person['soname']}")
    print(f"Контакты: {person['phone']}, e-mail {person['email']}")


# СОТРУДНИКИ - 2 Показать сотрудников
def print_company_personal():
    print('\n2) Сотрудники организации:')
    if mod_personal.get_size_personal() == 0:
        print('в компании нет сотрудников')
    else:
        for person in mod_personal.get_personal():
            print_company_person_mini(person)
            print()


# СОТРУДНИКИ - 3 Добавить сотрудника
def add_company_personal():
    print('\n3) Добавление сотрудника:')

    new_person = {}
    for data_key in mod_personal.person_data_columns:
        if data_key == 'id':
            new_person[data_key] = mod_id.get_uuid_string()
            continue
        new_person[data_key] = input(f'Введите {data_key}:')
    check = input("всё верно? (введите '1' если да или '0' для отмены): ")
    if not check.isdigit() or int(check) != 1:
        return False

    mod_personal.add_personal(new_person)
    return True


# СОТРУДНИКИ - 4 Редактировать сотрудника
def edit_company_personal():
    personal = mod_personal.get_personal()
    keys_menu = range(1, len(personal) + 1)
    values_menu = [(x['soname'] + ' ' + x['name']) for x in personal]
    personal_menu = dict(zip(keys_menu, values_menu))
    ui_menu.print_menu('Выберите сотрудника', personal_menu)
    select_id = ui_menu.get_select_menu(personal_menu)

    id_personal = [x['id'] for x in personal]
    find_id = id_personal[select_id - 1]
    find_person = mod_personal.find_person_by('id', find_id)

    print('Ввод новых значений:')
    for data_key in mod_personal.person_data_columns:
        if data_key == 'id':
            continue
        input_data = input(f"Введите {data_key} (было '{find_person[data_key]}'):")
        if len(input_data) != 0:
            find_person[data_key] = input_data


# СОТРУДНИКИ - 5 Удалить сотрудника
def delete_company_personal():
    print('\n5) Удаление сотрудника:')
    indexes_menu = range(1, len(mod_personal.person_data_columns) + 1)
    keys_menu = list(mod_personal.person_data_columns.keys())
    values_menu = mod_personal.person_data_columns.values()
    column_menu = dict(zip(indexes_menu, values_menu))
    ui_menu.print_menu('Удалить по значению', column_menu)
    find_column_id = ui_menu.get_select_menu(column_menu)
    find_column = keys_menu[find_column_id - 1]
    find_str = input(f'Введите значение для поиска:')

    if mod_personal.delete_person_by(find_column, find_str):
        print('Сотрудник удылён!')
    else:
        print(f'Сотрудника с {find_column} = {find_str} не найден!')


# СОТРУДНИКИ - 6 Найти сотрудника
def find_company_personal():
    print('\n6) Найти сотрудника:')
    indexes_menu = range(1, len(mod_personal.person_data_columns) + 1)
    keys_menu = list(mod_personal.person_data_columns.keys())
    values_menu = mod_personal.person_data_columns.values()
    column_menu = dict(zip(indexes_menu, values_menu))
    ui_menu.print_menu('Удалить по значению', column_menu)
    find_column_id = ui_menu.get_select_menu(column_menu)
    find_column = keys_menu[find_column_id - 1]
    find_str = input(f'Введите значение для поиска:')

    find_person = mod_personal.find_person_by(find_column, find_str)
    if find_person is not None:
        print('Сотрудник не найден!')
        print_company_person_mini(find_person)
    else:
        print(f'Сотрудника с {find_column} = {find_str} не найден!')


# СОТРУДНИКИ - 7 Загрузить из файла
def load_company_personal_from_file():
    print('\n7) Загрузка из файла:')
    menu_file_format = ui_menu.load_menu_file_format()
    # ui_menu.print_menu('Формат файла', menu_file_format)
    # select_menu_file_format = ui_menu.get_select_menu(menu_file_format)
    select_menu_file_format = 1
    if select_menu_file_format == 1:
        if mod_file_personal.load_company_personal_from_file_csv():
            print('Успешная загрузка из файла!')
        else:
            print('Ошибка загрузки из файла! Проверьте доступность файла и повторите попытку.')
    else:
        print('Unknown format file')


# СОТРУДНИКИ - 8 Сохранить в файл
def save_company_personal_to_file():
    print('\n8) Сохранение в файл:')
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

        is_init_personal = False
        if mod_personal.get_personal() is not None and len(mod_personal.get_personal()) > 0:
            is_init_personal = True

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
            if not is_init_personal:
                print('\nПерсонал не создан!')
            else:
                edit_company_personal()
        # Удалить сотрудника
        elif select_menu_personal == 5:
            if not is_init_personal:
                print('\nПерсонал не создан!')
            else:
                delete_company_personal()
        # Найти сотрудника
        elif select_menu_personal == 6:
            if not is_init_personal:
                print('\nПерсонал не создан!')
            else:
                find_company_personal()
        # Загрузить из файла
        elif select_menu_personal == 7:
            load_company_personal_from_file()
        # Сохранить в файл
        elif select_menu_personal == 8:
            if not is_init_personal:
                print('\nПерсонал не создан!')
            else:
                save_company_personal_to_file()
        else:
            break
