def load_menu_file_format():
    menu_format = {}
    menu_format[1] = 'CSV'
    menu_format[2] = 'JSON'
    menu_format[3] = 'XML'
    menu_format[0] = 'отмена'
    return menu_format


def load_menu_main():
    menu = {}
    menu[1] = 'Компания'
    menu[2] = 'Сотрудники'
    menu[3] = 'Клиенты'
    menu[4] = 'Заказы'
    menu[0] = 'выход'
    return menu


def load_menu_company():
    menu_company = {}
    menu_company[1] = 'Создать компанию'
    menu_company[2] = 'Показать информацию о компании'
    menu_company[3] = 'Загрузить из файла'
    menu_company[4] = 'Сохранить в файл'
    menu_company[0] = 'назад'
    return menu_company


def load_menu_personal():
    menu_personal = {}
    menu_personal[1] = 'Показать кол-во сотрудников'
    menu_personal[2] = 'Показать сотрудников'
    menu_personal[3] = 'Добавить сотрудника'
    menu_personal[4] = 'Редактировать сотрудника'
    menu_personal[5] = 'Удалить сотрудника'
    menu_personal[6] = 'Найти сотрудника'
    menu_personal[7] = 'Загрузить из файла'
    menu_personal[8] = 'Сохранить в файл'
    menu_personal[0] = 'отмена'
    return menu_personal


def load_menu_client():
    menu_client = {}
    menu_client[1] = 'Показать кол-во клиентов'
    menu_client[2] = 'Показать клиентов'
    menu_client[3] = 'Добавить клиента'
    menu_client[4] = 'Редактировать клиента'
    menu_client[5] = 'Удалить клиента'
    menu_client[6] = 'Найти клиента'
    menu_client[7] = 'Загрузить из файла'
    menu_client[8] = 'Сохранить в файл'
    menu_client[0] = 'отмена'
    return menu_client


def print_menu(menu_title, menu_data):
    print(f'\n----- {menu_title} -----')

    for key_menu, title_menu in menu_data.items():
        print(key_menu, '-', title_menu)


def get_select_menu(menu):
    select_str = input('выберите пункт меню: ')
    while not select_str.isdigit() or int(select_str) not in menu.keys():
        print('error - указан неверный пункт меню!')
        select_str = input('выберите пункт меню: ')
    return int(select_str)
