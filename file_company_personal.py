import company_personal as mod_personal


def save_company_personal_to_file_csv(file_name='personal.csv', separator=';'):
    with open(file_name, 'w') as file_data:
        personal = mod_personal.get_personal()
        for person in personal:
            file_data.write(separator.join(person.values()) + '\n')
    return True


def load_company_personal_from_file_csv(file_name='personal.csv', separator=';'):
    global csv_format_data

    personal = mod_personal.get_personal()
    with open(file_name, 'r') as file_data:
        for line_data in file_data:
            personal_data = line_data.rstrip().split(separator, len(mod_personal.person_data_columns))
            person = mod_personal.create(zip(mod_personal.person_data_columns, personal_data))
            personal.append(person)
    return True