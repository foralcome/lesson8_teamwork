company = None
company_data_keys = ['id', 'title', 'city']


def init(new_company=None):
    global company

    if isinstance(new_company, dict):
        company = new_company
    else:
        company = {}


def get_company():
    return company
