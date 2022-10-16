personal = None
person_data_columns = {'id': 'Id', 'post': 'Должность', 'soname': 'Фамилия', 'name': 'Имя', 'email': 'E-mail',
                       'date_birthday': 'Дата рождения', 'phone': 'Телефон', 'description': 'Примечание'}


def init(new_personal=None):
    global personal
    if isinstance(new_personal, dict):
        personal = new_personal
    else:
        personal = []


def create(data):
    return dict(zip(person_data_columns, data))


def get_personal():
    return personal


def add_personal(person):
    global personal

    if personal is None:
        personal = []

    personal.append(person)
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

    if personal is None:
        return False

    for i in range(len(personal)):
        if personal[i][column] == value:
            personal.pop(i)
            return True
    return False
