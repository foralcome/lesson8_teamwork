import company_personal as mod_personal
import os.path

def save_company_personal_to_file_csv(file_name='personal.csv', separator=';'):
    with open(file_name, 'w') as file_data:
        personal = mod_personal.get_personal()
        if personal is not None:
            for person in personal:
                file_data.write(separator.join(person.values()) + '\n')
    return True


def load_company_personal_from_file_csv(file_name='personal.csv', separator=';'):
    if not os.path.exists(file_name):
        return False

    personal = []
    with open(file_name, 'r') as file_data:
        for line_data in file_data:
            personal_data = line_data.rstrip().split(separator)
            if len(personal_data) != len(mod_personal.person_data_columns):
                continue
            personal.append(dict(zip(mod_personal.person_data_columns, personal_data)))
    mod_personal.init(personal)
    return True
