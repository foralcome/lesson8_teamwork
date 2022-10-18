personal = None
size_personal = 0
person_data_columns = {'id': 'Id', 'post': 'Должность', 'soname': 'Фамилия', 'name': 'Имя', 'email': 'E-mail',
                       'date_birthday': 'Дата рождения', 'phone': 'Телефон', 'description': 'Примечание'}


def init(new_personal=None):
    global personal
    if isinstance(new_personal, list):
        personal = new_personal
    else:
        personal = []

    global size_personal
    size_personal = len(personal)


def get_size_personal():
    return size_personal


def get_personal():
    return personal


def add_personal(person):
    global personal
    global size_personal

    if personal is None:
        personal = []

    personal.append(person)
    size_personal += 1
    return True


def find_person_by(column, value):
    global personal

    if personal is None:
        return None

    for person in personal:
        if person[column] == value:
            return person
    return None


def delete_person_by(column, value):
    global personal
    global size_personal

    if personal is None:
        return False

    for i in range(len(personal)):
        if personal[i][column] == value:
            personal.pop(i)
            size_personal -= 1
            return True
    return False
