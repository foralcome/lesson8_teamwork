import company as mod_company
import user_interface_company as ui_company
import user_interface_personal as ui_personal
import user_interface_client as ui_client

import user_interface_menu as ui_menu


def run_main_menu():
    main_menu = ui_menu.load_menu_main()
    select_main_menu = 1
    while select_main_menu != 0:
        ui_menu.print_menu('ГЛАВНОЕ МЕНЮ', main_menu)
        select_main_menu = ui_menu.get_select_menu(main_menu)
        if select_main_menu == 0:
            break

        is_init_company = False
        if mod_company.get_company() is not None:
            is_init_company = True

        # Компания
        if select_main_menu == 1:
            ui_company.run_main_menu_company()
        # Сотрудники
        elif select_main_menu == 2:
            if not is_init_company:
                print('\nКомпания не создана!')
            else:
                ui_personal.run_main_menu_personal()
        # Клиенты
        elif select_main_menu == 3:
            if not is_init_company:
                print('\nКомпания не создана!')
            else:
                ui_client.run_main_menu_clients()
        # Заказы
        elif select_main_menu == 4:
            print('\nОперация временно не доступна!')
            continue
        # run_main_menu_orders()
        # Выход
        else:
            break
