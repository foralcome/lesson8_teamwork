company = None
company_data_keys = ['id', 'title', 'city']


def init(new_company=None):
    global company

    if isinstance(new_company, dict):
        company = new_company
    else:
        company = {}


def create(title, city):
    global company

    if company is None:
        company = {}

    company['title'] = title
    company['city'] = city


def get_company():
    return company
