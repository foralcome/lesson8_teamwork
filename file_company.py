import company as mod_company


def save_company_to_file_csv(file_name='company.csv', separator=';'):
    with open(file_name, 'w') as file_data:
        company = mod_company.get_company()
        file_data.write(separator.join(company.values()) + '\n')
    return True


def load_company_from_file_csv(file_name='company.csv', separator=';'):
    with open(file_name, 'r') as file_data:
        for line_data in file_data:
            company_data = line_data.rstrip().split(separator)
            if len(company_data) != len(mod_company.company_data_keys):
                continue
            mod_company.init(dict(zip(mod_company.company_data_keys, company_data)))
            break
    return True
